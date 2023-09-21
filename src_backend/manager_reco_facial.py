# import json
# sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
# from facereco import FaceRecognitionWithIndication
# from Open_Win_Admin import *

# face_recognition = FaceRecognitionWithIndication.FaceRecognition()


import logging
from src_backend.ui_set_open_door import set_ui_msg_open_door
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import facereco
label_name = "reconnaissancefaciale"
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton



def set_manager_reco_facial(self, eventData):
    logging.info(f"Lancement du programme de {eventData}")
    print(eventData)
    if eventData == "Reconnaissance_IA":
        logging.debug("personne reconnue")
        if self.face_recognition.recognize_faces_new("photo", 20) == True:       
            set_ui_msg_open_door(self,label_name)

    else:
       print(("out the function"))
       logging.debug("personne non connue")
    text_to_send = "Lunching"
    self.transmit_textonQML(text_to_send, label_name)
    