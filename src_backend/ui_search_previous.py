import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.manager_search_previous import set_manager_search_previous

def manager_search_previous(self):
    logging.debug("Lancement du programme de recherche précédente")
    set_manager_search_previous(self)