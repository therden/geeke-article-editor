import anvil.server
from anvil.tables import app_tables
import anvil.tables.query as q

@anvil.server.callable
def update_article(row,data):
    row.update(**data)

@anvil.server.callable
def add_article(data):
    app_tables.articles.add_row(**data)