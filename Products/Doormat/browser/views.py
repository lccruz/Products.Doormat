from plone.memoize.instance import memoize

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

class DoormatView(BrowserView):
    """
    """

    def getDoormatTitle(self):
        """
        """
        return self.context.Title()
         
    def getDoormatData(self):
        """ Return a dictionary like this:
        data = [
            {   'col_title: 'Column One',
                'col_cats: [
                {   'cat_title': 'De Oosterpoort',
                    'cat_links': [
                        {   'link_title': 'Adres OP',
                            'link_url': 'link.naar.adres',
                            },
                        ]
                    },
                ]
            },
        ]
        """
        dm = self.context
        data = []
        # Fetch Columns
        for col_brain in dm.getFolderContents():
            col_dict = {'col_title': col_brain.Title}
            col_cats = []
            cat_brains = col_brain.getObject().getFolderContents()

            # Fetch Categories from Column
            for cat_brain in cat_brains:
                cat_dict = {'cat_title': cat_brain.Title}
                cat_links = []
                link_brains = cat_brain.getObject().getFolderContents()

                # Loop over all link object in category
                for link_brain in link_brains:
                    # Use the link item's title, not that of the linked content
                    title = link_brain.Title
                    item = link_brain.getObject()
                    item_type = item.meta_type
                    if item_type == 'DoormatReference':
                        linked_item = item.getInternal_link()
                        if not linked_item:
                            continue
                        url = linked_item.absolute_url()
                    else:
                        # Link is an Archetypes link
                        url = link_brain.getRemoteUrl
                        if not url:
                            continue
                    link_dict = {'link_url': url, 'link_title': title}
                    cat_links.append(link_dict)
                cat_dict['cat_links'] = cat_links
                col_cats.append(cat_dict)
            col_dict['col_cats'] = col_cats
            data.append(col_dict)
        return data



##code-section module-footer #fill in your manual code here
##/code-section module-footer


