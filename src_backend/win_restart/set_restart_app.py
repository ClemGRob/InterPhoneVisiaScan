import os
import sys
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def restart_app():
    try:
        # Fermez l'application actuelle (Show_app_window.py).
        # Vous pouvez utiliser un gestionnaire de processus approprié, comme psutil, pour cela.
        # Ici, nous supposerons que vous fermez l'application manuellement.

        # Redémarrez l'application (Show_app_window.py).
        subprocess.Popen(["python", APP_WINDOW_MAIN])
        

    except Exception as e:
        print(f"Erreur lors du redémarrage de l'application : {str(e)}")

if __name__ == "__main__":
    restart_app()
