import os
import sys
import subprocess
import logging
import tempfile

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def Open_Win_popup_msg(text_to_send):
    # Exécutez le script avec l'environnement Python actuel
    logging.debug(f"Chemin complet : {POPUP_MSG_WINDOW}")
    logging.info(f'Open Popup_msg')

    try :
        process = subprocess.Popen(
            [
                "python",
                POPUP_MSG_WINDOW
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        process.stdin.write(text_to_send)
        process.stdin.close()  

        process.wait()
        
        if process.poll() is not None:
            logging.info("Fermeture de la fenetre Popup_msg")

    except Exception as e:
        logging.error(f"Une erreur s'est produite dans la fenetre Popup_msg : {e}")


def Open_Win_popup_question():
    # Exécutez le script avec l'environnement Python actuel
    logging.debug(f"Chemin complet : {POPUP_QUESTION_WINDOW}")
    
    logging.info(f'Open Popup_question')
    logging.debug("Ouverture de la fenêtre Popup_question")

    try:
        # Créer un fichier temporaire pour stocker la réponse
        with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp_file:
            result_file_path = temp_file.name

        process = subprocess.Popen(
            [
                "python",
                POPUP_QUESTION_WINDOW,
                result_file_path,  # Passer le chemin du fichier temporaire
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        process.communicate()
        logging.info("Fermeture de la fenêtre Popup_question")

        # Lire la réponse du fichier temporaire
        with open(result_file_path, 'r') as result_file:
            response = result_file.read()
        logging.debug(f"Lecture de la réponse du fichier : {response}")
        return response

    except Exception as e:
        logging.error(f"Une erreur s'est produite dans la fenetre Popup_question : {e}")
        return None



