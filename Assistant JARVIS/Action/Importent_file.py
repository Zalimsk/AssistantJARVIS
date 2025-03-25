import os
import pygame
import random
import configparser
import logging
import numpy as np
import scipy.signal as signal
import pyaudio
from pygame import mixer

# Configure logging
logging.basicConfig(filename='app.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Default configuration parameters
DEFAULT_CONFIG = {
    'Settings': {
        'music_folder_path': 'H:\\Songs',
        'required_claps': '3'
    }
}

def load_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    if os.path.isfile(config_file):
        config.read(config_file)
    else:
        # Create a default config file if not present
        config.read_dict(DEFAULT_CONFIG)
        with open(config_file, 'w') as f:
            config.write(f)
    return config

def play_random_music(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    music_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3', '.wav', '.ogg', '.flac'))]

    if not music_files:
        print("No music files found in the specified folder.")
        return

    selected_music = random.choice(music_files)
    music_path = os.path.join(folder_path, selected_music)

    try:
        pygame.init()
        mixer.init()
        mixer.music.load(music_path)
        mixer.music.play()
        print(f"Playing: {selected_music}")

        return selected_music

    except Exception as e:
        logging.error(f"Error playing music: {e}")

def stop_music():
    try:
        mixer.music.stop()
        print("Music stopped.")
    except Exception as e:
        logging.error(f"Error stopping music: {e}")

def pause_music():
    try:
        mixer.music.pause()
        print("Music paused.")
    except Exception as e:
        logging.error(f"Error pausing music: {e}")

def unpause_music():
    try:
        mixer.music.unpause()
        print("Music resumed.")
    except Exception as e:
        logging.error(f"Error resuming music: {e}")

def play_feedback_sound():
    feedback_sound_path = 'feedback.wav'
    try:
        feedback_sound = mixer.Sound(feedback_sound_path)
        feedback_sound.play()
    except Exception as e:
        logging.error(f"Error playing feedback sound: {e}")

# Clap Detection Class
class TapTester:
    def __init__(self):
        self.chunk = 1024
        self.sample_rate = 44100
        self.threshold = 1000  # Default threshold
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.sample_rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
    
    def detect_clap(self, data):
        audio_data = np.frombuffer(data, dtype=np.int16)
        b, a = signal.butter(4, [300, 3000], btype='band', fs=self.sample_rate)
        filtered_data = signal.filtfilt(b, a, audio_data)
        fft_data = np.abs(np.fft.fft(filtered_data))
        return np.max(fft_data) > self.threshold
    
    def listen(self):
        data = self.stream.read(self.chunk)
        return self.detect_clap(data)

def manual_control():
    config = load_config()
    music_folder_path = config.get('Settings', 'music_folder_path')
    required_claps = config.getint('Settings', 'required_claps')
    
    tt = TapTester()
    is_playing = False
    is_paused = False
    clap_count = 0
    current_track = None
    
    print("Commands: ")
    print("  'play' - Play a random track")
    print("  'pause' - Pause the current track")
    print("  'resume' - Resume the current track")
    print("  'stop' - Stop the current track")
    print("  'next' - Skip to the next track")
    print("  'quit' - Quit the program")

    while True:
        user_input = input("Enter command: ").strip().lower()

        if user_input == 'quit':
            stop_music()
            break
        elif user_input == 'play':
            if not is_playing:
                current_track = play_random_music(music_folder_path)
                is_playing = True
                is_paused = False
            else:
                print("Music is already playing.")
        elif user_input == 'pause':
            if is_playing and not is_paused:
                pause_music()
                is_paused = True
            elif is_paused:
                print("Music is already paused.")
            else:
                print("No music is playing.")
        elif user_input == 'resume':
            if is_paused:
                unpause_music()
                is_paused = False
            elif is_playing:
                print("Music is already playing.")
            else:
                print("No music to resume.")
        elif user_input == 'stop':
            if is_playing:
                stop_music()
                is_playing = False
                is_paused = False
            else:
                print("No music is playing.")
        elif user_input == 'next':
            if is_playing:
                stop_music()
                current_track = play_random_music(music_folder_path)
            else:
                print("No music is playing.")
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    # Start manual control
    manual_control()
