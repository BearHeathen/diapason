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
from PIL import Image, ImageTk


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
            nowplaying = strip_filename(filename)
            statusbar['text'] = "Playing" + ' ' + nowplaying
        except:
            tkinter.messagebox.showerror('Error Playing', 'Diapason experienced an error. Please try again.')
    else:
        mixer.music.unpause()
        nowplaying = strip_filename(filename)
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

def rewind_music():
    play_music()
    current_file = strip_filename(filename)
    statusbar['text'] = "Restarted Playback of" + ' ' + current_file

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume) # <-- This function takes float value from 0 to 1
    print("Volume set to: ", val)

# Utility function for getting just the filename with no path or extension
def strip_filename(filename):
    tmp = os.path.basename(filename)
    nowplaying = os.path.splitext(tmp)[0]
    return nowplaying

def resize_btn_image(path_to_img, x_dim, y_dim):
    original_image = Image.open(path_to_img)
    original_image = original_image.resize((x_dim, y_dim), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(original_image)
    return new_image

muted = False
def mute_audio():
    global muted
    if muted: # Unmute music
        set_vol(70)
        muted = False
        btnMute.configure(image=volumeImg)

    else: # mute music
        set_vol(0)
        btnMute.configure(image=mutedImg)
        muted = True


#========
# MAIN
#========

# Window layout and setup
# Layout setup
root = Tk()
middle_frame = Frame(root)
middle_frame.pack(padx=30, pady=30)

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

global flat_red
flat_red = '#C93C3E'

# Main Screen label.
#text = Label(middle_frame, relief=GROOVE, text = 'Make a joyful noise!')
#text.grid(row=0, column=2)

# Pause Button
pauseImg = resize_btn_image('assets/pause.png', 50, 50)
btnPause = Button(middle_frame, image=pauseImg, relief=FLAT, command=pause_music)
btnPause.grid(row=1, column=0)

# Play Button
playImg = PhotoImage(file='assets/play.png')
btnPlay = Button(middle_frame, image = playImg, relief=FLAT, command=play_music)
btnPlay.grid(row=1, column=1)

# Stop Button
stopImg = resize_btn_image('assets/stop.png', 50, 50)
btnStop = Button(middle_frame, image=stopImg, relief=FLAT,command=stop_music)
btnStop.grid(row=1, column=2)

bottom_frame = Frame(root)
bottom_frame.pack()

# Rewind Button
rewindImg = resize_btn_image('assets/rewind.png', 35, 35)
btnRewind = Button(bottom_frame, image=rewindImg, relief=FLAT,command=rewind_music)
btnRewind.grid(row=0, column=0, pady=20)

# Mute button
volumeImg = resize_btn_image('assets/volume.png', 35, 35)
mutedImg = resize_btn_image('assets/muteVolume.png', 35, 35)
btnMute = Button(bottom_frame, image=volumeImg, relief=FLAT, command=mute_audio)
btnMute.grid(row=0, column=2)

# Volume Scale
scale = Scale(bottom_frame,from_=0, to=100, orient=HORIZONTAL, length=250, sliderlength=25, sliderrelief=FLAT, troughcolor=flat_red, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7) # Set default volume
scale.grid(row=0, column=1, padx=30)

# Status Bar
statusbar = Label(root, text='Welcome to Diapason', anchor=W, bd=10, relief=FLAT)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
