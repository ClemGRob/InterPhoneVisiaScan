import os
import sys
import time
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.ui_nkeypad_get_clear import set_Clear_number

def managerBlockAccessAdmin(self, eventData):
    logging.info("In Manager search habitant")
    if EVENT_BLOCK_ACCESS_ADMIN in eventData:
        logging.debug("passez " + eventData)

        Label_name = "pyLcurrentLabelvisible"
        msg = ""
        logging.debug(f"Transmission du blocage de l'accès admin : {msg}")
        self.transmit_textonQML(msg, Label_name)

        time.sleep(2.5)
        
        set_Clear_number(self, "V")

    else:
        logging.error("Enter else : manger_search_habitant :" + eventData)