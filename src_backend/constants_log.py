import os
import enum

# Folder projet interphone
LOG_DIR = "src_backend/Repport/"

# Information des trace d'erreur
ERROR_TRACE_FILE_PATH = os.path.join(LOG_DIR, 'Error.trace')

# Information des logs pour des log général
LOG_FILENAME = "APP_Window.log"

#Structure du code
LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"  # Format du journal
MAX_BYTES = 1024*1024
LOG_MAX_FILES = 4  

class LogLevel(enum.Enum):
    INFO    = "INFO"
    DEBUG   = "DEBUG"
    ERROR   = "ERROR"

# Niveau de journalisation par défaut
    # Remplacez "DEBUG" par le niveau de votre choix
DEFAULT_LOG_LEVEL = LogLevel.DEBUG  

# Reset 
MAX_AGE_DAYS = 2  # Définissez le nombre maximal de jours pour conserver les fichiers
