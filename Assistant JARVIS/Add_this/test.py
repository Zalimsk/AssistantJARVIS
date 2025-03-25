import os
import random
import threading
import time
from playsound import playsound
import speech_recognition as sr
from pydub import AudioSegment
import simpleaudio as sa

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.songs = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
        self.is_playing = False
        self.current_song = None
        self.paused = False
        self.play_thread = None

    def play_music(self):
        while True:
            if not self.paused:
                if not self.songs:
                    print("No MP3 files found in the specified directory.")
                    return

                self.current_song = random.choice(self.songs)
                song_path = os.path.join(self.music_folder, self.current_song)
                print(f"Now playing: {self.current_song}")

                # Load and play the song
                song = AudioSegment.from_mp3(song_path)
                play_obj = sa.play_buffer(song.raw_data, num_channels=song.channels, 
                                          bytes_per_sample=song.sample_width, 
                                          sample_rate=song.frame_rate)

                self.is_playing = True
                play_obj.wait_done()  # Wait until the song is finished playing

            time.sleep(1)

    def pause_music(self):
        self.paused = True
        print("Music paused.")

    def resume_music(self):
        self.paused = False
        print("Resuming music.")

    def stop_music(self):
        print("Stopping the music.")
        self.is_playing = False
        if self.play_thread:
            self.play_thread.join()  # Wait for the music thread to finish

    def next_song(self):
        print("Playing next song.")

    def previous_song(self):
        if self.current_song:
            print(f"Playing previous song: {self.current_song}")
        else:
            print("No previous song available.")

def listen_for_commands(player):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        while True:
            print("Listening for commands...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                command = input(":>")
                #command = recognizer.recognize_google(audio).lower()
                print(f"Command received: {command}")

                if "stop" in command:
                    player.stop_music()
                    break  # Stop listening for commands

                elif "next" in command:
                    player.next_song()

                elif "previous" in command:
                    player.previous_song()

                elif "pause" in command:
                    player.pause_music()

                elif "resume" in command:
                    player.resume_music()

            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    music_folder = "H:\\download"
    player = MusicPlayer(music_folder)

    # Start music playback in a separate thread
    player.play_thread = threading.Thread(target=player.play_music)
    player.play_thread.start()

    # Start listening for commands
    listen_for_commands(player)
