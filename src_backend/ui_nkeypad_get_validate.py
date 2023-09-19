import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

from src_backend.ui_nkeypad_set_verify_entry import set_number_sequency
from src_backend.ui_nkeypad_get_clear import set_Clear_number

def get_Validation_number (self):
    logging.info("Validation")
    if self.stored_values == EXPECTED_SEQUENCE:
        set_number_sequency(self)

    elif self.stored_values == EXPECTED_SEQUENCE_ADMIN:
        msg = "Code bon"
        logging.debug(f"Admin visible avec {msg}")
        self.transmit_textonQML(msg, "pyLcurrentLabelvisible")
       
    else:
        msg = "Séquence incorrecte"
        logging.debug(msg)
        self.transmit_textonQML(msg, "pyLcurrentLabelvisible")
        set_Clear_number(self, "")

    