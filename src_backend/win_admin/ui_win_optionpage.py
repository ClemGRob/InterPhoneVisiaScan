from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QDesktopWidget)
from ui_win_registrationpage import RegistrationPage
from ui_win_deletionpage import DeletionPage

class OptionsPage(QWidget):
    def __init__(self, name_display_widget):
        """
        Initialize the OptionsPage widget.

        Args:
            name_display_widget: A QWidget for displaying names.
        """
        super().__init__()
        self.name_display_widget = name_display_widget
        self.initUI()

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
        self.registration_page = RegistrationPage(self.name_display_widget)
        self.registration_page.setWindowTitle("Registration Page")
        self.registration_page.show()
        self.close()

    def delete(self):
        """
        Open the DeletionPage and close the OptionsPage.
        """
        self.deletion_page = DeletionPage(self.name_display_widget)
        self.deletion_page.setWindowTitle("Deletion Page")
        self.deletion_page.show()
        self.close()

    def center(self):
        """
        Center the widget on the screen.
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())