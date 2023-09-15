import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def write_messages_to_file(word, file_path):
    logging.info(f"It not managed : {file_path}")

    if not os.path.exists(INFO_BUTTON_NOT_MANAGED_FILE):
        # Si le fichier n'existe pas, le créer
        with open(INFO_BUTTON_NOT_MANAGED_FILE, 'w') as file:
            logging.debug("Ce fichier a été créé car il n'existait pas auparavant.")

        logging.debug(f"Le fichier '{INFO_BUTTON_NOT_MANAGED_FILE}' a été créé.")

    else:
        logging.debug(f"Le fichier '{INFO_BUTTON_NOT_MANAGED_FILE}' existe déjà.")

    if word and len(word.strip()) > 0:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if word + "\n" not in lines:
                with open(file_path, "a") as append_file:
                    append_file.write(word + "\n")