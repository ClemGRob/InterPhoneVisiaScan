import os
import sys
import logging

from threading import Lock
from logging.handlers import RotatingFileHandler

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.set_reset_log_trace import init_reset_file
from src_backend.constants_log import *

class LogManager:
    """
    Classe pour la gestion des logs :
    """

    def __init__(self):
        """
        Initialisation du gestionnaire de logs et des traces d'erreur.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(DEFAULT_LOG_LEVEL.value)

        init_reset_file(self)

        # Configuration du gestionnaire de fichiers de logs
        log_file_path = LOG_FILE_PATH
        max_bytes = MAX_BYTES
        backup_count = BACKUP_COUNT
        contents_formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        handler = RotatingFileHandler(log_file_path, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter(contents_formatter)
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

        # Initialisation d'un verrou pour le fichier de log
        self.log_lock = Lock()

    def _acquire_lock(self):
        """
        Acquérir le verrou du fichier de log.
        """
        self.log_lock.acquire()

    def _release_lock(self):
        """
        Libérer le verrou du fichier de log.
        """
        self.log_lock.release()

    def info(self, message):
        """
        Enregistrer un message d'information dans les logs.

        Args:
            message (str): Le message à enregistrer.
        """
        self._acquire_lock()
        try:
            self.logger.info(message)
        finally:
            self._release_lock()


    def error(self, message):
        """
        Enregistrer un message d'erreur dans les logs.

        Args:
            message (str): Le message d'erreur à enregistrer.
        """
        self._acquire_lock()
        try:
            self.logger.error(message)
        finally:
            self._release_lock()

    def debug(self, message):
        """
        Enregistrer un message de débogage dans les logs.

        Args:
            message (str): Le message de débogage à enregistrer.
        """
        self._acquire_lock()
        try:
            self.logger.debug(message)
        finally:
            self._release_lock()

def management_logging():
    """
    Initialiser le gestionnaire de logs.

    Returns:
        LogManager: Instance du gestionnaire de logs.
    """
    return LogManager()

def init_log():
    # Initialisation de la gestion des logs
    logger = management_logging()
    logger.info("Starting the application")
    return logger