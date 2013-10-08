# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

import logging

logger = logging.getLogger('Doormat: setuphandlers')


def isNotDoormatProfile(context):
    return context.readDataFile("Doormat_marker.txt") is None
