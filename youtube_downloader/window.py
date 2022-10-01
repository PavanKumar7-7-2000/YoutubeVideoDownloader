from urllib.request import urlopen
from PIL import ImageTk

from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff')
#Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff')
#add to canvas
canvas.create_window(250, 390, window=download_btn)


image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a0/Bill_Gates_2018.jpg"

data = urlopen(image_url)
image = ImageTk.PhotoImage(data=data.read())
Label(screen, image=image).pack()

screen.mainloop()