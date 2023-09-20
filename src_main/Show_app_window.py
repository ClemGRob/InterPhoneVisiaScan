#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import pyrebase

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src_backend.constants_ui import *
from src_backend.ui_manager_backend import Backend
from src_backend.set_log import init_log
from src_backend.set_error import call_exception

from facereco import FaceRecognitionWithIndication
import pyrebase_val.config as config
import pyrebase_val.src as serveraction
firebase = pyrebase.initialize_app(config.pirebaseConfig)
db = firebase.database()
storage = firebase.storage()
auth=firebase.auth()
face_recognition = FaceRecognitionWithIndication.FaceRecognition(storage, auth, db)
try:
    DICT_HABITANT = serveraction.get_data(db, "token")#["noms"]
except KeyError:
    logging.error("The 'noms' key was not found in the data.")

if __name__ == "__main__":
    try:
        
        logger = init_log()
        logging.info(logger)
        LIST_HABITANT = [*DICT_HABITANT] 
        app = QGuiApplication(sys.argv)
        view = QQmlApplicationEngine()
        logging.info("Init Backend")
        backend = Backend(view ,db, storage,auth,face_recognition, LIST_HABITANT)
        logging.info("Init Application")
        context = view.rootContext()
        context.setContextProperty("backend", backend)
        logging.info("Load Interface Application")
        view.load(QUrl.fromLocalFile(MAIN_WINDOW_QML))
        if not view.rootObjects():
            logging.info("Exit Application")
            sys.exit(-1)

    except Exception as e:
        call_exception(e)

    logging.info("System Application Preparation Complete")
    sys.exit(app.exec_())