import ttkbootstrap as ttk
from ttkbootstrap.constants import *


app = ttk.Window(themename='darkly')
app.grab_set()
app.focus_force()
app.resizable(True,True)
# app.geometry("1600x680+0+0")
app.title('Sem Titulo')

def open_dialog():
    root = ttk.Toplevel(title='Resumo')
    root.mainloop()

open_button = ttk.Button(text='Abrir',bootstyle=PRIMARY,command=open_dialog)
open_button.pack(side=LEFT,pady=10,padx=5)

button_close = ttk.Button(text='Fechar',bootstyle=(INFO,OUTLINE))
button_close.pack(side=RIGHT,pady=10,padx=5)

app.mainloop()