import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.ui_nkeypad_get_number import set_saisie_text_qml
from src_backend.ui_nkeypad_get_validate import get_Validation_number
from src_backend.ui_nkeypad_get_clear import set_Clear_number

def Manager_numeric_Keypad(self, eventData):
    logging.info("In manager_numeric")
    if eventData in (   EVENT_NUMERIC_KEYPAD_0,
                        EVENT_NUMERIC_KEYPAD_1,
                        EVENT_NUMERIC_KEYPAD_2,
                        EVENT_NUMERIC_KEYPAD_3,
                        EVENT_NUMERIC_KEYPAD_4,
                        EVENT_NUMERIC_KEYPAD_5,
                        EVENT_NUMERIC_KEYPAD_6,
                        EVENT_NUMERIC_KEYPAD_7,
                        EVENT_NUMERIC_KEYPAD_8,
                        EVENT_NUMERIC_KEYPAD_9,
                        EVENT_NUMERIC_KEYPAD_ETOILE,
                        EVENT_NUMERIC_KEYPAD_DIEZ):
        set_saisie_text_qml(self, eventData)

    elif eventData == EVENT_NUMERIC_KEYPAD_VALIDATION:
        get_Validation_number(self)

    elif eventData == EVENT_NUMERIC_KEYPAD_CLEAR:
        set_Clear_number(self, eventData)

    else : 
         logging.debug("Enter else : Manager_numeric_Keypad :" + eventData)