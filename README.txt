Introduction
============

Reconstructs relative URLs in static portlets
in link and image tags. This cures a problem for static
portlets where link by uid is turned off.

Installation
============

Add this via buildout. Make sure to add a zcml entry for older Plones.

The product must be installed in Plone in order to add the browser layer
used to override the static portlet renderer.

Versions Tested
===============

- Plone 3.3.6

- Plone 4.1.4

This is an updated version of uwosh.static.fix from
uwosh's svn.