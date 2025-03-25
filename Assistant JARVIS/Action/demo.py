import configparser
import sys
import numpy as np
import os
import argparse
import pygame
import pyaudio
import numpy as np
import scipy.signal as signal
import random
import argparse
import configparser
import scipy.signal as signal

def detect_clap(data):
    audio_data = np.frombuffer(data, dtype=np.int16)
    # Apply a bandpass filter to focus on the frequency range of claps
    b, a = signal.butter(4, [300, 3000], btype='band', fs=sample_rate)
    filtered_data = signal.filtfilt(b, a, audio_data)
    # Use FFT to analyze the frequency domain
    fft_data = np.abs(np.fft.fft(filtered_data))
    # Check if the amplitude in the frequency domain exceeds a certain threshold
    return np.max(fft_data) > threshold






def get_args():
    parser = argparse.ArgumentParser(description='Clap to play music script.')
    parser.add_argument('--threshold', type=int, default=1000, help='Threshold for clap detection.')
    return parser.parse_args()

args = get_args()
threshold = args.threshold



def play_feedback_sound():
    feedback_sound = pygame.mixer.Sound('feedback.wav')  # Replace with your feedback sound file
    feedback_sound.play()

# Example usage in the main loop
    if detect_clap(data):
        play_feedback_sound()
        print("Clap detected! Playing music...")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        print("Music stopped. Listening for next clap...")




    try:
        pygame.mixer.music.load("H:\\Songs")
    except pygame.error as e:
        print(f"Error loading music file: {e}")
        exit()

    try:
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)
    except IOError as e:
        print(f"Error accessing microphone: {e}")
        exit()



playlist = ['song1.mp3', 'song2.mp3', 'song3.mp3']  # List of songs

def play_random_song():
    song = random.choice(playlist)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# In the main loop, replace `pygame.mixer.music.play()` with `play_random_song()`
    if detect_clap(data):
        play_feedback_sound()
        print("Clap detected! Playing random song...")
        play_random_song()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        print("Song stopped. Listening for next clap...")




    if sys.platform.startswith('win'):
        # Windows-specific code
        pass
    elif sys.platform.startswith('linux'):
        # Linux-specific code
        pass
    elif sys.platform.startswith('darwin'):
        # macOS-specific code
        pass
    else:
        print("Unsupported operating system.")
        exit()



config = configparser.ConfigParser()
config.read('config.ini')

music_file = config.get('Settings', 'music_file')
threshold = config.getint('Settings', 'threshold')

# Example config.ini file content:
# [Settings]
# music_file = song.mp3
# threshold = 1000




# Initialize pygame
pygame.init()

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
music_files = config.get('Settings', 'music_files').split(',')
threshold = config.getint('Settings', 'threshold')
feedback_sound_path = config.get('Settings', 'feedback_sound')

# Load music files and feedback sound
feedback_sound = pygame.mixer.Sound(feedback_sound_path)

# Initialize PyAudio
chunk = 1024
sample_rate = 44100

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                input=True,
                frames_per_buffer=chunk)

def detect_clap(data):
    audio_data = np.frombuffer(data, dtype=np.int16)
    b, a = signal.butter(4, [300, 3000], btype='band', fs=sample_rate)
    filtered_data = signal.filtfilt(b, a, audio_data)
    fft_data = np.abs(np.fft.fft(filtered_data))
    return np.max(fft_data) > threshold

def play_random_song():
    song = random.choice(music_files)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def play_feedback_sound():
    feedback_sound.play()

print("Listening for claps...")

while True:
    data = stream.read(chunk)
    if detect_clap(data):
        play_feedback_sound()
        print("Clap detected! Playing random song...")
        play_random_song()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        print("Song stopped. Listening for next clap...")

# Cleanup
stream.stop_stream()
stream.close()
p.terminate()
