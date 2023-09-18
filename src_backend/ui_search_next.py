import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.manager_search_next import set_manager_search_next

def manager_search_next(self):
    logging.info("Lancement du programme de recherche suivante")
    set_manager_search_next(self)