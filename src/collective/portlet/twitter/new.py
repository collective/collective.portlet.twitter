# -*- coding: utf-8 -*-
from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema

from zope.formlib import form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.portlet.twitter import _
from collective.portlet.twitter.config import PROJECTNAME

import logging

logger = logging.getLogger(PROJECTNAME)


class IWidgetNewPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    data_id = schema.TextLine(title=_(u'Data Widget ID'),
                              description=_(u"Create new Widget in \
                                      https://twitter.com/settings/widgets \
                                      and input ID"))

    twitter = schema.TextLine(title=_(u"Twitter Account"),
                              description=_(u"@twitter"))

    theme = schema.TextLine(title=_(u"Theme"),
                            description=_(u"Theme client side configuration"),
                            required=False)

    link_color = schema.TextLine(title=_(u"Link Color"),
                                 description=_(u"Link Color client side configuration"),
                                 required=False)

    width = schema.TextLine(title=_(u"Width"),
                            description=_(u"Width client side configuration"),
                            required=False)

    height = schema.TextLine(title=_(u"Height"),
                             description=_(u"Height client side configuration"),
                             required=False)

    chrome = schema.TextLine(title=_(u"Chrome"),
                             description=_(u"Chrome client side configuration"),
                             required=False)

    border_color = schema.TextLine(title=_(u"Border color"),
                                   description=_(u"Border color client side configuration"),
                                   required=False)

    language = schema.TextLine(title=_(u"Language"),
                               description=_(u"Language client side configuration"),
                               required=False)

    related = schema.TextLine(title=_(u"Web Intent Related Users"),
                              description=_(u"Web Intent Related Users client side configuration"),
                              required=False)

    aria = schema.TextLine(title=_(u"ARIA politeness"),
                           description=_(u"ARIA politeness client side configuration"),
                           required=False)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IWidgetNewPortlet)
    data_id = u""
    twitter = u""

    def __init__(self, theme=None, link_color=None, width=None, height=None,
                 chrome=None, border_color=None, language=None, related=None,
                 aria=None, data_id=u"", twitter=u""):
        self.data_id = data_id
        self.twitter = twitter
        self.theme = theme
        self.link_color = link_color
        self.width = width
        self.height = height
        self.chrome = chrome
        self.border_color = border_color
        self.language = language
        self.related = related
        self.aria = aria

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Twitter Widget (New) [%s]" % self.data_id


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('new.pt')

    def getDataId(self):
        """
        Returns the data id for the portlet
        """
        return self.data.data_id

    def getUrl(self):
        """ Returns the url for themplate portlet
        """
        return "http://twitter.com/%s" % self.data.twitter

    def getText(self):
        """ Returns the text for themplate pertlet
        """
        return "Tweets by %s" % self.data.twitter

    def get_attributes(self):
        attr = {'data-widget-id': self.getDataId(),
                'href': self.getUrl()}

        if self.data.theme:
            attr['data-theme'] = self.data.theme
        if self.data.link_color:
            attr['data-link-color'] = self.data.link_color
        if self.data.width:
            attr['width'] = self.data.width
        if self.data.height:
            attr['height'] = self.data.height
        if self.data.chrome:
            attr['data-chrome'] = self.data.chrome
        if self.data.border_color:
            attr['data-border-color'] = self.data.border_color
        if self.data.language:
            attr['data-language'] = self.data.language
        if self.data.chrome:
            attr['data-related'] = self.data.related
        if self.data.aria:
            attr['data-aria-polite'] = self.data.aria

        return attr

    def get_html_tag(self):
        attrs_str = ""
        attrs = self.get_attributes()
        for attr in attrs.keys():
            attrs_str += "%s='%s' " % (attr, attrs[attr])
        return "<a class='twitter-timeline'  %s >%s</a>" % (attrs_str,
                                                            self.getText())


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IWidgetNewPortlet)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IWidgetNewPortlet)
