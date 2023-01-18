from tkinter import filedialog, messagebox
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from os import getenv

def download(audio_only, txtbox):

    #Choose directory
    directory = filedialog.askdirectory(initialdir = getenv("HOME"),title = "Where do you want to save?")

    try:
        #Get input from textbox
        url = txtbox.get()
        yt = YouTube(url)

        #Download audio
        if not audio_only:
            yt.streams.get_highest_resolution().download(directory)
            return

        audio = yt.streams.filter(only_audio=True).first()
        audio.download(directory)
        messagebox.showinfo("Success", "Audio Downloaded Successfully")
    
        if txtbox.get() != None:
            txtbox.delete(0, 'end')
        
    except VideoUnavailable:
        messagebox.showerror("Error", "Invalid URL")
        if txtbox.get() != None:
            txtbox.delete(0, 'end')

    