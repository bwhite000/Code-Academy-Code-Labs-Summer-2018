from tkinter import *

### NEW ###
# Install dependency: pip3 install Pillow
from PIL import Image, ImageTk
### NEW ###

root = Tk()

root.title("App")
root.geometry("500x300")

def exit_window():
    exit()

message = Label(root, text="I made a Python app!!")
message.pack(fill=BOTH)

button = Button(root, text="Close Window", command=exit_window)
button.pack()

menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=exit_window)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

### NEW ###
load = Image.open("./res/careertek.png")
render = ImageTk.PhotoImage(load)

img = Label(root, image=render)
img.pack()
### NEW ###

root.mainloop()
