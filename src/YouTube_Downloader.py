#------------------------------------#
#       YOUTUBE DOWNLOADER           #
#------------------------------------#
#   Author: Alessandro Di Bernardo   #
#   Co-author: Michele Pagano        #
#   GitHub: Ale2328, AlmondFlame1287 #
#   Date: 11/01/2023                 #
#------------------------------------#
#Hi From vscode.dev
#IMPORTS
from tkinter import StringVar, ttk
import tkinter as tk
from PIL import ImageTk
from Downloader import download

#CONTROL_FORMAT
def control_format():
    if format_combobox.get() == 'mp3':
        download(True, textbox)
    else:
        download(False, textbox)

#WINDOW INITIALIZATION
root = tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='imgs/icon.png'))
root.title("YouTube Downloader")
root.geometry("500x500")
root.resizable(False, False)

frame = tk.Frame(root).grid(row=0, column=0, sticky="nw")
background = ImageTk.PhotoImage(file="imgs/bg.png")

#BACKGROUND
global widget_background
widget_background = tk.Label(frame, image=background)
widget_background.image = background
widget_background.grid(row=0, column=0, sticky="nw")

#TEXTBOX
textbox = tk.Entry(frame, width=25, font=("Arial", 15), bd=0)
textbox.place(x=110, y=310)

#COMBOBOX
format_selected = StringVar()
format_combobox = ttk.Combobox(root, textvariable=format_selected)
format_combobox.grid(row=0, column=0,sticky="nw")
format_combobox.place(x=180,y=340)
format_combobox['values'] = ["mp4","mp3"]
format_combobox['state'] = 'readonly'

#DOWNLOAD_BUTTON
btn = ImageTk.PhotoImage(file="imgs/btn.png")
widget_btn = tk.Button(frame, image=btn, command=control_format, bg="red")
widget_btn.image = btn
widget_btn.place(x=150, y=380)

root.mainloop()




