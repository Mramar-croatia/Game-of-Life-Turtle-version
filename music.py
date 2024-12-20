import pygame
import threading
import time

# Folder where the music files are stored
MUSIC_FOLDER = "./Music/"

# List of music files to play
MUSIC_LIST = ["Bella.mp3", "Katyusha.mp3", "Marsal.mp3", "Bandiera.mp3", "Kalinka.mp3"]

# Global variable to keep track of whether the music is paused
is_paused = False


# Function to play music from the list
def play_music():
    
    global is_paused
    index = 0
    
    while True:
        
        pygame.mixer.music.load(MUSIC_FOLDER + MUSIC_LIST[index])
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            
            if is_paused:
                pygame.mixer.music.pause()
                
            time.sleep(1)
            
        index = (index + 1) % len(MUSIC_LIST)  # Move to the next track and loop back


# Class to manage the music player
class MusicPlayer:
    
    def __init__(self):
        
        pygame.init()
        pygame.mixer.init()

        # Music will be played in a separate thread (Chat GPT - How does this work?)
        music_thread = threading.Thread(target=play_music, daemon=True)
        music_thread.start()


    # Function to pause the music
    def pause(self):
        
        global is_paused
        
        is_paused = True
        pygame.mixer.music.pause()


    # Function to unpause the music
    def unpause(self):
        
        global is_paused
        is_paused = False
        pygame.mixer.music.unpause()