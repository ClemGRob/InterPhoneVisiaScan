
import os
import sys
import subprocess
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *


def Open_Win_Admin(self):
    try:
        # Exécutez le script avec l'environnement Python actuel
        logging.debug(f"Chemin complet : {ADMIN_WINDOW_QT}")
        subprocess.Popen(["python", ADMIN_WINDOW_QT])
    except Exception as e:
        logging.error(f"Une erreur s'est produite : {e}")
    
def managerActivateAdmin(self, eventData):
    if "Open_Admin" in eventData:
            logging.debug("Receipt of: " + eventData)
            logging.info("Lancement d'ouverture de la fenetre Admin")
            Open_Win_Admin(self)
    else : 
        logging.debug("Enter else : managerActivateAdmin :" + eventData)