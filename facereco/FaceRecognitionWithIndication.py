import cv2
import numpy as np
import evdev
import dlib
import json  # Import the json module
import shutil
import time
import sys
import os
import pyrebase

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pyrebase_val.config as config
import pyrebase_val.src as serveraction
from my_tool import get_linux_distribution
current_pos = str(os.path.dirname(os.path.abspath(__file__)))
distr = get_linux_distribution()
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
touchscreen_device = None

for device in devices:
    if "event" in device.fn:
        touchscreen_device = device
        break

class FaceRecognition:


    def __init__(self,storage,auth,db):
        print(current_pos)
        self.name = ""
        self.last_name = ""
        self.apartment_number = ""
        self.input_ID = ""
        self.input_password = ""
        self.face_cascade = cv2.CascadeClassifier(current_pos+'/haarcascade_frontalface_default.xml')
        self.images_per_person = 5
        
        self.storage = storage
        self.auth = auth
        self.db = db
        self.user = serveraction.login(self.auth, "password@password.password", "password")
        try:
            file = current_pos+'/images_per_person_dict.json'  # Change the filename to use JSON
            online_file = 'images_per_person_dict.json'
            serveraction.download(self.storage, file, online_file, self.user)
            with open('images_per_person_dict.json', 'r') as file:  # Change file format to read JSON
                self.images_per_person_dict = json.load(file)  # Use json.load to read JSON
        except FileNotFoundError:
            self.images_per_person_dict = {}
        try:
            file = current_pos+'/house_administrator_dict.json'  # Change the filename to use JSON
            online_file = 'house_administrator_dict.json'
            serveraction.download(self.storage, file, online_file, self.user)
            with open(current_pos+'house_administrator_dict.json', 'r') as file:  # Change file format to read JSON
                self.house_administrator_dict = json.load(file)  # Use json.load to read JSON
        except FileNotFoundError:
            self.house_administrator_dict = {}
        self.training_data = []
        self.recognizer = cv2.face_LBPHFaceRecognizer.create()

    def verify_id(self, entered_id_input, entered_pwd_input):
        correct_id = "cedric"
        correct_password = "1234"
        error_count = 0

        while error_count < 3:
            if entered_id_input == correct_id and entered_pwd_input == correct_password:
                return True
            error_count += 1
            print("Invalid ID or password. Please try again.")

        print("Too many failed attempts. Access denied.")
        return False

    def capture_photos(self, name_client):
        cap = cv2.VideoCapture(0)

        self.images_per_person_dict[name_client] = 0

        while self.images_per_person_dict[name_client] < self.images_per_person:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces_detected = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces_detected:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if self.images_per_person_dict[name_client] <= 2:
                    cv2.putText(frame, "Front face - Press space to capture", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                (0, 0, 255), 2)
                elif self.images_per_person_dict[name_client] == 3:
                    cv2.putText(frame, "Left profile - Press space to capture", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                (0, 0, 255), 2)
                elif self.images_per_person_dict[name_client] == 4:
                    cv2.putText(frame, "Right profile - Press space to capture", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                                0.7, (0, 0, 255), 2)

                # if distr=="ubuntu":
                #     key = cv2.waitKey(1)
                #     if key == ord(' '):

                img_name = os.path.join(current_pos,'dataset', name_client,f"{name_client}{self.images_per_person_dict[name_client] + 1}.jpg")

                print(img_name)
                cv2.imwrite(img_name, gray[y:y + h, x:x + w])
                print(f"Image {self.images_per_person_dict[name_client] + 1} of {name_client} saved.")
                self.images_per_person_dict[name_client] += 1
                # else:
                #     touchscreen = evdev.InputDevice(touchscreen_device.fn)
                #     for event in touchscreen.read_loop():

                #         img_name = os.path.join(current_pos,'dataset', name_client,f"{name_client}{self.images_per_person_dict[name_client] + 1}.jpg")
            
                #         # self.images_per_person_dict[name_client] +=1
                #         # img_name = "/home/clem/pyrebaseIAScan/"+str(name_client)+"/"+str(name_client)+str(self.images_per_person_dict[name_client] )+".jpg"
                #         # os.path.join('dataset', name_client,
                #         #                         f"{name_client}{self.images_per_person_dict[name_client] + 1}.jpg")
                #         print(img_name)
                #         cv2.imwrite(img_name, gray[y:y + h, x:x + w])
                #         print(f"Image {self.images_per_person_dict[name_client] + 1} of {name_client} saved.")
                #         self.images_per_person_dict[name_client] += 1
                #         time.sleep(1)


            cv2.imshow('Capture', frame)

            key = cv2.waitKey(1)

            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def register_faces(self, name, last_name, apartment_number, is_house_admin=False):
        self.name = name
        self.last_name = last_name
        self.apartment_number = apartment_number

        full_name = f"{name}_{last_name}_{apartment_number}"
        try: 
            os.makedirs(current_pos+"/dataset/"+full_name)
        except Exception as e:
            pass
        if full_name not in self.images_per_person_dict:
            person_id = len(self.images_per_person_dict) + 1
            self.images_per_person_dict[full_name] = person_id

            # Save the updated dictionary to JSON
            with open('images_per_person_dict.json', 'w') as file:
                json.dump(self.images_per_person_dict, file)
            file = 'images_per_person_dict.json'
            online_file = 'images_per_person_dict.json'
            serveraction.upload(self.storage, file, online_file, self.user)
            if is_house_admin:
                self.house_administrator_dict[full_name] = person_id
                # Save the updated dictionary to JSON
                with open('house_administrator_dict.json', 'w') as file:
                    json.dump(self.house_administrator_dict, file)

                file = 'house_administrator_dict.json'
                online_file = file
                serveraction.upload(self.storage, file, online_file, self.user)
        self.capture_photos(full_name)
        

        for i in range(self.images_per_person):
            img_path = os.path.join(current_pos,'dataset', full_name, f"{full_name}{i + 1}.jpg")
            self.training_data.append(
                (cv2.imread(img_path, cv2.IMREAD_GRAYSCALE), self.images_per_person_dict[full_name]))
            
        x_train = [data[0] for data in self.training_data]
        y_train = [data[1] for data in self.training_data]
        self.recognizer.train(x_train, np.array(y_train))

        self.recognizer.save(current_pos+'/face_recognition_model.yml')

        serveraction.upload(self.storage,"face_recognition_model.yml",self.user)

    def delete_person(self, name, last_name, apartment_number):
        
        self.name = name
        self.last_name = last_name
        self.apartment_number = apartment_number

        full_name = f"{name}_{last_name}_{apartment_number}"

        # Create a list of keys to delete
        keys_to_delete = []

        for key in self.images_per_person_dict:
            if key.lower() == full_name.lower():
                keys_to_delete.append(key)

        # Remove found keys from the dictionary
        for key in keys_to_delete:
            del self.images_per_person_dict[key]

        # Remove associated files
        for key in keys_to_delete:
            remove(self.storage,full_name,self.user,"dataset")

        # Update training data
        self.training_data = [(img, label) for img, label in self.training_data if
                              label not in [self.images_per_person_dict.get(key) for key in keys_to_delete]]

        # Remove from house administrator list if present
        if full_name in self.house_administrator_dict:
            del self.house_administrator_dict[full_name]
            with open('house_administrator_dict.json', 'w') as file:
                json.dump(self.house_administrator_dict, file)
            serveraction.upload(self.storage,'house_administrator_dict.json','house_administrator_dict.json',self.user)
            if os.path.exists('house_administrator_dict.json'):
                shutil.rmtree('house_administrator_dict.json')
        if len(self.training_data) >= 2:
            x_train = [data[0] for data in self.training_data]
            y_train = [data[1] for data in self.training_data]
            self.recognizer.train(x_train, np.array(y_train))

        # Save the updated dictionaries to JSON
        with open('images_per_person_dict.json', 'w') as file:
            json.dump(self.images_per_person_dict, file)
        serveraction.upload(self.storage,'images_per_person_dict.json','images_per_person_dict.json',self.user)
        if os.path.exists('images_per_person_dict.json'):
            shutil.rmtree('images_per_person_dict.json')
        # Remove the recognition model if necessary
        if len(self.training_data) < 2:
            serveraction.remove(self.storage,"face_recognition_model.yml")
            if os.path.exists("face_recognition_model.yml"):
                shutil.rmtree("face_recognition_model.yml")
        return True

    def recognize_faces(self):
        cap = cv2.VideoCapture(0)
        predictor = dlib.shape_predictor(current_pos+'/shape_predictor_68_face_landmarks.dat')
        serveraction.download(self.storage,"face_recognition_model.yml","face_recognition_model.yml",self.user)
        print("download")
        self.recognizer.read(current_pos+'/face_recognition_model.yml')
        print("read")
        
        cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Face Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        start_time = time.time()
        delay_passed = False

        while True:
            ret, frame = cap.read()

            if not delay_passed:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow('Face Detection', frame)

                if time.time() - start_time > 15:
                    delay_passed = True
            else:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                for (x, y, w, h) in faces:
                    roi_gray = gray[y:y + h, x:x + w]
                    landmarks = predictor(roi_gray, dlib.rectangle(0, 0, w, h))

                    left_eye = landmarks.part(36)
                    right_eye = landmarks.part(45)
                    eye_distance_x = right_eye.x - left_eye.x

                    if eye_distance_x > 10:
                        gray_face = roi_gray[y:y + h, x:x + w]
                        print(str(gray_face))
                        confidence = 110
                        if np.size(gray_face) > 0:
                            
                            label, confidence = self.recognizer.predict(gray_face)
                            print(confidence)

                        if confidence < 100:
                            print("Door Open")
                            cap.release()
                            cv2.destroyAllWindows()
                            if os.path.exists("face_recognition_model.yml"):
                                shutil.rmtree("face_recognition_model.yml")
                            return True
                        else:
                            print("Unknown person")
                    else:
                        print("Security checks fail")
                cv2.imshow('Face Detection', frame)

            if time.time() - start_time > 10:
                print("Timeout: No face recognized in 10 seconds.")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        if os.path.exists("face_recognition_model.yml"):
                shutil.rmtree("face_recognition_model.yml")
        return False

    def web_cam_single_photo(self,name:str):
        cap = cv2.VideoCapture(0)
        id_photo=0
        ret, frame = cap.read()
        cv2.imwrite(name+str(id_photo)+".png", frame)
        print(name+str(id_photo)+".png")
        id_photo+=1
        cap.release()
        cv2.destroyAllWindows()
        time.sleep(0.1)

    def verify_photo(self, name:str):
        print(name)
        cap = cv2.VideoCapture(0)
        predictor = dlib.shape_predictor(current_pos+'/shape_predictor_68_face_landmarks.dat')
        serveraction.download(self.storage,"face_recognition_model.yml","face_recognition_model.yml",self.user)
        self.recognizer.read(current_pos+'/face_recognition_model.yml')
        img = cv2.imread(name,-1)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            landmarks = predictor(roi_gray, dlib.rectangle(0, 0, w, h))

            left_eye = landmarks.part(36)
            right_eye = landmarks.part(45)
            eye_distance_x = right_eye.x - left_eye.x

            if eye_distance_x > 10:
                gray_face = roi_gray[y:y + h, x:x + w]
                print(str(gray_face))
                confidence = 110
                if np.size(gray_face) > 0:
                    
                    label, confidence = self.recognizer.predict(gray_face)
                    print(confidence)

                if confidence < 100:
                    print("Door Open")
                    cap.release()
                    cv2.destroyAllWindows()
                    if os.path.exists("face_recognition_model.yml"):
                        shutil.rmtree("face_recognition_model.yml")
                    cv2.destroyAllWindows()
                    return True
                else:
                    print("Unknown person")
            else:
                print("Security checks fail")
        cv2.destroyAllWindows()
        return False


if __name__ == "__main__":
    firebase = pyrebase.initialize_app(config.pirebaseConfig)
    db = firebase.database()
    storage = firebase.storage()
    auth=firebase.auth()
    face_recognition = FaceRecognition(storage, auth, db)
    # face_recognition.capture_photos("aaa")
    for _ in range(25):
        face_recognition.web_cam_single_photo("a"+str(_))
        print(face_recognition.verify_photo("a"+str(_)+"0.png"))
        time.sleep(0.5)
    action = "register"#input("Enter 'register' to register faces or 'recognize' for recognition: ")

    # if action == "register":
    #     name = input("Enter the name: ")
    #     last_name = input("Enter the last name: ")
    #     apartment_number = input("Enter the apartment number: ")
    #     face_recognition.register_faces(name, last_name, apartment_number)
    # elif action == "recognize":
    #     face_recognition.recognize_faces()
    # elif action == "delete":
    #     name = input("Enter the name: ")
    #     last_name = input("Enter the last name: ")
    #     apartment_number = input("Enter the apartment number: ")
    #     face_recognition.delete_person(name, last_name, apartment_number)