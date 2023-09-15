import os
import sys
import logging
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pyrebase_val.src as serveraction

def update_name_display(db):
    logging.info("Lancement du programme de raffraichissement")
    DICT_HABITANT = serveraction.get_data(db,"users")["noms"]
    #registered_names = list(face_recognition.house_administrator_dict.keys())

    #if not registered_names:
    #    name: str = "No names registered"
    #    return name
    #current_name = registered_names[face_recognition.current_name_index]
    ## Remove any digits at the end of the name (if any)
    #current_name = ''.join(filter(lambda x: not x.isdigit(), current_name))
    ## Replace underscores with spaces
    #msg_name = current_name.replace("_", " ")
    #msg_appt = msg_name.rsplit(' ', 1)[-1]
    #msg_name_hab = msg_name.rsplit(' ', 1)[0]

    return #msg_name_hab, msg_appt