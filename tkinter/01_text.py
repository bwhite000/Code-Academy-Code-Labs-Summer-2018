from tkinter import *

root = Tk()

root.title("App")
root.geometry("500x300")

message = Label(root, text="I made a Python app!!")
message.pack(fill=BOTH)

root.mainloop()
