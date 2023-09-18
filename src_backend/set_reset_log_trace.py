import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_log import *

def remove_old_logs(log_dir, max_age_days):
    """
    Supprime les fichiers journaux trop anciens du répertoire de journaux.
    
    :param log_dir: Le chemin vers le répertoire contenant les fichiers journaux.
    :param max_age_days: Le nombre maximal de jours avant qu'un fichier ne soit considéré comme trop ancien.
    """
    current_time = time.time()

    for log_file in os.listdir(log_dir):
        log_path = os.path.join(log_dir, log_file)

        if os.path.isfile(log_path):
            # Obtenez l'horodatage de création du fichier
            file_creation_time = os.path.getctime(log_path)

            # Calculez le nombre de jours depuis la création du fichier
            days_since_creation = (current_time - file_creation_time) / (60 * 60 * 24)

            # Si le fichier est plus ancien que max_age_days, supprimez-le
            if days_since_creation > max_age_days:
                os.remove(log_path)

def reset_file(file_path):
    """
    Réinitialise le fichier en renommant l'ancien avec un horodatage et en créant un nouveau fichier vide.
    """

    remove_old_logs(FOLDER_REPPORT_PREVIOUS_VISIA_SCAN, MAX_AGE_DAYS)

    # Renommer l'ancien fichier avec un horodatage
    if os.path.exists(file_path):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        backup_path = f"src_backend/Repport/old_trace/old_{os.path.basename(file_path)}_{timestamp}"
        print(file_path)
        os.rename(file_path, backup_path)

    # Suppression de l'ancien fichier et ouverture d'un nouveau
    if os.path.exists(file_path):
        os.remove(file_path)
    open(file_path, 'a').close()

def init_reset_file(self):
    """
    Initialise et réinitialise les fichiers de log et de trace.
    """
    reset_file(LOG_FILE_PATH)
    self.logger.info('File log reset')
    reset_file(ERROR_TRACE_FILE_PATH)
    self.logger.info('File trace reset')
