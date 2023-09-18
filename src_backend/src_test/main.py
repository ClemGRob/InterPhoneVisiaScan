import sys
from PyQt5.QtWidgets import QApplication

# Importez la classe FrontendTest depuis frontend_test.py
from frontend_test import FrontendTest

def main():
    try:
        app = QApplication(sys.argv)

        # Créez une instance de FrontendTest
        frontend = FrontendTest()
        
        # Exécutez la fenêtre de test
        frontend.show()
    except Exception as e:
        print(f"Une exception s'est produite : {str(e)}")

if __name__ == "__main__":
    main()
