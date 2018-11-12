#!/usr/bin/python

from tkinter import *

import time
from PIL import ImageTk, Image
import os
def animate():
  gui = Tk()
  interval = 1
  i = 1
  angle = interval
  img = ImageTk.PhotoImage(Image.open("images/0.png"))
  panel = Label(gui, image = img)
  panel.pack(side = "bottom", fill = "both", expand = "yes")
  while True:
    if(angle == 0):
      i += interval
      print(i)
      continue
  
    time.sleep(0.025) 
    i += interval
    angle = i % 180
    path2 = "images/"+str(angle)+".png"
    try:
      img2 = ImageTk.PhotoImage(Image.open(path2))
      panel.configure(image=img2)
      panel.image = img2
      gui.update()
    except:
      print(angle)
      print(angle)
      break
  gui.title("First title")

  gui.mainloop()
