from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("600x300")

mixer.init()
mixer.music.load("mp3 player/tomp3.cc - GIGACHAD Theme Song but its Phonk House.mp3")


def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()


Label(root, text="MP3 MUSIC PLAYER", font="lucidia 30 bold",bg="#66bfbf").pack()
Button(text="START", command=play , background = "green" ,activebackground="pink").place(x=120, y=100)
Button(text="STOP", command=pause,background = "#55ff55",activebackground="pink").place(x=220, y=100)
Button(text="RESUME", command=resume,background = "green",activebackground="pink").place(x=320, y=100)
Button(text="QUIT", command=quit,background = "red",activebackground="pink").place(x=440, y=100)

root.mainloop()