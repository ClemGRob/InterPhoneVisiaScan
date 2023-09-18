import os
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QApplication

def main  ():
    app = QApplication(sys.argv)

    # Lire le texte depuis l'entrée standard
    text_to_display = sys.stdin.read()
    #sys.stdin.write(text_to_display)
    
    window = QMainWindow()
    text_edit = QTextEdit(window)
    text_edit.setPlainText(text_to_display)
    window.setCentralWidget(text_edit)

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
