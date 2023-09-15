import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.manager_call import set_manager_search_call

def manager_search_call(self, db, storage, call_receiver):
    logging.info("Lancement du programme d'appel à l'habitant")
    set_manager_search_call(self, db, storage, call_receiver)