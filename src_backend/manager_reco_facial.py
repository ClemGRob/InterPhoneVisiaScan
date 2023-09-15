#import json
#sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
#from facereco import FaceRecognitionWithIndication
#from Open_Win_Admin import *

#face_recognition = FaceRecognitionWithIndication.FaceRecognition()


import logging
from src_backend.ui_set_open_door import set_ui_msg_open_door

label_name = "lbcustomrecofacial"

def set_manager_reco_facial(self, eventData):
    logging.info("Lancement du programme de {eventData}}")
    pass
    # if face_recognition.recognize_faces():
    #    logging.debug("personne reconnue")
    # set_ui_msg_open_door(self)

    # else:
    #    logging.debug("personne non connue")
    text_to_send = "Lunching"
    self.transmit_textonQML(text_to_send, label_name)
    