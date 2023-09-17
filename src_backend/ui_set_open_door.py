import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

from src_backend.ui_nkeypad_get_clear import set_Clear_number

def set_ui_msg_open_door(self):
    TextValidationOuverture = EVENT_NUMERIC_KEYPAD_VALIDATION

    msg = "The door is open"

    logging.debug("Première transmission : {msg}")
    self.transmit_textonQML(msg, "pyLbNum_Keypad")

    set_Clear_number(self, TextValidationOuverture)

    # TODO 
    # voir pour mettre un délai via la comunication de l'ui
    # py(msg_1) -> QML -> py -> qml(msg_2)

    msg_2 = "Waiting code PIN"
    logging.debug("Seconde transmission : {msg_2}")
    self.transmit_textonQML(msg_2, "pyLbNum_Keypad")