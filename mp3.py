import os
import sys
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
from tkinter import Tk, filedialog

def resource_path(relative_path):
    """Get absolute path to resource, works for PyInstaller and dev script"""
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def play_music(folder, mp3_files, index):
    file_path = os.path.join(folder, mp3_files[index])
    
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return None

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    print(f"\nNow playing: {mp3_files[index]}")
    print("Command: [P]ause, [R]esume, [S]top ,[N]ext, [A]dd song")
    
    while True:
        command = input("> ").upper()
        
        if command == "P":
            pygame.mixer.music.pause()
            print("Paused")
            
        elif command == "R":
            pygame.mixer.music.unpause()
            print("Resume")
            
        elif command == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return None
        
        elif command == "N":
            pygame.mixer.music.stop()
            print("Next song....")
            index  +=1
            if index >= len(mp3_files):
                print("End of Playlist !")
                return None 
            return index 
        
        elif command == "A":
            pygame.mixer.music.stop()
            new_file = select_new_song()
            if new_file:
                mp3_files.append(os.path.basename(new_file))
                print(f"Added: {os.path.basename(new_file)}")
                return index
        else:
            print("Invalid command")
def select_new_song():
    """Open a file dialog to select a new MP3 song"""
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="select MP3 file", filetypes=[("MP3 files","*.mp3")])
    if file_path:
        #  copy the  song to the music folder 
        folder = resource_path("music_file")
        os.makedirs(folder, exist_ok=True)
        import shutil
        dest_path = os.path.join(folder, os.path.basename(file_path))
        shutil.copy(file_path, dest_path)
        return dest_path
    return None

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed:", e)
        return 
    
    folder = resource_path("music_file")  # Dynamic path to music
    os.makedirs(folder, exist_ok=True)
    
    
    while True:
        # Refresh song list each time
        mp3_files = [f for f in os.listdir(folder) if f.endswith(".mp3")]
        if not mp3_files:
            print("No .mp3 files found!")
            return
    
        print("****** MP3 PLAYER By Nikhil tiwari ⬆️ ******")
        print("My Song list:")
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")
        
        choice_input = input("\nEnter the song # to play (or 'Q' to quit): ")
        if choice_input.upper() == "Q":
            print('Goodbye')
            break
        elif choice_input == "A":
            select_new_song()
            continue
        
        if not choice_input.isdigit():
            print("Enter a valid number")
            continue
         
        choice = int(choice_input) - 1
        
        if 0 <= choice < len(mp3_files):
            current_index = choice
            while current_index is not None:
                current_index = play_music(folder, mp3_files, current_index)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
