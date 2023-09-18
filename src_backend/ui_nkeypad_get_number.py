import logging

def set_saisie_text_qml(self, eventData):
    self.stored_values.append(eventData)
    # Envoye de la valeur "*" au "pyLbNum_Keypad"
    num_stars = len(self.stored_values)
    stars_text = "*" * num_stars
    logging.debug(stars_text)
    self.transmit_textonQML(stars_text, "pyLbNum_Keypad")

