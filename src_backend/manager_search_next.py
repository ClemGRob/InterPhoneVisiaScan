import logging

from .constants_ui import *

def set_manager_search_next(self):
    logging.info("Lancement du programme de recherche suivant")
    label_name = "pyLbSerach_Hab"
    
    #msg_name_hab = "suivantname"
    #msg_number_app = "suivantappartement"

    #text_to_send = f" Contacte : {msg_name_hab} \nNum appartement :\n{msg_number_app} "
    #self.transmit_textonQML(text_to_send, label_name)

    if self.Selected_Hab < len(self.Habitant):
        self.Selected_Hab +=1
    text_to_send = str(self.Habitant[self.Selected_Hab])
    self.transmit_textonQML(text_to_send, label_name)