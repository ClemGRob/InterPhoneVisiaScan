import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_log import *

def call_exception(e):
 # Condition pour la gestion spécifique d'une exception
        if isinstance(e, KeyboardInterrupt):
            logging.info("Application terminated by user")
        else:
            call_exception_msg(e)

def call_exception_msg(e):
    error_message = f"An error occurred: {str(e)}"
    logging.error(error_message)
    log_error(error_message)

def log_error(message):
    """
    Enregistrer le message d'erreur dans le fichier Error.trace.
    
    Args:
        message (str): Le message d'erreur à enregistrer.
    """
    with open(ERROR_TRACE_FILE_PATH, 'a') as error_file:
        error_file.write(message + '\n')