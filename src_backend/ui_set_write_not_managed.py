import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *

def write_messages_to_file(word, file_path):
    logging.info("It not managed"+file_path)
    if word and len(word.strip()) > 0:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if word + "\n" not in lines:
                with open(file_path, "a") as append_file:
                    append_file.write(word + "\n")