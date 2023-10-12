# modules
import tkinter as ttk
import ttkbootstrap as ttb
from ttkbootstrap import Style

# window
window=ttb.Window()
window.geometry('500x800')
window.title("To-Do List")
style=Style()

# main_frame
main_frame=ttb.Frame(window)
main_frame.pack(expand=True, fill='x', ipadx=10, ipady=10)

# run
window.mainloop()