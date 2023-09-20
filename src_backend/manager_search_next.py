import logging

from .constants_ui import *

def set_manager_search_next(self):
    logging.info("Lancement du programme de recherche suivant")
    label_name = "pyLbSerach_Hab"

    if self.Selected_Hab < len(self.Habitant):
        self.Selected_Hab +=1
    text_to_send = str(self.Habitant[self.Selected_Hab])
    self.transmit_textonQML(text_to_send, label_name)
