import sys
import os
import pyrebase
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from src.wrapper import *
import config

firebase = pyrebase.initialize_app(config.pirebaseConfig)
db = firebase.database()

data = {
        "users":
        {
            "noms":
            {
                "Cedric": 
                {
                    "email":"Cedric@gmail.com",
                    "numero apartement" : "1"
                },
        
                "Clement":
                {
                    "email":"clement@gmail.com",
                    "numero apartement" : "2"

                },
                "Constentin":
                {
                    "email":"Constentin@gmail.com",
                    "numero apartement" : "3"

                },
                "Ifuja" : 
                {
                    "email":"Ifuja@gmail.com",
                    "numero apartement" : "4"
                }
            }
        },
        "token":
        { 
            "Cedric": "123",
            "Clement": "456",
            "Constentin":"789",
            "Ifuja" : "101",
        }
    }
print(set_data(db,data))