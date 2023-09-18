import os
import enum

#####Front #####

# Liste des thèmes
THEMES = ["Thème 1", "Thème 2", "Thème 3", "Thème 4"]


##### LOG #####

TEST_LOG_DIR = "src_backend/Repport"  # Répertoire où les fichiers journaux seront stockés
TEST_LOG_FILENAME = "TEST_App_Window.log"  # Nom du fichier journal principal

class LogLevel(enum.Enum):# Niveau de journalisation
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"  

TEST_DEFAULT_LOG_LEVEL = LogLevel.DEBUG  


TEST_LOG_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"  # Format du journal
TEST_LOG_MAX_FILES = 4  # Nombre maximal de fichiers journaux à conserver