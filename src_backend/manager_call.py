import logging
from pyfcm import FCMNotification
import pyrebase
import sys
import os
from src_backend.manager_search_refresh_name import update_name_display
from src_backend.ui_set_open_door import set_ui_msg_open_door

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import pyrebase_val.config as config
import pyrebase_val.src as serveraction
import time

Label_name_reco = "pyLbSerach_Hab"

def set_manager_search_call(self, db_backend, storage_backend, LIST_HABITANT_BACKEND):
    logging.info("Lancement du programme d'appel")
    firebase = pyrebase.initialize_app(config.pirebaseConfig)
    
    tokken = serveraction.get_data(db_backend,"token")
    
    text_retour = self.backend.receive_textonPYTHON(Label_name_reco)
    logging.debug("Texte reçu sur Python:", text_retour)
    call_receiver = text_retour

    if call_receiver not in [*tokken]:
        return "none"
    
    logging.debug(call_receiver)
    DEVICE_TOKEN = tokken[call_receiver]

    message_title = "demande d'entree"
    message_body = "demande d'entree"
    data_message = {
    }
    
    logging.debug(data_message)
    serveraction.send_message(config.API_KEY, DEVICE_TOKEN,message_title,message_body,data_message)


    # TODO
    logging.info("Take capture")
    # ####################################
    # # Take picture
    # ####################################




    img = "img.txt"

    logging.debug("Authentification")
    auth=firebase.auth()

    logging.debug("Login")
    user=serveraction.login(auth, "password@password.password","password")

    logging.debug("Upload")
    serveraction.upload(storage,img,call_receiver+img,user, "call",call_receiver)



    # TODO
    logging.info("Delete picture")
    # ####################
    # delet picture
    # ####################







    # TODO
    logging.info("Check access door")
    # ####################
    # verification acces porte
    # ####################
    door_open = False
    for _ in range(20):
        if serveraction.get_data(db,"door_open") is "True":
            door_open = True
            break
        time.sleep(1)
    if door_open is True:
        # message porte ouverte
        logging.debug("Door open")
        set_ui_msg_open_door(self, Label_name_reco )
    else:
        # message porte fermée
        for X in range(3) :
            msg_relance = "Remainder : {X} Try "
            logging.info("Door NOT open, {msg_relance}")
            if X == 3:
                msg_relance = "please try a others choice option"
                logging.info("Door NOT open, {msg_relance}")
                text_to_send = f" {msg_relance} "
                self.transmit_textonQML(msg_relance)
        







    
    msg_name = update_name_display()
    msg_name_hab = msg_name[0]
    msg_number_app = msg_name[1]
    text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
    self.transmit_textonQML(text_to_send, label_name)