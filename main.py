#! python3.8

# DIAPASON - A grand swelling burst of harmony; just octave in Pythagorean tuning

from tkinter import *

# FUNCTIONS
# ===========

def play_btn():
    print('Hey, this button works!')

# MAIN
#============
root = Tk()

root.geometry('600x400')
root.title("Diapason")
root.iconbitmap(r'assets/diapason.ico')

text = Label(root, text = 'Let\'s make some noise!')
text.pack()

playImg = PhotoImage(file='assets/play.png')
lblPlay = Label(root, text="Play")
lblPlay.pack()

btnPlay = Button(root, image = playImg, command=play_btn)
btnPlay.pack()

root.mainloop()