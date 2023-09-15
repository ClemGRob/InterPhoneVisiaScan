import logging
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLineEdit, QDesktopWidget, QPushButton, QMessageBox, QCheckBox)
from ui_win_virtual_keyboard import VirtualKeyboard

class DeletionPage(QWidget):
    def __init__(self, name_display_widget):
        """
        Initialize the DeletionPage widget.

        Args:
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        logging.info("D - Init_UI")
        self.name_display_widget = name_display_widget
        self.initUI()
        logging.info("D - End Init")

    def initUI(self):
        """
        Initialize the user interface components of the DeletionPage.
        """
        self.setWindowTitle("Deletion Page")
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
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete)

        layout.addWidget(self.name_input)
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.apartment_number_input)
        layout.addWidget(self.house_admin_checkbox)  # Add the checkbox
        layout.addWidget(delete_button)

        # Add click event handlers to show the virtual keyboard when the field is clicked
        self.name_input.mousePressEvent = self.show_virtual_keyboard_name
        self.last_name_input.mousePressEvent = self.show_virtual_keyboard_last_name
        self.apartment_number_input.mousePressEvent = self.show_virtual_keyboard_apartment

    def delete(self):
        """
        Delete a person based on the provided information.

        Retrieves the name, last name, apartment number, and house administrator status
        from the input fields, deletes the person using FaceRecognition,
        displays a success or failure message, and updates the name list in the name_display_widget.
        """
        logging.info("D - Saisie RegistrationPage")
        name = self.name_input.text()
        last_name = self.last_name_input.text()
        apartment_number = self.apartment_number_input.text()
        is_house_admin = self.house_admin_checkbox.isChecked()  # Check if the checkbox is checked
        result = print(name, last_name, apartment_number, is_house_admin)
        if result:
            msg = "D - Deletion Success", "Person successfully deleted."
            logging.info(msg)
            QMessageBox.information(self, msg)
        else:
            msg = "D - Deletion Failed", "Person not found or deletion failed."
            logging.error(msg)
            QMessageBox.critical(self, msg)
        logging.info("D - Close Saisie RegistrationPage")
        self.close()
        self.name_display_widget.update_name_list()
        logging.info("D - Fin de l'update de la liste")

    def center(self):
        """
        Center the widget on the screen.
        """
        logging.info("D - Place of the middle of the window")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def show_virtual_keyboard_name(self):
        """
        Show the virtual keyboard for the name input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "D - Activation du clavier pour le name"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_last_name(self):
        """
        Show the virtual keyboard for the last name input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "D - Activation du clavier pour last name"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.last_name_input)
        virtual_keyboard.exec_()

    def show_virtual_keyboard_apartment(self):
        """
        Show the virtual keyboard for the apartment number input field.

        Args:
            event: The mousePressEvent event.
        """
        msg = "D - Activation du clavier pour le number appartement"
        logging.info(msg)
        virtual_keyboard = VirtualKeyboard(self.apartment_number_input)
        virtual_keyboard.exec_()