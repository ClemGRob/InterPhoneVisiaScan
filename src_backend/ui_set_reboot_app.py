import os
import sys
import subprocess
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def managerRebootApp(self, eventData):
    logging.info("In Manager search habitant")
    if EVENT_BLOCK_ACCESS_ADMIN in eventData:
        logging.debug(f"passez {eventData}")

        logging.info("Reboot système")
        restart_application()

    else:
        logging.error("Enter else : manger_search_habitant :" + eventData)


def restart_application():
    try:
        subprocess.Popen(["python", RESTART_APP_WINDOW])
    except Exception as e:
        print(f"Erreur lors du redémarrage de l'application : {str(e)}")
