import enum

# Folder projet interphone
FOLDER_VISIA_SCAN = "src_backend/Repport"

# Information des trace d'erreur
ERROR_TRACE_FILE_PATH = FOLDER_VISIA_SCAN + 'Error.trace'
ERROR_PREVIOUS_TRACE_FILE_PATH = FOLDER_VISIA_SCAN + 'Error.previous.trace'

# Information des logs
LOG_TEST_FILE_PATH = FOLDER_VISIA_SCAN +"/test_information.log"
LOG_FILE_PATH = FOLDER_VISIA_SCAN + "/information.log"
MAX_BYTES = 1024*1024
BACKUP_COUNT = 3

class LogLevel(enum.Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"

# Niveau de journalisation par défaut
DEFAULT_LOG_LEVEL = LogLevel.DEBUG  # Remplacez "DEBUG" par le niveau de votre choix
DEFAULT_LOG_TEST_LEVEL = LogLevel.ERROR  