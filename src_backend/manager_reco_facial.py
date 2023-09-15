#import json
#sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
#from facereco import FaceRecognitionWithIndication
#from Open_Win_Admin import *

#face_recognition = FaceRecognitionWithIndication.FaceRecognition()


import logging
from src_backend.ui_set_open_door import set_ui_msg_open_door

Label_name_reco = "lbcustomrecofacial"

def set_manager_reco_facial(self, eventData, db_backend, storage_backend, LIST_HABITANT_BACKEND ):
    logging.info("Lancement du programme de {eventData}")
    pass
    # if face_recognition.recognize_faces():
    #    logging.debug("personne reconnue")
    # set_ui_msg_open_door(self, ICIlabeldeReco)

    # else:
    #    logging.debug("personne non connue")
    text_to_send = "Lunching"
    self.transmit_textonQML(text_to_send, Label_name_reco)
    