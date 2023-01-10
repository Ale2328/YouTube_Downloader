from cgitb import text
from msilib.schema import Directory
from re import X
import tkinter as tk
from tkinter.font import BOLD
from tkinter import filedialog, messagebox
from turtle import color
from PIL import ImageTk
from pytube import YouTube

def download_video():
    try:
        
        directory = "./video"
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

root = tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.png'))
root.title("YouTube Downloader")
root.geometry("500x500")
root.resizable(False, False)

frame = tk.Frame(root).grid(row=0, column=0, sticky="nw")
background = ImageTk.PhotoImage(file="bg.png")

global widget_background
widget_background = tk.Label(frame, image=background)
widget_background.image = background
widget_background.grid(row=0, column=0, sticky="nw")

textbox = tk.Entry(frame, width=25, font=("Arial", 15), bd=0)
textbox.place(x=110, y=310)

btn = ImageTk.PhotoImage(file="btn.png")
widget_btn = tk.Button(frame, image=btn, command=download_video, bg="red")
widget_btn.image = btn
widget_btn.place(x=150, y=380)

root.mainloop()




