import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def Manager_numeric_Keypad(self, eventData):
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
        self.stored_values.append(eventData)
        # Envoye de la valeur "*" au "pyLbNum_Keypad"
        num_stars = len(self.stored_values)
        stars_text = "*" * num_stars
        self.transmit_textonQML(stars_text, "pyLbNum_Keypad")

    elif eventData == EVENT_NUMERIC_KEYPAD_VALIDATION:
        
        if self.stored_values == EXPECTED_SEQUENCE:
            logging.info("Séquence correcte")
            self.transmit_textonQML("The door is open", "pyLbNum_Keypad")
        
            self.transmit_textonQML("Waiting code PIN", "pyLbNum_Keypad")

        else:
            logging.info("Séquence incorrecte")
            self.transmit_textonQML("Waiting right code PIN", "pyLbNum_Keypad")
        self.stored_values = []

    elif eventData == EVENT_NUMERIC_KEYPAD_CLEAR:
        logging.info("Effacement de la liste de valeurs")
        self.transmit_textonQML("Waiting right code PIN", "pyLbNum_Keypad")
        self.stored_values = []

    else : 
         logging.debug("Enter else : Manager_numeric_Keypad :" + eventData)