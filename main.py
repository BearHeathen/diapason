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

import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer


#=============
# FUNCTIONS
# ===========

def about_us():
    tkinter.messagebox.showinfo('About Diapasaon', '''        A joyfully polyphonous yet reverent music player
        Built using Python and Tkinter
        © bearheathen 2020''')

def browse_file():
    global filename
    filename = filedialog.askopenfilename()

def play_music():
    try:
        is_paused # Check if the pause button has been pressed. If it has, skip to "else"
    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            # Show name of playing media in statusbar
            tmp = os.path.basename(filename)
            nowplaying = os.path.splitext(tmp)[0]
            statusbar['text'] = "Playing" + ' ' + nowplaying
        except:
            tkinter.messagebox.showerror('Error Playing', 'Diapason experienced an error. Please try again.')
    else:
        mixer.music.unpause()
        tmp = os.path.basename(filename)
        nowplaying = os.path.splitext(tmp)[0]
        statusbar['text'] = "Resumed Playing" + ' ' + nowplaying

def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Stopped."
    print('Stopped.')

def pause_music():
    global is_paused
    is_paused = True
    mixer.music.pause()
    statusbar['text'] = "Paused."

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume) # <-- This function takes float value from 0 to 1
    print("Volume set to: ", val)

#========
# MAIN
#========

# Window layout and setup
# Layout setup
root = Tk()
middle_frame = Frame(root)
middle_frame.pack(padx=10, pady=50)

# Basic window
root.title("Diapason")
root.iconbitmap(r'assets/diapason.ico')

# Top Menubar
menubar = Menu(root)
root.config(menu=menubar)

# Top Menubar Submenus

# File Heading
sub_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Open", command=browse_file)
sub_menu.add_command(label="Exit", command=root.destroy)

# Help Heading
sub_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=sub_menu)
sub_menu.add_command(label="About", command=about_us)

# Initialize Pygame Mixer class for audio playback
mixer.init()

# Load images for Tkinter to use
playImg = PhotoImage(file='assets/play.png')
stopImg = PhotoImage(file='assets/stop.png')
pauseImg = PhotoImage(file='assets/pause.png')
global flat_red
flat_red = '#C93C3E'
# Main Screen label.
text = Label(root, text = 'Make a joyful noise!')
text.pack(side=TOP)

# Play Button
btnPlay = Button(middle_frame, image = playImg, relief=FLAT, command=play_music)
btnPlay.pack(side=LEFT, padx=10, pady=20)

# Pause Button
btnPause = Button(middle_frame, image=pauseImg, relief=FLAT, command=pause_music)
btnPause.pack(side=LEFT, padx=10, pady=20)

# Stop Button
btnStop = Button(middle_frame, image=stopImg, relief=FLAT,command=stop_music)
btnStop.pack(side=LEFT, padx=10, pady=20)

# Volume Scale
scale = Scale(root,from_=0, to=100, orient=HORIZONTAL, length=250, sliderlength=25, sliderrelief=FLAT, troughcolor=flat_red, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7) # Set default volume
scale.pack(pady=15)

# Status Bar
statusbar = Label(root, text='Welcome to Diapason', anchor=W, bd=10, relief=FLAT)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
