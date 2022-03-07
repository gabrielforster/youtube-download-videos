from pytube import YouTube
from tkinter import *

root = Tk()
save_path = '/Downloads'

root.geometry("400x300")
root.title("Youtube Download Videos")
root['bg'] = '#ffbf00'

urlInput = Entry(root, width=50)
urlInput.pack(pady=30)
urlInput.get()


def getLink():
    video = YouTube(urlInput.get())
    videofile = video.streams.get_highest_resolution()
    title = video.title 
    videotext = "(" + title + ")\nIt'll be available at: " + save_path
    Label(root,
    text=videotext,
    bg="#ffbf00",
    pady=7.5).pack()
    videofile.download(save_path)



downloadButton = Button(root,
                        text="Download the video!", 
                        command=getLink,
                        padx=10,
                        pady=5).pack()

root.mainloop()