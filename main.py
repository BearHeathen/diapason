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
        mixer.music.load(filename)
        mixer.music.play()
        print('Playing.')
    except:
        tkinter.messagebox.showerror('Error Playing', 'Diapason could not find the file. Please try again.')

def stop_music():
    mixer.music.stop()
    print('Stopped.')

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume) # <-- This function takes float value from 0 to 1
    print("Volume set to: ", val)

#========
# MAIN
#========
root = Tk()

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

# Basic window
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
scale.set(70) 
mixer.music.set_volume(0.7) # Set default volume
scale.pack()

root.mainloop()