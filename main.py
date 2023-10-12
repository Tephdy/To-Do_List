# modules
import tkinter as ttk
import ttkbootstrap as ttb
from ttkbootstrap import Style

# window
window=ttb.Window()
window.geometry('500x800')
window.title("To-Do List")
window.resizable(False, False)
style=Style()

# main_frame
main_frame=ttb.Frame(window)
main_frame.pack(expand=True, fill='both', ipadx=10, ipady=10)

# header_frame
header_frame=ttb.Frame(main_frame)
header_frame.pack(fill='x', padx=10, pady=10)

# header_title_label
header_title_label=ttb.Label(header_frame, text="To-Do List", font="Calibre 14 bold")
header_title_label.pack(side="left")

# # add icon
# add_icon=ttk.PhotoImage(file="icons/plus-square-fill.png")
# plus_icon=ttb.Label(header_frame, text="Add")
# plus_icon.pack(side="right")

# add_btn
add_btn=ttb.Button(header_frame, text="Add", width=10)
add_btn.pack(side="right")

#

# run
window.mainloop()