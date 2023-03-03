# from tkinter import *
# from pygame import mixer

# root = Tk()
# root.geometry("500x300")



# mixer.init()
# mixer.music.load("mp3 player/tomp3.cc - GIGACHAD Theme Song but its Phonk House.mp3")

# def start():
#     mixer.music.play()

# def stop():
#     mixer.music.pause()

# def resume():
#     mixer.music.unpause() 

# Label(root,text="Music Player MP3",activebackground="pink").pack()
# Button(text="start",command=start,height=2).place(x=100,y=100)          
# Button(text="stop",command=stop,height=2).place(x=180,y=100)  
# Button(text="resume",command=resume,height=2).place(x=260,y=100)  
# Button(text="exit",command=quit,height=2).place(x=350,y=100)  

# root.mainloop()

import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600, 400))
mixer.music.load("mp3 player/tomp3.cc - GIGACHAD Theme Song but its Phonk House.mp3")
mixer.music.play()

print("Press 'p' to pause 'r' to resume")
print("Press 'q' to quit")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_r:
                mixer.music.unpause()
            if event.key == pygame.K_q:
                running = False
quit