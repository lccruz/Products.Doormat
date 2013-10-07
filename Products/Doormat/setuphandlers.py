# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

import logging

logger = logging.getLogger('Doormat: setuphandlers')


def isNotDoormatProfile(context):
    return context.readDataFile("Doormat_marker.txt") is None


def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotDoormatProfile(context):
        return
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    #if isNotDoormatProfile(context):
    #    return
    pass
