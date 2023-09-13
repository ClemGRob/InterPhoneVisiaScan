import sys
from PyQt5.QtWidgets import QApplication

from ui_win_adminpage import AdminPage

def main():
    app = QApplication(sys.argv)
    admin_window = AdminPage(None)  # Créez une instance de AdminPage avec None en argument (ou la fenêtre parente appropriée si nécessaire)
    admin_window.setWindowTitle("Admin Window")
    admin_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()