from anvil import set_url_hash
from anvil.tables import app_tables,query
from anvil.js import get_dom_node
from anvil.js.window import jQuery,document
from anvil import *

fetch_parameters=query.fetch_only('title','subtitle','category','bg')
articles_cache={}
current_form=None

def scroll_into_view(comp,pos='start'):
    get_dom_node(comp).scrollIntoView({"behavior":"smooth","block":pos})
    