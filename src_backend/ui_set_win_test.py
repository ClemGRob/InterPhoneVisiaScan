
import os
import sys
import subprocess
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *


def Open_Win_Test(self):
    # Exécutez le script avec l'environnement Python actuel
    logging.debug(f"Chemin complet : {TEST_WINDOW_QT}")
    try :   
        process = subprocess.Popen(["python", TEST_WINDOW_QT])
        process.wait()
        
        if process.poll() is not None:
            logging.info("Fermeture de la fenetre Test")

    except Exception as e:
        logging.error(f"Une erreur s'est produite dans la fenetre Test : {e}")
    
def managerActivateTest(self, eventData):
    if "Open_Test" in eventData:
        logging.debug("Receipt of: " + eventData)
        logging.info("Lancement d'ouverture de la fenetre Test")
        Open_Win_Test(self)  # Utilisez la méthode pour gérer l'ouverture/fermeture
 
    else:
        logging.debug("Enter else : managerActivateTest :" + eventData)

