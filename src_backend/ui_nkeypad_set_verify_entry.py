import os
import sys
import time
import logging

from src_backend.ui_set_open_door import set_ui_msg_open_door

def set_number_sequency(self):
    
    logging.info("Sequency number")
    set_ui_msg_open_door(self)