# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.twiiter.widget')


# See http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)


