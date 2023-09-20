import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QPushButton, QDesktopWidget, QMessageBox)
from ui_win_optionpage import OptionsPage
from ui_win_virtual_keyboard import VirtualKeyboard

class AdminPage(QWidget):
    def __init__(self, name_display_widget,db, face_recognition,storage,auth):
        """
        Initialize the AdminPage widget.

        Args:
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        logging.info("A - Init_UI")
        self.name_display_widget = name_display_widget
        self.db = db
        self.face_recognition = face_recognition
        self.auth = auth
        self.storage = storage
        self.initUI()
        logging.info("A - End Init")

    def initUI(self):
        """
        Initialize the user interface components of the AdminPage.
        """
        self.setWindowTitle("Admin Page")
        self.setGeometry(0, 0, 300, 150)
        self.center()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("Enter ID")
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter Password")
        verify_button = QPushButton("Verify")
        verify_button.clicked.connect(self.verify)

        layout.addWidget(self.id_input)
        layout.addWidget(self.password_input)
        layout.addWidget(verify_button)

        # Add click event handlers to show the virtual keyboard when the field is clicked.
        self.id_input.mousePressEvent = self.show_virtual_keyboard_id
        self.password_input.mousePressEvent = self.show_virtual_keyboard_password
        


    def verify(self):
        """
        Verify the entered ID and password.

        If the verification is successful, open the OptionsPage.
        Otherwise, display an error message.
        """
        logging.info("A - Start Verify")
        
        entered_id = self.id_input.text()
        entered_password = self.password_input.text()
        #logging.debug(entered_id)
        #logging.debug(entered_password)

        if self.verify_id(entered_id, entered_password):
            logging.debug("A - In OptionPage")
            self.open_options_page()
        else:
            msg_acces = "A - Access Denied", "Incorrect ID or password."
            logging.error(msg_acces)
            QMessageBox.critical(self, msg_acces)

    def verify_id(self, entered_id_input, entered_pwd_input):
        """
        Verify the entered user ID and password.

        This function takes two arguments, `entered_id_input` and `entered_pwd_input`, and compares them
        with the correct user ID and password. It allows a maximum of three attempts for
        verification. If the correct ID and password are entered within the allowed attempts,
        it returns True. Otherwise, after three failed attempts, it returns False.

        :param entered_id_input: The user-provided ID to be verified.
        :type entered_id_input: str
        :param entered_pwd_input: The user-provided password to be verified.
        :type entered_pwd_input: str
        :return: True if the ID and password are correct within 3 attempts, False otherwise.
        :rtype: bool
        """
        correct_id = "cedric"
        correct_password = "1234"
        error_count = 0

        logging.info("A - Verify_ID")
        while error_count < 3:
            if entered_id_input == correct_id and entered_pwd_input == correct_password:
                return True
            error_count += 1
            logging.debug("A - Invalid ID or password. Please try again.")
        # Allow 3 attempts for ID and password verification.

        logging.debug("A - Too many failed attempts. Access denied.")
        return False

    def open_options_page(self):
        """
        Open the OptionsPage and close the AdminPage.
        """
        logging.info("A - Open OptionPage")
        self.options_page = OptionsPage(self.name_display_widget,self.db, self.face_recognition,self.storage,self.auth)
        self.options_page.setWindowTitle("Options Page")
        self.options_page.show()
        logging.info("A - Close OptionPage")
        self.close()

    def center(self):
        """
        Center the widget on the screen.
        """
        logging.info("A - Place of the middle of the window")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_virtual_keyboard_id(self,event):
        """
        Show the virtual keyboard for the ID input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "A - Activation du clavier pour l'ID"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.id_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_password(self,event):
        """
        Show the virtual keyboard for the password input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "A - Activation du clavier pour l'PW"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.password_input)
        virtual_keyboard.exec_()