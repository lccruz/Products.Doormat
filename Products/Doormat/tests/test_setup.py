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


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
