import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import Media
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def store_artwork(file):
    """
    Store an uploaded artwork file in the artwork data table.
    
    Args:
        file: The uploaded file (Media object)
    
    Returns:
        The created artwork row from the data table
    """
    # Create a new row in the artwork table
    artwork_row = app_tables.artwork.add_row(
        file=file,
        date_uploaded=datetime.now(),
        status="pending"  # Initial status
    )
    
    return artwork_row

# Example usage:
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
