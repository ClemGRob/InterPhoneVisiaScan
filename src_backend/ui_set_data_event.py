import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

from src_backend.ui_set_search import manger_search_habitant
from src_backend.ui_set_swipview import managerchangeswipeView
from src_backend.ui_set_win_admin import managerActivateAdmin
from src_backend.ui_set_activate_reco_facial import manager_reco_facial
from src_backend.ui_set_numeric_Keypad import Manager_numeric_Keypad
from src_backend.ui_set_write_not_managed import write_messages_to_file



def manager_data(self, eventData, db_backend, storage_backend, LIST_HABITANT_BACKEND):
    logging.info(eventData)
    # Utilisation d'un switch case pour gérer les différents cas
    switch_UI = {
        EVENT_NUMERIC_KEYPAD_0:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_1:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_2:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_3:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_4:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_0:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_5:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_6:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_7:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_8:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_9:             Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_ETOILE:        Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_DIEZ:          Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_VALIDATION:    Manager_numeric_Keypad,
        EVENT_NUMERIC_KEYPAD_CLEAR:         Manager_numeric_Keypad,
        EVENT_PREVIOUS_BUTTON_CLICKED:      managerchangeswipeView,
        EVENT_NEXT_BUTTON_CLICKED:          managerchangeswipeView,
        #"Select_interface Menu":
        #"Select_interface Display Numeric keypad":
        #"Select_interface Display Search Hab":
        #"Select_interface Display Admin":
    }

    switch_backend = {
            EVENT_RECOGNITION_IA:               manager_reco_facial,
            EVENT_CALL_THE_PERSON:              manger_search_habitant,
            EVENT_SEARCH_THE_PERSON_PREVIOUS:   manger_search_habitant,
            EVENT_SEARCH_THE_PERSON_NEXT:       manger_search_habitant,
            EVENT_OPEN_ADMIN:                   managerActivateAdmin,
        }


    # Vérifier si l'événement est présent dans le switch
    if eventData in switch_UI:
        # Appeler la fonction associée à l'événement
        switch_UI[eventData](self, eventData)
        
    elif eventData in switch_backend:
        # Appeler la fonction associée à l'événement
        switch_backend[eventData](self, eventData, db_backend, storage_backend, LIST_HABITANT_BACKEND)
    else:
        logging.debug("Not pass : " + eventData)
        write_messages_to_file(eventData, INFO_BUTTON_NOT_MANAGED_FILE)