#!/usr/bin/python

from tkinter import *

import time
from PIL import ImageTk, Image
import os

gui = Tk()

'''gui.geometry("800x800")

c = Canvas(gui ,width=800 ,height=800)

c.pack()

oval = c.create_oval(5,5,60,60,fill='pink')

xd = 5

yd = 10
'''
i = 1
angle = 1
img = ImageTk.PhotoImage(Image.open("images/"+str(angle)+".png"))
panel = Label(gui, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
while True:
  '''c.move(oval,xd,yd)

  p=c.coords(oval)

  if p[3] >= 800 or p[1] <=0:

     yd = -yd

  if p[2] >=800 or p[0] <=0:

     xd = -xd
  '''
  angle = i % 181
  if(angle == 0):
    i += 1
    continue
  
  time.sleep(0.025) 
  i += 1
  path2 = "images/"+str(angle)+".png"
  img2 = ImageTk.PhotoImage(Image.open(path2))
  panel.configure(image=img2)
  panel.image = img2
  gui.update()
gui.title("First title")

#from tkinter import *
from PIL import ImageTk, Image
import os
gui.mainloop()
