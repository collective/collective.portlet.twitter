Twitter Widget Portlet
======================

https://twitter.com/settings/widgets


Screenshot
----------

.. image:: https://raw.github.com/avelino/collective.twitter.widget.portlets/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.52.39%20AM.png


Install
-------

* When you're reading this you have probably already run ``easy_install collective.twitter.widget.portlets``. Find out how to install setuptools (and EasyInstall) here: http://peak.telecommunity.com/DevCenter/EasyInstall
* Create a file called ``collective.twitter.widget.portlets-configure.zcml`` in the ``/path/to/instance/etc/package-includes`` directory.  The file should only contain this


    <include package="collective.twitter.widget.portlets" />


Alternatively, if you are using zc.buildout and the plone.recipe.zope2instance recipe to manage your project, you can do this:

* Add ``collective.twitter.widget.portlets`` to the list of eggs to install, e.g.:

    [buildout]
    eggs = collective.twitter.widget.portlets

* Re-run buildout, e.g. with:

    $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package from another package's configure.zcml file.


HowTo
_____

Create twitter widget:

.. image:: https://raw.github.com/collective/collective.twitter.widget.portlets/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.54.19%20AM.png

Configure widget:

.. image:: https://raw.github.com/collective/collective.twitter.widget.portlets/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.54.58%20AM.png

Saved:

.. image:: https://raw.github.com/collective/collective.twitter.widget.portlets/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.55.14%20AM.png

Get widget id:

.. image:: https://raw.github.com/collective/collective.twitter.widget.portlets/master/docs/_img/Screen%20Shot%202012-11-09%20at%209.55.14%20AM-Get_id.png


Credits
-------

Development
___________

* Main developper: `Thiago Avelino <https://github.com/avelino>`_
* Sponsor: `tv1.com <http://www.grupotv1.com.br/pt-br/tv1-com/>`_


Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/avelino/collective.twitter.widget.portlets.png
    :target: http://travis-ci.org/avelino/collective.twitter.widget.portlets