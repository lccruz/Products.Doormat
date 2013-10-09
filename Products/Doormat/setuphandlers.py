# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('Doormat: setuphandlers')


def createDefaultContent(portal):
    portal.invokeFactory('Doormat', 'doormat')
    doormat = portal.doormat
    doormat.setTitle('Doormat')
    doormat.setExcludeFromNav(True)
    doormat.reindexObject()


def isNotDoormatProfile(context):
    return context.readDataFile("Doormat_marker.txt") is None


def setupVarious(context):
    if isNotDoormatProfile(context):
        return
    portal = context.getSite()
    createDefaultContent(portal)
