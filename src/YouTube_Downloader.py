#----------------------------------#
#       YOUTUBE DOWNLOADER         #
#----------------------------------#
#   Author: Alessandro Di Bernardo #
#   GitHub: Ale2328                #
#   Date: 11/01/2023               #
#----------------------------------#
#Hi From vscode.dev
#IMPORTS
from cgitb import text
from msilib.schema import Directory
from re import X
from tkinter import StringVar, ttk
import tkinter as tk
from tkinter.font import BOLD
from tkinter import filedialog, messagebox
from turtle import color
from PIL import ImageTk
from pytube import YouTube

#CONTROL_FORMAT
def control_format():
    if format_combobox.get() == 'mp3':
        download_audio()
    else:
        download_video()

#DOWNLOAD_VIDEO
def download_video():

    #Choose directory
    directory = filedialog.askdirectory(initialdir = "/",title = "Where you want to save?")
    
    try:
        #Get input from textbox
        url = textbox.get()
        yt = YouTube(url)

        #Download video
        yt.streams.get_highest_resolution().download(directory)
    
        messagebox.showinfo("Success", "Video Downloaded Successfully")

        if textbox.get() != None:
            textbox.delete(0, 'end')
        
    except:
        messagebox.showerror("Error", "Invalid URL")
        if textbox.get() != None:
            textbox.delete(0, 'end')


#DOWNLOAD_AUDIO
def download_audio():

    #Choose directory
    directory = filedialog.askdirectory(initialdir = "/",title = "Where you want to save?")

    try:
        #Get input from textbox
        url = textbox.get()
        yt = YouTube(url)

        #Download audio 
        video = yt.streams.filter(only_audio=True).first()
        video.download(directory)
        
        messagebox.showinfo("Success", "Audio Downloaded Successfully")

        if textbox.get() != None:
            textbox.delete(0, 'end')
        
    except:
        messagebox.showerror("Error", "Invalid URL")
        if textbox.get() != None:
            textbox.delete(0, 'end')

#WINDOW INITIALIZATION
root = tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./icon.png'))
root.title("YouTube Downloader")
root.geometry("500x500")
root.resizable(False, False)

frame = tk.Frame(root).grid(row=0, column=0, sticky="nw")
background = ImageTk.PhotoImage(file="./bg.png")

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
btn = ImageTk.PhotoImage(file="./btn.png")
widget_btn = tk.Button(frame, image=btn, command=control_format, bg="red")
widget_btn.image = btn
widget_btn.place(x=150, y=380)

root.mainloop()




