import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from PyQt5.QtWidgets import QApplication
from ui_win_adminpage import AdminPage
from win_admin.set_log_admin import admin_init_log

def main():
    try:
        logging = admin_init_log() 
        logging.info("M - Init App_Win.")
        app = QApplication(sys.argv)
        admin_window = AdminPage(None)  # Créez une instance de AdminPage avec None en argument (ou la fenêtre parente appropriée si nécessaire)
        admin_window.setWindowTitle("Admin Window")
        logging.info("M - Show Interface Application ")
        admin_window.show()
        logging.info("M - System Application Preparation Complete")

    except Exception as e:
        error_message = f"M - An error occurred: {str(e)}"
        logging.error(error_message)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()