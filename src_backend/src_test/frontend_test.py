import os
import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QApplication
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_test.constants_test import THEMES  # Importez la liste des thèmes depuis constant_test.py

class FrontendTest(QMainWindow):
    def __init__(self):
        super().__init__()

        # Paramètres de la fenêtre principale
        self.setWindowTitle("Frontend Test")
        self.setGeometry(100, 100, 1920, 1080)  # Résolution 1920x1080

        # Création du widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout(central_widget)

        self.add_theme_buttons(layout)
        self.add_input_area(layout)
        self.add_results_area(layout)

    def add_theme_buttons(self, layout):
        # Boutons pour chaque thème
        theme_buttons = QWidget()
        theme_layout = QVBoxLayout(theme_buttons)

        # Ajoutez des boutons pour chaque thème à partir de la liste THEMES
        for theme in THEMES:
            button = QPushButton(theme)
            theme_layout.addWidget(button)

        theme_buttons.setLayout(theme_layout)
        layout.addWidget(theme_buttons)

    def add_input_area(self, layout):
        # Zone de saisie
        input_label = QLabel("Zone de saisie:")
        input_text = QTextEdit()
        layout.addWidget(input_label)
        layout.addWidget(input_text)

    def add_results_area(self, layout):
        # Zone d'affichage des résultats des tests
        results_label = QLabel("Zone d'affichage des résultats:")
        results_text = QTextEdit()
        results_text.setReadOnly(True)  # Rendre la zone d'affichage en lecture seule
        layout.addWidget(results_label)
        layout.addWidget(results_text)
