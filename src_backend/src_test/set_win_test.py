from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QGroupBox

class OptionsPage(QWidget):
    """
    OptionsPage représente la fenêtre principale de l'interface graphique.
    Elle permet de définir les boutons et les actions associées.
    """
    def __init__(self, test_runner):
        super().__init__()
        self.test_runner = test_runner
        self.init_ui()

    def init_ui(self):
        """
        Initialise l'interface utilisateur en créant des widgets et en définissant des actions.
        """
        self.setWindowTitle('Test unitaire')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Boutons pour les fonctionnalités
        self.run_button = QPushButton('Exécuter tous les tests')
        self.run_button.clicked.connect(self.run_unit_tests)
        layout.addWidget(self.run_button)

        self.composant_physique_button = QPushButton('Test Matériels physique')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.composant_physique_button)

        self.soft_Frontend_button = QPushButton('Test Soft Frontend')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.soft_Frontend_button)

        self.soft_Backend_button = QPushButton('Test Soft Backend')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.soft_Backend_button)

        self.soft_button = QPushButton('Test Soft entier')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.soft_button)

        self.test_unitaire_button = QPushButton('Test des tests unitaires')
        # Connectez ce bouton à la fonction correspondante
        layout.addWidget(self.test_unitaire_button)

        # Zone de rendu des résultats
        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)
    
    def run_unit_tests(self):
        """
        Exécute les tests unitaires et affiche les résultats dans la zone de texte.
        """
        test_results = self.test_runner.run_all_tests()
        if not test_results["failed_tests"]:
            self.result_text.setText("Tous les tests ont réussi.")
        else:
            failed_tests = ", ".join(test_results["failed_tests"])
            self.result_text.setText(f"Certains tests unitaires ont échoué.\n {failed_tests}")
