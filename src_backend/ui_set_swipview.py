import logging
from src_backend.constants_ui import EVENT_PREVIOUS_BUTTON_CLICKED, EVENT_NEXT_BUTTON_CLICKED


def managerchangeswipeView(self, eventData):
    logging.info(f"État enregistré : {eventData}")

    if EVENT_PREVIOUS_BUTTON_CLICKED in eventData:
        logging.debug("passez " + eventData)
        label_name = "pyLblnext"
        msg_name = "clicked Previous"
        text_to_send = f"{msg_name} "
        logging.debug(text_to_send)
        self.transmit_textonQML(text_to_send, label_name)

    elif EVENT_NEXT_BUTTON_CLICKED in eventData:
        logging.debug("passez " + eventData)
        label_name = "pyLblnext"
        msg_name = "clicked Next"
        text_to_send = f"{msg_name} "
        logging.debug(text_to_send)
        self.transmit_textonQML(text_to_send, label_name)

    else : 
        logging.debug("Enter else : managerchangeswipeView :" + eventData)


