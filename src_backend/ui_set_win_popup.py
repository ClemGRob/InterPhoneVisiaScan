import os
import sys
import subprocess
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def Open_Win_popup_msg(text_to_send):
    # Exécutez le script avec l'environnement Python actuel
    logging.debug(f"Chemin complet : {POPUP_MSG_WINDOW}")
    logging.info(f'Open Popup_msg')

    try :
        process = subprocess.Popen(["python", POPUP_MSG_WINDOW], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        process.stdin.write(text_to_send)
        process.stdin.close()  

        process.wait()
        
        if process.poll() is not None:
            logging.info("Fermeture de la fenetre Popup_msg")

    except Exception as e:
        logging.error(f"Une erreur s'est produite dans la fenetre Popup_msg : {e}")





