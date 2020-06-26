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
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog, ttk

from mutagen.mp3 import MP3
from PIL import Image, ImageTk
from pygame import mixer
from ttkthemes import themed_tk as tk

#=============
# FUNCTIONS
# ===========

# Utility functions
global flat_red
flat_red = '#C93C3E'

def strip_filename(filename):
    tmp = os.path.basename(filename)
    nowplaying = os.path.splitext(tmp)[0]
    return nowplaying

def resize_btn_image(path_to_img, x_dim, y_dim):
    original_image = Image.open(path_to_img)
    original_image = original_image.resize((x_dim, y_dim), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(original_image)
    return new_image

def about_us():
    tkinter.messagebox.showinfo('About Diapasaon', '''        A joyfully polyphonous yet reverent music player
        Built using Python and Tkinter
        © bearheathen 2020''')

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    add_to_playlist(filename)
global play_selection
playlist = []
def add_to_playlist(playlist_filename):
    playlist_filename = strip_filename(playlist_filename)
    index = 0
    lboxPlaylist.insert(index, playlist_filename)
    playlist.insert(index, filename) # gets the whole file+path
    lboxPlaylist.pack()
    index += 1

def show_details(name_of_file):

    # Get the extension
    file_data = os.path.splitext(filename)[1]
    # Is it an mp3 or wav, ogg, etc?
    if file_data == '.mp3':
        audio = MP3(filename)
        total_length = audio.info.length
    else:
        a = mixer.Sound(name_of_file)
        total_length = a.get_length()

    # divmod - takes mins, divides by 60 and stores remainder in secs
    # total_length / 60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    time_format = '{:02d}:{:02d}'.format(mins, secs)
    lblLength['text'] = time_format  

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()

def start_count(length):
    current_time=0
    while(current_time <= length and mixer.music.get_busy()):
        if is_paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            lblCurrent['text'] = time_format
            time.sleep(1)
            current_time += 1

def remove_item():
    selected_song = lboxPlaylist.curselection()
    selected_song = int(selected_song[0])
    lboxPlaylist.delete(selected_song)
    playlist.pop(selected_song)
    print(playlist)

# Player Functions
is_paused = False
def play_music():
    global is_paused
    if is_paused:
        mixer.music.unpause()
        selected_song = lboxPlaylist.curselection()
        selected_song = int(selected_song[0])
        play_selection = playlist[selected_song]
        nowplaying = strip_filename(play_selection)
        statusbar['text'] = "Resumed Playing" + ' ' + nowplaying
        is_paused = False
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = lboxPlaylist.curselection()
            selected_song = int(selected_song[0])
            
            play_selection = playlist[selected_song]
            mixer.music.load(play_selection)
            mixer.music.play()
            show_details(play_selection)
            # Show name of playing media in statusbar
            nowplaying = strip_filename(play_selection)
            statusbar['text'] = "Playing" + ' ' + nowplaying
        except:
            tkinter.messagebox.showerror('Error Playing', 'Diapason experienced an error. Please try again.')

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
    selected_song = lboxPlaylist.curselection()
    selected_song = int(selected_song[0])
    play_selection = playlist[selected_song]
    nowplaying = strip_filename(play_selection)
    statusbar['text'] = "Restarted Playback of" + ' ' + nowplaying

def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume) # <-- This function takes float value from 0 to 1
    print("Volume set to: ", val)

muted = False
def mute_audio():
    global muted
    if muted: # Unmute music
        set_vol(70)
        muted = False
        btnMute.configure(image=volumeImg)
        scale.set(70)

    else: # mute music
        set_vol(0)
        btnMute.configure(image=mutedImg)
        scale.set(0)
        muted = True

def on_close():
    tkinter.messagebox.showinfo('Shutdown', 'Shutting down...')
    stop_music()
    root.destroy()

#========
# MAIN
#========

# Window layout and setup
# Layout setup
root = tk.ThemedTk()
root.get_themes()
root.set_theme("equilux", themebg=True )

