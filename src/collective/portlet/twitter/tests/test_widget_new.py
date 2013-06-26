# -*- coding: utf-8 -*-

import unittest2 as unittest

from collective.portlet.twitter.new import Assignment, Renderer
from collective.portlet.twitter.testing import INTEGRATION_TESTING

from plone.portlets.interfaces import IPortletType, IPortletManager, IPortletRenderer

from zope.component import getUtility, getMultiAdapter

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class WidgetNewTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def _get_portlet_renderer(self, assignment):
        context = self.portal
        request = self.portal.REQUEST
        view = context.restrictedTraverse('@@plone')
        manager = getUtility(IPortletManager, name='plone.rightcolumn', context=context)
        renderer = getMultiAdapter((context, request, view, manager, assignment), IPortletRenderer)
        return renderer

    def test_portlet_render(self):
        assignment = Assignment(data_id=u"0", twitter=u"plone")
        renderer = self._get_portlet_renderer(assignment)

        self.failUnless(isinstance(renderer, Renderer))
        self.failUnless(renderer.available,
                        "Renderer should be available by default.")

        self.assertEqual(renderer.get_html_tag(),
                         "<a class='twitter-timeline'  href='http://twitter.com/plone' data-widget-id='0'  >Tweets by plone</a>")
        html = renderer.render()
        self.assertIn('<dl', html)
        self.assertIn('<script>', html)
        self.assertIn(renderer.get_html_tag(), html)

    def test_portlet_render_options(self):
        assignment = Assignment(data_id=u"0",
                                twitter=u"plone",
                                omit_border=True)
        renderer = self._get_portlet_renderer(assignment)
        html = renderer.render()
        self.assertNotIn('<dl', html)


    def test_portlet_addview_registered(self):
        portlet = getUtility(
            IPortletType,
            name='collective.portlet.twitter.TwitterBoxPortlet')

        self.assertEqual(portlet.addview,
                         'collective.portlet.twitter.TwitterBoxPortlet')

    def test_portlet_title_registered(self):
        portlet = getUtility(IPortletType,
                             name='collective.portlet.twitter.TwitterBoxPortlet')

        self.assertEqual(u"Twitter Widget (new)", portlet.title)
