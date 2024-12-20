import pygame
import threading
import time

MUSIC_LIST = ["Bella.mp3", "Katyusha.mp3", "Marsal.mp3", "Bandiera.mp3", "Kalinka.mp3"]
is_paused = False

# Function to play music from the list
def play_music():
    global is_paused
    index = 0
    while True:
        pygame.mixer.music.load("./Music/" + MUSIC_LIST[index])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            if is_paused:
                pygame.mixer.music.pause()
            time.sleep(1)
        index = (index + 1) % len(MUSIC_LIST)  # Move to the next track and loop back

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        # Start playing music in a separate thread to keep the GUI responsive
        music_thread = threading.Thread(target=play_music, daemon=True)
        music_thread.start()

    def pause(self):
        global is_paused
        is_paused = True
        pygame.mixer.music.pause()

    def unpause(self):
        global is_paused
        is_paused = False
        pygame.mixer.music.unpause()

# Usage example:
music_player = MusicPlayer()
# To pause and unpause
music_player.pause()  # Pauses the music
music_player.unpause()  # Unpauses the music