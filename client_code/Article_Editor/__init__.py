from ._anvil_designer import Article_EditorTemplate
from anvil import *
from anvil.js import window
from ..Article_Viewer import Article_Viewer
from datetime import date
import anvil.server

class Article_Editor(Article_EditorTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.item=properties.get('item')
        if self.item:
            self.title.text=self.item['title']
            self.subtitle.text=self.item['subtitle']
            self.category.text=self.item['category']
            self.bg.text=self.item['bg']
            self.action.text='Update Article'

    def generate_data(self):
        return {
            "title":self.title.text,
            "subtitle":self.subtitle.text,
            "category":self.category.text,
            "bg":self.bg.text,
            "cont":window.simplemde.value(),
            # "cont":window.easymde.value(),
            "date":date.today()
        }
        
    def preview_click(self, **event_args):
        alert(Article_Viewer(item=self.generate_data()),large=True,buttons=None,title='Preview')

    def form_show(self, **event_args):
        if self.item:
            window.simplemde.value(self.item['cont'])
            # window.easymde.value(self.item['cont'])

    def action_click(self, **event_args):
        if confirm("Will you like to publish/update this article",title='Confirmation'):
            if self.item:
                anvil.server.call('update_article',self.item,self.generate_data())
            else:
                anvil.server.call('add_article',self.generate_data())
            open_form('Home')
            
    def button_1_click(self, **event_args):
        open_form('Home')

    def button_2_click(self, **event_args):
        from .Instructions import Instructions
        alert(Instructions(),title='Instructions')
