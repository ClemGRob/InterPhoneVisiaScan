import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QDesktopWidget, QPushButton, QMessageBox, QCheckBox)
from ui_win_virtual_keyboard import VirtualKeyboard
import pyrebase
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import pyrebase_val.config as config
import pyrebase_val.src as serveraction
from facereco import FaceRecognitionWithIndication

firebase = pyrebase.initialize_app(config.pirebaseConfig)
db = firebase.database()
storage = firebase.storage()
auth=firebase.auth()
face_recognition = FaceRecognitionWithIndication.FaceRecognition(storage, auth, db)

class RegistrationPage(QWidget):
    def __init__(self,name_display_widget):
        """
        Initialize the RegistrationPage widget.

        Args:
            name_display_widget: A QWidget for displaying names.
        """
        self.db = db
        self.face_recognition = face_recognition
        self.auth = auth
        self.storage = storage
        super().__init__()
        logging.info("R - Init_UI")
        self.name_display_widget = name_display_widget
        self.initUI()
        logging.info("R - End Init")

    def initUI(self):
        """
        Initialize the user interface components of the RegistrationPage.
        """
        self.setWindowTitle("Registration Page")
        self.setGeometry(0, 0, 350, 150)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Name")
        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Enter Last Name")
        self.apartment_number_input = QLineEdit(self)
        self.apartment_number_input.setPlaceholderText("Enter Apartment Number")
        self.house_admin_checkbox = QCheckBox("House administrator")  # Add the checkbox
        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)

        layout.addWidget(self.name_input)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.apartment_number_input)
        layout.addWidget(self.house_admin_checkbox)  # Add the checkbox
        layout.addWidget(register_button)

        # Add click event handlers to show the virtual keyboard when the field is clicked
        self.name_input.mousePressEvent = self.show_virtual_keyboard_name
        self.last_name_input.mousePressEvent = self.show_virtual_keyboard_last_name
        self.apartment_number_input.mousePressEvent = self.show_virtual_keyboard_apartment

    def register(self):
        """
        Register a person with the provided information.

        Retrieves the name, last name, apartment number, and house administrator status
        from the input fields, registers the person using FaceRecognition,
        displays a success message, and updates the name list in the name_display_widget.
        """
        logging.info("R - Saisie RegistrationPage")
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        apartment_number = self.apartment_number_input.text()
        is_house_admin = self.house_admin_checkbox.isChecked()  
        self.face_recognition.register_faces(name, last_name, apartment_number, is_house_admin)
        
        logging.debug((name, last_name, apartment_number, is_house_admin))
        serveraction.set_data(self.db,{"numero":apartment_number },"users","nom",last_name)
        QMessageBox.information(self, "Registration Success", "Person successfully registered.")
        logging.info("R - Close Saisie RegistrationPage")
        self.close()
        # self.name_display_widget.update_name_list()
        logging.info("R - Fin de l'update de la liste")

    def center(self):
        """
        Center the widget on the screen.
        """
        logging.info("R - Place of the middle of the window")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_virtual_keyboard_name(self, event):
        """
        Show the virtual keyboard for the name input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "R - Activation du clavier pour le name"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_last_name(self, event):
        """
        Show the virtual keyboard for the last name input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "R - Activation du clavier pour last name"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.last_name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_apartment(self, event):
        """
        Show the virtual keyboard for the apartment number input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "R - Activation du clavier pour le number appartement"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.apartment_number_input)
        virtual_keyboard.exec_()