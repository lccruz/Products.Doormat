# -*- coding: utf-8 -*-
#
# File: DoormatSection.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.Doormat.content.DoormatMixin import DoormatMixin

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.Doormat.config import *

schema = Schema((


),
)

DoormatSection_schema = ATFolderSchema.copy() + \
    getattr(DoormatMixin, 'schema', Schema(())).copy() + \
    schema.copy()


class DoormatSection(ATFolder, DoormatMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDoormatSection)

    meta_type = 'DoormatSection'
    _at_rename_after_creation = True

    schema = DoormatSection_schema

    # Methods


registerType(DoormatSection, PROJECTNAME)
# end of class DoormatSection
