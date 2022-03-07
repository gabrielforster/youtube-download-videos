from tkinter import *

root = Tk()

root.geometry("400x300")
root.title("Youtube Download Videos")
root['bg'] = '#ffbf00'

urlInput = Entry(root, width=50)
urlInput.pack(pady=30)
urlInput.get()

def getLink():
    url = 'Testando ' + urlInput.get()
    Label(root,
    text=url,
    bg="#ffbf00",
    pady=7.5).pack()

downloadButton = Button(root,
                        text="Download the video!", 
                        command=getLink,
                        padx=10,
                        pady=5).pack()

root.mainloop()