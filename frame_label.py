import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

# Crie um ttk.Frame para adicionar o padding
padding_frame = ttk.Frame(root, padding=15)
padding_frame.pack(fill=X, expand=YES, anchor=N)

option_text = "Label Frame"
option = ttk.Labelframe(padding_frame, text=option_text)
option.pack(fill=X, expand=YES, anchor=N)

b1 = ttk.Button(option, text="Button 1", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(option, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
