import os
import logging
from logging.handlers import RotatingFileHandler
from src_backend.constants_log import LOG_DIR, LOG_FILENAME, DEFAULT_LOG_LEVEL, LOG_FORMAT, LOG_MAX_FILES

class LogManager:
    """
    Initialisation du gestionnaire de logs et des traces d'erreur.
    """
    def __init__(self, log_level=DEFAULT_LOG_LEVEL):
        """
        Initialise un objet LogManager.

        Args:
            log_level (str): Niveau de journalisation (par défaut : "DEBUG").
        """
        self.log_level = log_level
        self.logger = None

    def setup_logging(self):
        """
        Configure le système de journalisation.
        
        Returns:
            logger: Instance du logger configuré.
        """
        # Vérifie si le répertoire de logs existe, sinon le crée
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        # Configuration du logger
        self.logger = logging.getLogger()
        self.logger.setLevel(self.log_level)

        # Configuration du gestionnaire de fichiers journaux rotatifs
        log_file = os.path.join(LOG_DIR, LOG_FILENAME)
        handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=LOG_MAX_FILES-1)
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        self.logger.addHandler(handler)

        return self.logger

def init_log():
    """
    Initialise et configure le journal de l'application.

    Returns:
        logger: Instance du logger configuré.
    """
    log_manager = LogManager(log_level=DEFAULT_LOG_LEVEL.value)  # Vous pouvez spécifier le niveau de journalisation ici
    log_manager.setup_logging()
    logging.debug("Log init ok")
    return log_manager.logger