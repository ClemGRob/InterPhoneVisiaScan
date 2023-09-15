import logging

def set_manager_search_next(self):
    logging.info("Lancement du programme de recherche suivant")
    #face_recognition.current_name_index += 1
    label_name = "pyLbSerach_Hab"
    # Va chercher le nom suivant = msg
    #msg_name = update_name_display(self)
    #msg_name_hab = msg_name[0]
    #msg_number_app = msg_name[1]
    text_to_send = "Action en cours (suivante)"# f" Contacte : {msg_name_hab} \nNum appartement :\n{msg_number_app} "
    self.transmit_textonQML(text_to_send, label_name)
    #if face_recognition.current_name_index == len(list(face_recognition.house_administrator_dict.keys())):
    #    face_recognition.current_name_index = 0