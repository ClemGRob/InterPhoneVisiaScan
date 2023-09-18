import logging

def managerCloseUI(self, eventData):
    if "Open_Admin" in eventData:
        logging.debug("Receipt of: " + eventData)
        logging.info("Fermeture de l'interface")
 
    else:
        logging.debug("Enter else : managerActivateAdmin :" + eventData)