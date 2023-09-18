import os
import sys
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def set_Clear_number(self,msg) :
    if msg == EVENT_NUMERIC_KEYPAD_VALIDATION:
        msg = "Waiting code PIN" 
    else:
        msg = "Waiting RIGHT code PIN"

    logging.info("Clear")
    logging.debug("Début d'effacement de la liste de valeurs")
    self.transmit_textonQML(msg, "pyLbNum_Keypad")
    self.stored_values = []
    logging.debug("fin d'éffacement de la liste de valeurs")