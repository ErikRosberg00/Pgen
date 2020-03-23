import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
savedPwds = []


def exitButton(self):
    exit()


def openFile():
    filename = filedialog.askopenfilename(initialdi="/", title="Select File",
                                          filetypes=(("txt", "*.txt"), ("all files", "*.*")))
    savedPwds.append(filename)
    print(filename)
    for savedPwd in savedPwds:
        passwordShowcase = tk.Label(showcase, text=savedPwd, bg="white")
        passwordShowcase.pack()

background = tk.Canvas(root, height=500, width=1000, bg="#99ccff")
background.pack()

showcase = tk.Frame(root, bg="#7575a3")
showcase.place(relwidth=0.8, relheight=0.8, y=30, x=100)

exitButton = tk.Button(root, text="Exit", padx=5, command=exitButton)
exitButton.place(x=0, y=0)

fileBtn = tk.Button(root, text="file", padx=5, command=openFile)
fileBtn.place(x=30, y=0)

rndPwd = tk.Button(root, text="Random password", padx=5)
rndPwd.place(x=60, y=0)

root.mainloop()