# Status Bar
statusbar = ttk.Label(root, text='Welcome to Diapason', anchor=W, font="Helvetica 16 bold")
statusbar.pack(side=BOTTOM, fill=X)

# Basic window
root.title("Diapason")
root.iconbitmap(r'assets/diapason.ico')

# Left/Right Frames
left_frame = ttk.Frame(root)
left_frame.pack(side=LEFT, padx=30)

right_frame = ttk.Frame(root)
right_frame.pack()

# Top Frame
top_frame = ttk.Frame(right_frame)
top_frame.pack(side=TOP)

# Bottom Frame
bottom_frame = ttk.Frame(right_frame)
bottom_frame.pack(side=BOTTOM)

# Middle Frame
middle_frame = ttk.Frame(right_frame)
middle_frame.pack(padx=30, pady=30)

# Top Menubar
menubar = Menu(root, font="Helvetica 10")
root.config(menu=menubar)

# Top Menubar Submenus

# File Heading
sub_menu = Menu(menubar, tearoff=0, font="Helvetica 10")
menubar.add_cascade(label="File", menu=sub_menu, font="Helvetica 10")
sub_menu.add_command(label="Open", command=browse_file, font="Helvetica 10")
sub_menu.add_command(label="Exit", command=root.destroy, font="Helvetica 10")

# Help Heading
sub_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=sub_menu, font="Helvetica 10")
sub_menu.add_command(label="About", command=about_us, font="Helvetica 10")

# Show media length
lblLength = ttk.Label(top_frame, text = "Total Length: --:--", font="Helvetica 10")
lblLength.pack()

# Show current play time
lblCurrent = ttk.Label(top_frame, text="Current Time: --:--", font="Helvetica 10 bold")
lblCurrent.pack()

# Initialize Pygame Mixer class for audio playback
mixer.init()



# Playlist Listbox
lboxPlaylist = Listbox(left_frame, font="Helvetica 9 bold", bg=flat_red, relief=FLAT, fg="#f0f0f0")
lboxPlaylist.pack()

# Pause Button
pauseImg = resize_btn_image('assets/pause.png', 50, 50)
btnPause = ttk.Button(middle_frame, image=pauseImg, command=pause_music)
btnPause.grid(row=1, column=0)

# Play Button
playImg = PhotoImage(file='assets/play.png')
btnPlay = ttk.Button(middle_frame, image = playImg, command=play_music)
btnPlay.grid(row=1, column=1)

# Add Song Button
addImg = resize_btn_image('assets/add.png', 32, 32)
btnAdd = ttk.Button(left_frame, image=addImg, command=browse_file)
btnAdd.pack(side=LEFT)

# Remove Song Button
removeImg = resize_btn_image('assets/remove.png', 32, 32)
btnRemove = ttk.Button(left_frame, image=removeImg, command=remove_item)
btnRemove.pack(side=LEFT)

# Stop Button
stopImg = resize_btn_image('assets/stop.png', 50, 50)
btnStop = ttk.Button(middle_frame, image=stopImg, command=stop_music)
btnStop.grid(row=1, column=2)

# Rewind Button
rewindImg = resize_btn_image('assets/rewind.png', 35, 35)
btnRewind = ttk.Button(bottom_frame, image=rewindImg, command=rewind_music)
btnRewind.grid(row=0, column=0, pady=20)

# Mute button
volumeImg = resize_btn_image('assets/volume.png', 35, 35)
mutedImg = resize_btn_image('assets/muteVolume.png', 35, 35)
btnMute = ttk.Button(bottom_frame, image=volumeImg, command=mute_audio)
btnMute.grid(row=0, column=1)

# Volume Scale
scale = ttk.Scale(bottom_frame,from_=0, to=100, orient=HORIZONTAL, length=250, command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7) # Set default volume
scale.grid(row=0, column=2, padx=15)



root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
