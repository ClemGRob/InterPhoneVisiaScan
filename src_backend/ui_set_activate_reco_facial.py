import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.manager_reco_facial import set_manager_reco_facial

def manager_reco_facial(self, eventData):
    logging.info("Lancement du programme de reconnaissance faciale")
    set_manager_reco_facial()