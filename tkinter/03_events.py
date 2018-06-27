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

root.mainloop()
