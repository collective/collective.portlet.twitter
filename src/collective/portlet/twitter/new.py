# -*- coding: utf-8 -*-
from cgi import escape
from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema

from zope.formlib import form

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.portlet.twitter import _
from collective.portlet.twitter.config import PROJECTNAME

import logging
import re

logger = logging.getLogger(PROJECTNAME)


class IWidgetNewPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    data_id = schema.TextLine(title=_(u'Data Widget ID'),
                              description=_(u"The numerical identifier for the Twitter widget to be displayed.  For example: 123456789098765432."))

    twitter = schema.TextLine(title=_(u"Twitter Account"),
                              description=_(u"Enter the Twitter account username that the portlet should link to. For example: @twitter."))

    header = schema.TextLine(title=_(u"Portlet header"),
                             description=_(u"Title of the rendered portlet."),
                             constraint=re.compile("[^\s]").match,
                             required=False)

    omit_border = schema.Bool(title=_(u"Omit portlet border"),
                              description=_(u"Tick this box if you want to render the portlet without the standard header, border or footer."),
                              required=True,
                              default=False)

    theme = schema.TextLine(title=_(u"Theme"),
                            description=_(u"Client side configuration. Sets the theme of the embedded widget. For example: dark."),
                            required=False)

    link_color = schema.TextLine(title=_(u"Link Color"),
                                 description=_(u"Client side configuration. Controls the color of links in the widget. For example: #cc0000."),
                                 required=False)

    width = schema.TextLine(title=_(u"Width"),
                            description=_(u"Client side configuration. Sets the width of the widget by way of the standard HTML width attribute. For example: 200px, 100%, or 10em."),
                            required=False)

    height = schema.TextLine(title=_(u"Height"),
                             description=_(u"Client side configuration. Sets theheight of the widget by way of the standard HTML height attribute.  For example: 200px, 50% or 10em."),
                             required=False)

    chrome = schema.TextLine(title=_(u"Chrome"),
                             description=_(u"Client side configuration. Enter space-separated options to control widget layout. For example: noheader nofooter noborders noscollbar transparent."),
                             required=False)

    border_color = schema.TextLine(title=_(u"Border Color"),
                                   description=_(u"Client side configuration. Controls the border color of the widget. For example: #cc0000."),
                                   required=False)

    language = schema.TextLine(title=_(u"Language"),
                               description=_(u"Client side configuration. Controls the HTML lang attribute for the widget. For example: fr."),
                               required=False)

    tweet_limit = schema.Int(title=_(u"Tweet Limit"),
                             description=_(u"Client side configuration. Controls the number of tweets shown in the timeline. The widget will be resized to show all tweets without scrolling. For example: 10."),
                             required=False)

    related = schema.TextLine(title=_(u"Web Intent Related Users"),
                              description=_(u"Client side configuration. Comma-separated list of usernames as suggested follows after tweet interaction. For example: plone,worldploneday."),
                              required=False)

    aria = schema.TextLine(title=_(u"ARIA Politeness"),
                           description=_(u"Client side configuration. Control how the widget may allow assistive technology to ineract with dynamic content. For example: assertive."),
                           required=False)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IWidgetNewPortlet)
    data_id = u""
    twitter = u""
    tweet_limit = None
    header = u"Twitter"
    omit_border = False

    def __init__(self, theme=None, link_color=None, width=None, height=None,
                 chrome=None, border_color=None, language=None,
                 tweet_limit=None, related=None, aria=None, data_id=u"",
                 twitter=u"", header=u"Twitter", omit_border=False):
        self.data_id = data_id
        self.twitter = twitter
        self.theme = theme
        self.link_color = link_color
        self.width = width
        self.height = height
        self.chrome = chrome
        self.border_color = border_color
        self.language = language
        self.tweet_limit = tweet_limit
        self.related = related
        self.aria = aria
        self.header = header
        self.omit_border = omit_border

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
        """ Returns the data id for the portlet.
        """
        return self.data.data_id

    def getUrl(self):
        """ Returns the Twitter url for the given user.
        """
        return "http://twitter.com/%s" % self.data.twitter

    def getText(self):
        """ Returns the text for the portlet.
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
        if self.data.tweet_limit:
            attr['data-tweet-limit'] = self.data.tweet_limit
        if self.data.related:
            attr['data-related'] = self.data.related
        if self.data.aria:
            attr['data-aria-polite'] = self.data.aria

        return attr

    def get_html_tag(self):
        attrs_str = ""
        attrs = self.get_attributes()
        for attr in attrs.keys():
            attrs_str += '%s="%s" ' % (attr, escape(attrs[attr], quote=True))
        return '<a class="twitter-timeline"  %s >%s</a>' % (attrs_str,
                                                            self.getText())


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IWidgetNewPortlet)
    label = _(u"Add Twitter Widget Portlet")
    description = _(u"This portlet displays an Embedded Timeline Twitter widget. Create a widget using the Twitter widgets page (https://twitter.com/settings/widgets) first.")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IWidgetNewPortlet)
    label = _(u"Edit Twitter Widget Portlet")
    description = _(u"This portlet displays an Embedded Timeline Twitter widget. Create a widget using the Twitter widgets page (https://twitter.com/settings/widgets) first.")

