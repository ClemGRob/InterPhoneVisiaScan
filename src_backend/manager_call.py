#import cv2
import logging

from pyfcm import FCMNotification
import pyrebase
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import pyrebase_val.config as config
import pyrebase_val.src as serveraction
import time

from src_backend.ui_set_win_popup import Open_Win_popup_msg, Open_Win_popup_question

label_name = "pyLbSerach_Hab"



def web_cam_photo(name:str):
 #   cap = cv2.VideoCapture(0)
 #   id_photo=0
 #   ret, frame = cap.read()
 #   cv2.imshow('frame',frame)
  #      #if cv2.waitKey(1) & 0xFF == ord('q'):
  #  cv2.imwrite(name+".png", frame)
        
    pass
  #  cap.release()
 #   cv2.destroyAllWindows()



def init_popup(self):
    msg_retour = Open_Win_popup_question()
    logging.info(f"messag retour popup{msg_retour}")
    if msg_retour != "oui":
        return "unavailable"



def init_call(self):
    # self.Habitant[self.Selected_Hab]
    logging.info("Lancement du programme d'appel")
    firebase = pyrebase.initialize_app(config.pirebaseConfig)
    
    token = serveraction.get_data(self.db,"token")
    return token, firebase



def verif_habitant(self,token):
    # TODO
    #msg = "test"
    #Open_Win_popup_msg(msg)
    # Dans le cas où l'habitant et non joignable, l'indiquer à l'individu et sortir de la fonctionnalité
    if self.Habitant[self.Selected_Hab] not in [*token]:
        msg =  f'Unavailable Habitant : {self.Habitant[self.Selected_Hab]}'
        logging.debug(msg)
        Open_Win_popup_msg(msg)
        return "unavailable"



def envoi_msg(self, token):
    logging.debug(self.Habitant[self.Selected_Hab])
    DEVICE_TOKEN = token[self.Habitant[self.Selected_Hab]]

    message_title = "demande d'entree"
    message_body = "demande d'entree"
    data_message = {
    }
    
    logging.debug(data_message)
    serveraction.send_message(config.API_KEY, DEVICE_TOKEN,message_title,message_body,data_message)



def take_picture(self,firebase):
    # TODO
    logging.info("Take capture")
    # ####################################
    # # Take picture
    # ####################################
    web_cam_photo(self.Habitant[self.Selected_Hab])


    img = "img.txt"

    logging.debug("Authentification")
    auth=firebase.auth()

    logging.debug("Login")
    user=serveraction.login(auth, "password@password.password","password")

    logging.debug("Upload")
    serveraction.upload(self.storage,self.Habitant[self.Selected_Hab]+".png",self.Habitant[self.Selected_Hab]+".png",user, "call",self.Habitant[self.Selected_Hab])



def delete_picture(self):
    # TODO
    logging.info("Delete picture")
    # ####################
    # delet picture
    # ####################
    file_to_delete = self.Habitant[self.Selected_Hab]+".png"

    try:
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
        else:
            msg =  f'Picture not found : {file_to_delete}'
            logging.debug(msg)
            return "unavailable"
    except Exception as msg:
        logging.debug(f"manager_call ligne 95{msg}")
        Open_Win_popup_msg(msg)



def verif_access_door(self):
    # TODO
    logging.info("Check access door")
    data = {"door_open":"False"}
    serveraction.set_data(self.db,data,"door")

    # ####################
    # verification acces porte
    # ####################
    door_open = False
    for _ in range(20):
        if serveraction.get_data(self.db,"door") =={ "door_open":"True"}:
            door_open = True
            break
        time.sleep(1)

    if door_open is True:
        # message porte ouverte
        logging.debug("Door open")
        pass
    else:
        # message porte fermée
        # TODO
        # for X in range(3) :
        #    msg_relance = "Remainder : {X} Try "
        #    logging.info("Door NOT open, {msg_relance}")
        #    if X == 3:
        #        msg_relance = "please try a others choice option"
        #        logging.info("Door NOT open, {msg_relance}")
        #        text_to_send = f" {msg_relance} "
        #        self.transmit_textonQML(msg_relance)
        pass


def replacement(self):
    serveraction.remove(self.storage,self.Habitant[self.Selected_Hab]+".png", "call",self.Habitant[self.Selected_Hab])


def sequency_call(self):
    init_popup(self)
    s_token, s_firebase = init_call(self)
    verif_habitant(self, s_token)
    envoi_msg(self, s_token)
    take_picture(self, s_firebase)
    delete_picture(self)
    verif_access_door(self)
    replacement(self)


def set_manager_search_call(self):
    try : 
        sequency_call(self)
    except Exception as e:
        logging.error(f"Une erreur s'est produite : {str(e)}")
