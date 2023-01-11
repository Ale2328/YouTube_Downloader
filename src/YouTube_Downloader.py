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

def control_format():
    if format_combobox.get() == 'mp3':
        download_audio()
    else:
        download_video()

def download_video():
    print("mp4")
    directory = filedialog.askdirectory(initialdir = "/",title = "Where you want to save?")
    
    try:
        

        url = textbox.get()
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(directory)
        
        messagebox.showinfo("Success", "Video Downloaded Successfully")

        if textbox.get() != None:
            textbox.delete(0, 'end')
        
    except:
        messagebox.showerror("Error", "Invalid URL")
        if textbox.get() != None:
            textbox.delete(0, 'end')


def download_audio():
    
    directory = filedialog.askdirectory(initialdir = "/",title = "Where you want to save?")

    try:
        
        url = textbox.get()
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(directory)
        
        messagebox.showinfo("Success", "Audio Downloaded Successfully")

        if textbox.get() != None:
            textbox.delete(0, 'end')
        
    except:
        messagebox.showerror("Error", "Invalid URL")
        if textbox.get() != None:
            textbox.delete(0, 'end')

    





root = tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./icon.png'))
root.title("YouTube Downloader")
root.geometry("500x500")
root.resizable(False, False)

frame = tk.Frame(root).grid(row=0, column=0, sticky="nw")
background = ImageTk.PhotoImage(file="./bg.png")

global widget_background
widget_background = tk.Label(frame, image=background)
widget_background.image = background
widget_background.grid(row=0, column=0, sticky="nw")

textbox = tk.Entry(frame, width=25, font=("Arial", 15), bd=0)
textbox.place(x=110, y=310)

btn = ImageTk.PhotoImage(file="./btn.png")

format_selected = StringVar()
format_combobox = ttk.Combobox(root, textvariable=format_selected)

format_combobox.grid(row=0, column=0,sticky="nw")
format_combobox.place(x=180,y=340)
format_combobox['values'] = ["mp4","mp3"]
format_combobox['state'] = 'readonly'





widget_btn = tk.Button(frame, image=btn, command=control_format, bg="red")
widget_btn.image = btn
widget_btn.place(x=150, y=380)

root.mainloop()




