import tkinter as tk
from tkinter import filedialog, Text 
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=1000, bg="#99ccff")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.2, relheight=0.2)

root.mainloop()