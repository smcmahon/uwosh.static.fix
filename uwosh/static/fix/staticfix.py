import os.path

from lxml import etree
from lxml import html
from Products.CMFCore.utils import getToolByName

from plone.portlet.static import static


class Renderer(static.Renderer):
    """Portlet renderer.
    Patch to fix relative href and src attributes
    in static portlets.
    Overrides the static portlet's transformed method
    to convert URLs relative to the site root into
    absolute URLs.
    """

    def transformed(self, mt='text/x-html-safe'):
        results = super(Renderer, self).transformed(mt)
        # results = static.Renderer.transformed(self, mt)

        self._portlet = None
        portlets = self.manager(self.context, self.request, self.view).portletsToShow()
        for portlet in portlets:
            if portlet['name'] == self.data.id:
                self._portlet = portlet
        if self._portlet == None:
            return results
        return self._reconstruct(results)

    def _reconstruct(self, text):
        site_root = getToolByName(
                self.context,
                'portal_url'
            ).getPortalObject().absolute_url()
        nodes = html.fragment_fromstring(
            text.strip(),
            create_parent=True)
        for node in nodes.xpath('//*[@href] | //*[@src]'):
            for attr in ('href', 'src'):
                url = node.get(attr)
                if url is not None:
                    if not ('://' in url or 'mailto:' in url):
                        url = os.path.join(site_root, url)
                        node.set(attr, url)
                    break
        return etree.tostring(nodes, pretty_print=False, encoding="utf-8")
