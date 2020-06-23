#! python3.8

# DIAPASON - A grand swelling burst of harmony; just octave in Pythagorean tuning

from tkinter import *
from pygame import mixer

# FUNCTIONS
# ===========

def play_music():
    mixer.music.load("assets/chant.mp3")
    mixer.music.play()
    print('Make a joyful noise!')

# MAIN
#============
root = Tk()


# Initialize Pygame Mixer class for audio playback
mixer.init()

root.geometry('600x400')
root.title("Diapason")
root.iconbitmap(r'assets/diapason.ico')

playImg = PhotoImage(file='assets/play.png')
lblPlay = Label(root, text="Play")
lblPlay.pack()

# Main Screen background.
bckgImg = PhotoImage(file='assets/monk1.png') 
text = Label(root, text = 'Make a joyful noise!', image = bckgImg)
text.pack()



btnPlay = Button(root, image = playImg, command=play_music)
btnPlay.pack()

root.mainloop()