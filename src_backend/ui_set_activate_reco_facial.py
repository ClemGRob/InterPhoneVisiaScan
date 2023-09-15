import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.manager_reco_facial import set_manager_reco_facial

def manager_reco_facial(self, eventData, db_backend, storage_backend, LIST_HABITANT_BACKEND):
    logging.info("Lancement du programme de reconnaissance faciale")
    logging.debug(eventData)
    set_manager_reco_facial(self, eventData, db_backend, storage_backend, LIST_HABITANT_BACKEND)