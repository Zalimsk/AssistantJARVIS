import os
import librosa
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def extract_features(file_path):
    y, sr = librosa.load(file_path)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).T, axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr).T, axis=0)
    mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr).T, axis=0)
    return np.hstack((mfcc, chroma, mel))

def create_dataset(directory):
    features = []
    labels = []
    
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            file_path = os.path.join(directory, file)
            label = file.split('_')[0]  # Assuming filename format "chord_label.wav"
            feature = extract_features(file_path)
            features.append(feature)
            labels.append(label)
    
    return np.array(features), np.array(labels)

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    
    return model

def recognize_guitar(file_path, model):
    features = extract_features(file_path)
    features = features.reshape(1, -1)  # Reshape for the model
    recognized_chord = model.predict(features)
    return recognized_chord[0]

while True:
    directory = "J:\\Assistant JARVIS\\Add_this\Important Project (AI)\\Room_Alert_Photo"  # Update with your directory
    X, y = create_dataset(directory)
    
    # Train the model
    model = train_model(X, y)
    
    # Recognize a new guitar chord
    new_file_path = "J:\\Assistant JARVIS\\Add_this\\Important Project (AI)\\Room_Alert_Photo\\audio.wav"  # Update with your audio file path
    recognized_chord = recognize_guitar(new_file_path, model)
    
    speak(f"The recognized guitar chord is: {recognized_chord}.")
    print(f"Recognized Chord: {recognized_chord}")