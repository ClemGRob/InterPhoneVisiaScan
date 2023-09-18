import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTransform

class CustomPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Popup personnalisé')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        # Ajoutez une étiquette personnalisée pour le texte de la question
        label = QLabel('Une photo va etre prise, est ce que vous etes placé devant la caméra ?')
        layout.addWidget(label)

        # Ajoutez deux boutons personnalisés
        button_yes = QPushButton('Oui')
        button_no = QPushButton('Non')

        # Spécifiez la hauteur minimale des boutons (par exemple, 40 pixels)
        button_yes.setMinimumHeight(50)
        button_no.setMinimumHeight(50)

        # Associez des actions aux boutons
        button_yes.clicked.connect(self.on_yes_clicked)
        button_no.clicked.connect(self.on_no_clicked)

        layout.addWidget(button_yes)
        layout.addWidget(button_no)

        self.setLayout(layout)

        # Appliquez une transformation de rotation de 90 degrés à la fenêtre
        rotate_transform = QTransform().rotate(90)
        self.setTransform(rotate_transform)

    def on_yes_clicked(self):
        # Traitez l'action lorsque le bouton "Oui" est cliqué
        self.response = 'oui'
        self.accept()

    def on_no_clicked(self):
        # Traitez l'action lorsque le bouton "Non" est cliqué
        self.response = 'non'
        self.accept()

def show_custom_popup(result_file_path):
    app = QApplication(sys.argv)

    # Créez la fenêtre popup personnalisée
    custom_popup = CustomPopup()

    # Affichez la fenêtre et attendez la réponse de l'utilisateur
    response = custom_popup.exec_()

    # Écrivez la réponse dans le fichier temporaire
    with open(result_file_path, 'w') as result_file:
        result_file.write(custom_popup.response)

    sys.exit(app.exec_())

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python popup_script.py <result_file_path>")
        sys.exit(1)

    result_file_path = sys.argv[1]
    show_custom_popup(result_file_path)
