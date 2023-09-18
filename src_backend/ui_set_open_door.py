import os
import sys
import time
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.ui_nkeypad_get_clear import set_Clear_number

def set_ui_msg_open_door(self):
    Label_name = "pyLbNum_Keypad"
    TextValidationOuverture = EVENT_NUMERIC_KEYPAD_VALIDATION

    msg = "The door is open"
    msg_2 = "Waiting code PIN"

    logging.debug(f"Première transmission : {msg}")
    set_Clear_number(self, TextValidationOuverture)

    time.sleep(0.5) # TODO ne prend pas en compte le premier message

    self.transmit_textonQML(msg, Label_name)

    time.sleep(2)

    logging.debug(f"Seconde transmission : {msg_2}")
    self.transmit_textonQML(msg_2, Label_name)