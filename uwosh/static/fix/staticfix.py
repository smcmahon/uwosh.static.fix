import os.path

from lxml import etree
from lxml import html
from Products.CMFCore.utils import getToolByName

from plone.portlet.static import static


class Renderer(static.Renderer):
    """Portlet renderer.
    Patch to fix relative links.  This class will reconstruct the links.
    In Plone 3.5, Kupu internal links are computed from the root,
    but do not include it. We add it back in.
    """

    def transformed(self, mt='text/x-html-safe'):
        results = static.Renderer.transformed(self, mt)

        self._portlet = None
        portlets = self.manager(self.context, self.request, self.view).portletsToShow()
        for portlet in portlets:
            if portlet['name'] == self.data.id:
                self._portlet = portlet

        if self._portlet == None:
            return results
        return self._reconstruct(results)

    def _reconstruct(self, text):
        site_root = getToolByName(self.context, 'portal_url').getPortalObject().absolute_url()
        nodes = html.fragment_fromstring(text.strip(), create_parent=True)
        for node in nodes.xpath('//*[@href]'):
            url = node.get('href')
            if not ('://' in url or 'mailto:' in url):
                url = os.path.join(site_root, url)
                node.set('href', url)
        return etree.tostring(nodes, pretty_print=False, encoding="utf-8")
