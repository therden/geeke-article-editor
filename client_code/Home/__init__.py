from ._anvil_designer import HomeTemplate
from anvil import *
from anvil.tables import app_tables

class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def form_show(self, **event_args):
        self.repeating_panel_1.items=app_tables.articles.search()

    def button_1_click(self, **event_args):
        open_form('Article_Editor')