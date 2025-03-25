import face_recognition
import cv2
import os
import numpy as np
from playsound import playsound
import threading

# Known faces directory (make sure this points to a folder with images)
known_faces_dir = "J:\\Assistant JARVIS\\Add_this\\Important Project (AI)\\Face_Photo\\"

known_face_encodings = []
known_face_names = []

# Camera URL
CAMERA_URL = "http://192.168.79.51:4747/video"

def load_known_faces():
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
            encodings = face_recognition.face_encodings(image)
            if encodings:  # Check if any face encodings were found
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])  # Filename as name

def alert_unknown_face():
    playsound("J:\\Assistant JARVIS\\Add_this\\Important Project (AI)\\alert.mp3")  # Alert sound file path

def recognize_faces():
    video_capture = cv2.VideoCapture(CAMERA_URL)

    if not video_capture.isOpened():
        print("Error: Unable to access the camera.")
        return

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Unable to read frame from camera.")
            break

        rgb_frame = frame[:, :, ::-1]

        # Face recognition
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            else:
                # Start alert thread if face is unknown
                threading.Thread(target=alert_unknown_face).start()

            # Display results
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow('Video', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    load_known_faces()
    recognize_faces()
