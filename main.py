#! python3.8

#=================================================================================
# DIAPASON - A grand swelling burst of harmony; just octave in Pythagorean tuning
# A music media player for Windows
# Programmer: Brandon "bearheathen" Stewart
# June 2020
#=================================================================================

#========
# Imports
#========

from tkinter import *
from pygame import mixer

#=============
# FUNCTIONS
# ===========

def play_music():
    mixer.music.load("assets/chant.mp3")
    mixer.music.play()
    print('Playing.')

def stop_music():
    mixer.music.stop()
    print('Stopped.')

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume) # <-- This function takes float value from 0 to 1
    print("Volume set to: ", val)


# MAIN
#============
root = Tk()


# Initialize Pygame Mixer class for audio playback
mixer.init()

root.geometry('600x400')
root.title("Diapason")
root.iconbitmap(r'assets/diapason.ico')

# Load images for Tkinter to use
playImg = PhotoImage(file='assets/play.png')
stopImg = PhotoImage(file='assets/stop.png')

# Main Screen background.
bckgImg = PhotoImage(file='assets/monk1.png') 
text = Label(root, text = 'Make a joyful noise!')
text.pack()

# Play Button
btnPlay = Button(root, image = playImg, command=play_music)
btnPlay.pack()

# Stop Button
btnStop = Button(root, image=stopImg, comman=stop_music)
btnStop.pack()

# Volume Scale
scale = Scale(root,from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(70) # Set default volume
scale.pack()

root.mainloop()