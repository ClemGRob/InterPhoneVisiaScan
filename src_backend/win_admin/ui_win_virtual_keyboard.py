from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QFrame, QGridLayout, QPushButton)


def show_virtual_keyboard_id(self, event):
    """
    Show the virtual keyboard for the ID input field.

    Args:
        event: The mousePressEvent event.
    """
    virtual_keyboard = VirtualKeyboard(self.id_input)
    virtual_keyboard.exec_()

def show_virtual_keyboard_password(self, event):
    """
    Show the virtual keyboard for the password input field.

    Args:
        event: The mousePressEvent event.
    """
    virtual_keyboard = VirtualKeyboard(self.password_input)
    virtual_keyboard.exec_()

class VirtualKeyboard(QDialog):
    def __init__(self, target_input):
        """
        Initialize the VirtualKeyboard dialog.

        Args:
            target_input: The input field to which the virtual keyboard inputs characters.
        """
        super().__init__()
        self.target_input = target_input
        self.setWindowTitle("Virtual Keyboard")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Add a frame at the bottom of the screen for the virtual keyboard
        self.keyboard_frame = QFrame()
        self.keyboard_frame.setFrameShape(QFrame.StyledPanel)
        self.keyboard_layout = QGridLayout(self.keyboard_frame)

        buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Backspace', 'Space', 'Enter'
        ]

        row, col = 0, 0
        for button_text in buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_click)
            self.keyboard_layout.addWidget(button, row, col)
            col += 1
            if col > 9:
                col = 0
                row += 1

        self.layout.addWidget(self.keyboard_frame)
        self.keyboard_frame.hide()  # By default, hide the virtual keyboard

    def button_click(self):
        """
        Handle button clicks on the virtual keyboard.

        Depending on the clicked button, insert characters, delete characters, add a space,
        or accept the input.
        """
        button = self.sender()
        text = button.text()
        if text == 'Backspace':
            current_text = self.target_input.text()
            self.target_input.setText(current_text[:-1])
        elif text == 'Space':
            current_text = self.target_input.text()
            self.target_input.setText(current_text + ' ')
        elif text == 'Enter':
            self.accept()
        else:
            current_text = self.target_input.text()
            self.target_input.setText(current_text + text)

    def showEvent(self, event):
        """
        Show the virtual keyboard when the input field is selected.

        Args:
            event: The showEvent event.
        """
        self.keyboard_frame.show()

    def hideEvent(self, event):
        """
        Hide the virtual keyboard when the input field loses focus.

        Args:
            event: The hideEvent event.
        """
        self.keyboard_frame.hide()