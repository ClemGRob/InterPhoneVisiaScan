from pyfcm import FCMNotification
import pyrebase
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import pyrebase_val.config as config
import pyrebase_val.src as serveraction

def set_manager_search_call(db, storage, call_receiver):
    print("Lancement du programme d'appel")
    firebase = pyrebase.initialize_app(config.pirebaseConfig)
    
    tokken = serveraction.get_data(db,"token")

    DEVICE_TOKEN = tokken[call_receiver]

    message_title = "demande d'entree"
    message_body = "demande d'entree"
    data_message = {
    }
    
    serveraction.send_message(config.API_KEY, DEVICE_TOKEN,message_title,message_body,data_message)


    # TODO
    # ####################################
    # # Take picture
    # ####################################




    img = "img.txt"


    auth=firebase.auth()

    user=serveraction.login(auth, "password@password.password","password")

    serveraction.upload(storage,img,call_receiver+img,user, "call",call_receiver)


    # TODO
    # ####################
    # delet picture
    # ####################






    label_name = "pyLbSerach_Hab"
    # Va chercher le nom suivant = msg
    #msg_name = update_name_display(self)
    #msg_name_hab = msg_name[0]
    #msg_number_app = msg_name[1]
    #text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
    #self.transmit_textonQML(text_to_send, label_name)