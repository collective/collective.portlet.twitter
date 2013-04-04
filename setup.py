# -*- coding:utf-8 -*-

import os
from setuptools import setup, find_packages

version = '0.2.dev.0'
description = u"Twitter Widget Portlet - https://twitter.com/settings/widgets"
long_description = open("README.rst").read() + "\n" + \
                   open(os.path.join("docs", "INSTALL.rst")).read() + "\n" + \
                   open(os.path.join("docs", "CREDITS.rst")).read() + "\n" + \
                   open(os.path.join("docs", "HISTORY.rst")).read()

setup(name='collective.twitter.widget',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone portlet twitter widget',
      author='Thiago Avelino',
      author_email='thiagoavelinoster@gmail.com',
      url='https://github.com/collective/collective.twitter.widget',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.twitter'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.app.portlets',
          'plone.portlets',
          'Products.CMFCore',
          'Products.GenericSetup',
          'setuptools',
          'zope.formlib',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'unittest2',
              'zope.component',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
