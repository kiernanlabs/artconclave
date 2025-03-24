from ._anvil_designer import EvalFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class EvalForm(EvalFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    artist = self.artist_box.text    
    file = self.file_input.file
    anvil.server.call('store_artwork',file,artist)