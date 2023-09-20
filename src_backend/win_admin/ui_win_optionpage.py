import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QDesktopWidget)
from ui_win_registrationpage import RegistrationPage
from ui_win_deletionpage import DeletionPage

class OptionsPage(QWidget):
    def __init__(self, name_display_widget,db, face_recognition,storage,auth):
        """
        Initialize the OptionsPage widget.

        Args:
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        logging.info("O - Init_UI")
        self.name_display_widget = name_display_widget
        self.db = db
        self.face_recognition = face_recognition
        self.auth = auth
        self.storage = storage
        self.initUI()
        logging.info("O - End Init")

    def initUI(self):
        """
        Initialize the user interface components of the OptionsPage.
        """
        self.setWindowTitle("Options Page")
        self.setGeometry(0, 0, 400, 50)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        register_button = QPushButton("Register")
        delete_button = QPushButton("Delete")

        register_button.clicked.connect(self.register)
        delete_button.clicked.connect(self.delete)

        layout.addWidget(register_button)
        layout.addWidget(delete_button)

    def register(self):
        """
        Open the RegistrationPage and close the OptionsPage.
        """
        logging.info("O - Open RegistrationPage")
        self.registration_page = RegistrationPage(self.name_display_widget, self.db, self.face_recognition,self.storage,self.auth)
        self.registration_page.setWindowTitle("Registration Page")
        self.registration_page.show()
        logging.info("O - Close RegistrationPage")
        self.close()

    def delete(self):
        """
        Open the DeletionPage and close the OptionsPage.
        """
        logging.info("O - Open DeletionPage")
        self.deletion_page = DeletionPage(self.name_display_widget)
        self.deletion_page.setWindowTitle("Deletion Page")
        self.deletion_page.show()
        logging.info("O - Close DeletionPage")
        self.close()

    def center(self):
        """
        Center the widget on the screen.
        """
        logging.info("O - Place of the middle of the window")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())