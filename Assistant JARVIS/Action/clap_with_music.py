import os
import random
import pygame
import tkinter as tk
from tkinter import filedialog
import threading

# Initialize Pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.current_track = None
        self.is_paused = False
        self.music_files = []

        # GUI Elements
        self.play_button = tk.Button(root, text="Play", command=self.play_random_music)
        self.play_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack()

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack()

        self.resume_button = tk.Button(root, text="Resume", command=self.resume_music)
        self.resume_button.pack()

        self.volume_label = tk.Label(root, text="Volume (0.0 - 1.0):")
        self.volume_label.pack()

        self.volume_scale = tk.Scale(root, from_=0.0, to=1.0, orient=tk.HORIZONTAL, resolution=0.1, command=self.set_volume)
        self.volume_scale.pack()

        self.load_button = tk.Button(root, text="Load Music", command=self.load_music)
        self.load_button.pack()

        self.status_label = tk.Label(root, text="Status: Idle")
        self.status_label.pack()

    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("H:\\Songs", "*.mp3 *.wav")])
        self.music_files = list(files)
        self.status_label.config(text=f"Loaded {len(self.music_files)} files.")

    def play_music(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.current_track = file_path
            self.is_paused = False
            self.status_label.config(text=f"Playing: {os.path.basename(file_path)}")
        except pygame.error as e:
            self.status_label.config(text=f"Error: {e}")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None
        self.is_paused = False
        self.status_label.config(text="Playback stopped.")

    def pause_music(self):
        if pygame.mixer.music.get_busy() and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.status_label.config(text="Playback paused.")

    def resume_music(self):
        if pygame.mixer.music.get_busy() and self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.status_label.config(text="Playback resumed.")

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))
        self.status_label.config(text=f"Volume set to {volume}")

    def play_random_music(self):
        if not self.music_files:
            self.status_label.config(text="No music files loaded.")
            return
        
        music_file = random.choice(self.music_files)
        self.play_music(music_file)

    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    player = MusicPlayer(root)
    
    # Run the GUI in a separate thread to keep it responsive
    gui_thread = threading.Thread(target=player.run)
    gui_thread.start()
