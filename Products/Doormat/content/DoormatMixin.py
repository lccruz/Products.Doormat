# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Doormat.config import *

schema = Schema((

    BooleanField(
        name='showTitle',
        default="True",
        widget=BooleanField._properties['widget'](
            label="Show title in viewlet",
            description="If checked, this Doormat / Column / Section's title will be displayed in the doormat viewlet.",
            label_msgid='Doormat_label_showTitle',
            description_msgid='Doormat_help_showTitle',
            i18n_domain='Doormat',
        ),
    ),

),
)

DoormatMixin_schema = BaseSchema.copy() + \
    schema.copy()


class DoormatMixin(BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDoormatMixin)

    meta_type = 'DoormatMixin'
    _at_rename_after_creation = True

    schema = DoormatMixin_schema
