import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.manager_search_refresh_name import set_manager_refresh_name

def manager_refresh_name():
    logging.info("Lancement du programme de rafraichissement des noms")
    set_manager_refresh_name()
