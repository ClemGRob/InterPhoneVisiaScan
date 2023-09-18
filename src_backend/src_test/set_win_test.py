from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QGroupBox



class OptionsPage(QWidget):
    def __init__(self, test_runner):
        super().__init__()
        self.test_runner = test_runner
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Test unitaire')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Boutons pour les fonctionnalités
        self.run_button = QPushButton('Exécuter les tests')
        self.run_button.clicked.connect(self.run_unit_tests)
        layout.addWidget(self.run_button)

        self.storage_button = QPushButton('Espace de stockage')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.storage_button)

        self.capture_button = QPushButton('Capture de photo')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.capture_button)

        self.log_button = QPushButton('Affichage des logs')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.log_button)

        self.frontend_button = QPushButton('Fonctionnement du frontend')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.frontend_button)

        self.backend_button = QPushButton('Fonctionnement du backend')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.backend_button)

        self.admins_button = QPushButton('Fonctionnement de la partie admins')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.admins_button)

        self.tests_button = QPushButton('Fonctionnement de la partie tests')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.tests_button)

        # Zone de rendu des résultats
        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)
    
    def run_unit_tests(self):
        result = self.test_runner.run_all_tests()
        if result:
            self.result_text.setText("Tous les tests unitaires ont réussi.")
        else:
            self.result_text.setText("Certains tests unitaires ont échoué.")