**********************
Twitter Widget Portlet
**********************

.. contents:: Table of Contents

Life, the Universe, and Everything
----------------------------------

This portlet allows you to easily embed and customise JavaScript-based Twitter
widgets into your Plone site.

To read and understand more about such widgets, and to create your own, visit 
https://twitter.com/settings/widgets.

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.portlet.twitter.png?branch=master
    :target: http://travis-ci.org/collective/collective.portlet.twitter

.. image:: https://coveralls.io/repos/collective/collective.portlet.twitter/badge.png?branch=master
    :target: https://coveralls.io/r/collective/collective.portlet.twitter

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

Don't Panic
-----------

Installation
^^^^^^^^^^^^

To enable this package in a buildout-based installation:

1. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.portlet.twitter

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.portlet.twitter`` and click the 'Activate'
button.

.. Note::

    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.

Usage
^^^^^

Create twitter widget:

.. image:: https://raw.github.com/collective/collective.portlet.twitter/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.54.19%20AM.png

Configure widget:

.. image:: https://raw.github.com/collective/collective.portlet.twitter/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.54.58%20AM.png

Saved:

.. image:: https://raw.github.com/collective/collective.portlet.twitter/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.55.14%20AM.png

Get widget id:

.. image:: https://raw.github.com/collective/collective.portlet.twitter/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.55.14%20AM-Get_id.png

Add your widget ID into the **Data Widget ID** field as follows:

.. image:: https://raw.github.com/collective/collective.portlet.twitter/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.53.19%20AM.png

For more information on the variety of client-side options (such as theme,
link color, width, height, and so forth) that can be  configured within this
portlet's settings, see Twitter's development  documentation at
https://dev.twitter.com/docs/embedded-timelines#customization.

Make any customisations you'd like and click **Save**.

That's it!

.. image:: https://raw.github.com/collective/collective.portlet.twitter/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.52.39%20AM.png

.. _`opening a support ticket`: https://github.com/collective/collective.portlet.twitter/issues
