# constant_win.py
import enum

ADM_LOG_DIR = "src_backend/Repport"  # Répertoire où les fichiers journaux seront stockés
ADM_LOG_FILENAME = "Win_Admin.log"  # Nom du fichier journal principal

class LogLevel(enum.Enum):# Niveau de journalisation
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"  

ADM_DEFAULT_LOG_LEVEL = LogLevel.DEBUG  


ADM_LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"  # Format du journal
ADM_LOG_MAX_FILES = 4  # Nombre maximal de fichiers journaux à conserver

