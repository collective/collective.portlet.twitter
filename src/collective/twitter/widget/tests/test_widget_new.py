# -*- coding: utf-8 -*-

import unittest2 as unittest

from collective.twitter.widget.testing import INTEGRATION_TESTING

from plone.portlets.interfaces import IPortletType

from zope.component import getUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles


class WidgetNewTest(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_portlet_addview_registered(self):
        portlet = getUtility(
            IPortletType,
            name='collective.twitter.widget.WidgetNewPortlet')

        self.assertEqual(portlet.addview,
                         'collective.twitter.widget.WidgetNewPortlet')

    def test_portlet_title_registered(self):
        portlet = getUtility(IPortletType,
                             name='collective.twitter.widget.WidgetNewPortlet')

        self.assertEqual(u"Twitter Widget (new)", portlet.title)
