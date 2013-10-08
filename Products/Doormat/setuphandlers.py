# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('Doormat: setuphandlers')


def isNotDoormatProfile(context):
    return context.readDataFile("Doormat_marker.txt") is None
