from tkinter import *

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

label = Label(root, text="First name:")
label.pack(anchor="w")

txt = Entry(root, width=100)
txt.pack()

### NEW ###
def read_name():
    name = txt.get()
    namemsg.configure(text="Hello " + name + "!")

namebtn = Button(root, text="Create message", command=read_name)
namebtn.pack()

namemsg = Label(root)
namemsg.pack()
### NEW ###

root.mainloop()
