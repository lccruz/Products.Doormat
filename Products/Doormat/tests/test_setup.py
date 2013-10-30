# -*- coding: utf-8 -*-
from Products.Doormat.testing import PRODUCTS_DOORMAT_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID, setRoles

import unittest2 as unittest


class ProductsDoormatSetupTest(unittest.TestCase):

    layer = PRODUCTS_DOORMAT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.types = self.portal.portal_types

    def test_contenttypes_installed(self):
        self.assertTrue('Doormat' in self.types.objectIds())
        self.assertTrue('DoormatColumn' in self.types.objectIds())
        self.assertTrue('DoormatSection' in self.types.objectIds())
        self.assertTrue('DoormatReference' in self.types.objectIds())
        self.assertTrue('DoormatCollection' in self.types.objectIds())
        self.assertTrue('DoormatMixin' in self.types.objectIds())

    def test_browserlayer_available(self):
        from plone.browserlayer import utils
        from Products.Doormat.browser.interfaces import IDoormatLayer
        self.assertTrue(
            IDoormatLayer in utils.registered_layers()
        )

    def test_css_registered(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertTrue(
            '++resource++Products.Doormat.stylesheets/doormat.css' in
            stylesheets_ids)

    def test_default_content_created(self):
        self.assertTrue('doormat' in self.portal.objectIds())

    def test_default_contents_brain(self):
        from Products.Doormat.setuphandlers import DEFAULT_DOORMAT_DOCUMENT_HTML_LINK
        from Products.Doormat.setuphandlers import DEFAULT_DOORMAT_DOCUMENT_TITLE
        #test for title and exclude from nav Doormat
        brain = self.portal.portal_catalog.searchResults(
            {'portal_type': 'Doormat'})[0]
        self.assertEqual(brain.Title, 'Doormat')
        self.assertTrue(brain.exclude_from_nav)
        #test for contents title
        brains = self.portal.portal_catalog.searchResults(
            {'portal_type': ['Doormat','DoormatColumn','DoormatSection']})
        titles = [brain.Title for brain in brains]
        self.assertItemsEqual(titles, ['Doormat', 'Column 1', 'Section 1'])
        #test document
        brain = self.portal.portal_catalog.searchResults(
            {'portal_type': 'DoormatSection'})[0]
        brain = self.portal.portal_catalog.searchResults(
            path={"query": brain.getPath(),'depth': 1})[0]
        self.assertEqual(brain.Title, DEFAULT_DOORMAT_DOCUMENT_TITLE)
        self.assertEqual(brain.getPath().replace('/%s' % (self.portal.getId()),''), DEFAULT_DOORMAT_DOCUMENT_HTML_LINK)




def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
