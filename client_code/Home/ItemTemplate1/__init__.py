from ._anvil_designer import ItemTemplate1Template
from anvil import *
from ...Article_Viewer import Article_Viewer

class ItemTemplate1(ItemTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.title.text=self.item['title']

    def view_click(self, **event_args):
        alert(Article_Viewer(item=self.item),buttons=None,title='Preview',large=True)

    def edit_click(self, **event_args):
        open_form('Article_Editor',item=self.item)