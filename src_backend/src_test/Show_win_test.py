import os
import sys
import logging

from PyQt5.QtWidgets import QMainWindow, QTextEdit

from PyQt5.QtWidgets import QApplication

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_test.set_log_test import test_init_log
from src_test.set_win_test import OptionsPage
from src_test.set_run_test import TestUnitaire 

def main():
    logging = test_init_log() 
    logging.info("Start App_test.")

    app = QApplication(sys.argv)
    
    test_runner = TestUnitaire()
    options_page = OptionsPage(test_runner)
    options_page.show()
    
    result = options_page.run_unit_tests() 
    logging.debug(f"App_test succes lunch : {result}")
    #sys.exit(0 if result else 1)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
