import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

from src_backend.manager_search_next import set_manager_search_next
from src_backend.manager_search_previous import set_manager_search_previous
from src_backend.manager_call import set_manager_search_call

def manger_search_habitant(self, eventData):
    logging.info("In Manager search habitant")
    if EVENT_SEARCH_THE_PERSON_NEXT in eventData:
        logging.debug("passez " + eventData)
        set_manager_search_next(self)

    elif EVENT_SEARCH_THE_PERSON_PREVIOUS in eventData:
        logging.debug("passez " + eventData)
        set_manager_search_previous(self)

    elif EVENT_CALL_THE_PERSON in eventData:
        logging.debug("passez " + eventData)
        set_manager_search_call(self)

    else:
        logging.error("Enter else : manger_search_habitant :" + eventData)