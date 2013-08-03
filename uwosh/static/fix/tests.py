import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five.testbrowser import Browser
from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import uwosh.static.fix

ptc.setupPloneSite(products=['uwosh.static.fix'])


class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             uwosh.static.fix)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass

    def afterSetUp(self):
        super(TestCase, self).afterSetUp()

        self.browser = Browser()

        self.uf = self.portal.acl_users
        self.uf.userFolderAddUser('root', 'secret', ['Manager'], [])

    def loginAsManager(self, user='root', pwd='secret'):
        """points the browser to the login screen and logs in as user root with Manager role."""
        self.browser.open('http://nohost/plone/')
        self.browser.getLink('Log in').click()
        self.browser.getControl('Login Name').value = user
        self.browser.getControl('Password').value = pwd
        self.browser.getControl('Log in').click()


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='uwosh.static.fix',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='uwosh.static.fix.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='uwosh.static.fix',
        #    test_class=TestCase),

        ztc.FunctionalDocFileSuite(
           'browser.txt', package='uwosh.static.fix',
           test_class=TestCase),
        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
