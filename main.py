# modules
import tkinter as ttk
import ttkbootstrap as ttb
from ttkbootstrap import Style

def show_hide():
    add_btn_var.get()

    if text_frame.winfo_viewable():
        search_bar_frame.pack(fill='x', padx=15, pady=15)
        text_frame.pack_forget()
        add_btn_var.set("ADD NOTES")
        task_main_frame.pack(fill="both", ipadx=10, ipady=10, padx=10, pady=10, expand=True)
    else:
        text_frame.pack(padx=15, pady=15)
        add_btn_var.set("BACK")
        text_area.delete("1.0", "end")
        task_main_frame.pack_forget()
        search_bar_frame.pack_forget()

def cancel_btn():
    search_bar_frame.pack(fill='x',
                          padx=15,
                          pady=15)
    text_frame.pack_forget()
    add_btn_var.set("ADD NOTES")
    text_area.delete("1.0","end")
    task_main_frame.pack(fill="both",
                         ipadx=10,
                         ipady=10,
                         padx=10,
                         pady=10,
                         expand=True)

def add_task():
    search_bar_frame.pack(fill='x',
                          padx=15,
                          pady=15)
    task_value=text_area.get("1.0", "end-1c")
    # print(task_value)
    task.append(task_value)
    task.reverse()
    print(task)
    text_area.delete("1.0","end")
    text_frame.pack_forget()
    add_btn_var.set("ADD NOTES")
    task_main_frame.pack(fill="both",
                         ipadx=10,
                         ipady=10,
                         padx=10,
                         pady=10,
                         expand=True)


task=[]

# window
window=ttb.Window()
window.geometry('500x800')
window.title("pyWRITE")
window.resizable(False, False)
style=Style(theme="minty")

# main_frame
main_frame=ttb.Frame(window)
main_frame.pack(expand=True, fill='both', ipadx=20, ipady=10)

# header_frame
header_frame=ttb.Frame(main_frame)
header_frame.pack(fill='x', padx=10, pady=10)

# header_title_label
header_title_label=ttb.Label(header_frame, text="PYWRITE", font="Calibre 14 bold")
header_title_label.pack(side="left")

# add_btn
add_btn_var=ttk.StringVar()
add_btn_var.set("ADD NOTES")
add_btn=ttb.Button(header_frame, width=13, style="success", command=show_hide, textvariable=add_btn_var)
add_btn.pack(side="right")

# header_separator
header_separator=ttb.Separator(main_frame, style="default")
header_separator.pack(fill='x')
#

# text_frame
text_frame=ttb.Frame(main_frame)
# text_frame.pack(fill='both') function will pack this

# text_frame_label
text_frame_label=ttb.Label(text_frame, text="ADD NOTES")
text_frame_label.pack()

# text_area
text_area=ttb.Text(text_frame, wrap="word")
text_area.pack()

# text_area_control
text_area_control=ttb.Frame(text_frame)
text_area_control.pack(fill='both', expand=True, padx=5, pady=5)
text_area_control.columnconfigure((0, 1), weight=2)

# save_btn
save_btn=ttb.Button(text_area_control, text="SAVE", style="success", command=add_task)
save_btn.grid(row=0, column=0, sticky="ew")

# cancel_btn
cancel_btn=ttb.Button(text_area_control, text="CANCEL", style="danger", command=cancel_btn)
cancel_btn.grid(row=0, column=1, sticky="ew")

for widget in text_area_control.winfo_children():
    widget.grid_configure(padx=3, pady=3)


# search_bar_frame
search_bar_frame=ttb.Frame(main_frame)
search_bar_frame.pack(fill='x', padx=15, pady=15)

# search_bar
search_bar=ttb.Entry(search_bar_frame)
search_bar.insert(0, "Search")
search_bar.bind("<FocusIn>", lambda e: search_bar.delete('0', 'end'))
search_bar.pack(fill='x')


# task_main_frame
task_main_frame=ttb.Frame(main_frame, height=10)
task_main_frame.pack(fill="x", padx=15)

# task_content_frame
task_content_frame=ttb.Frame(task_main_frame)
task_content_frame.pack(fill='x', padx=10, pady=10)

# task_label
task_label=ttb.Label(task_content_frame, text="Note 1", font="Calibre, 12 bold")
task_label.pack(fill='x', pady=4)

# task_sub_label
task_sub_label=ttb.Label(task_content_frame, text="11, October", font="Calibre 9", style="secondary")
task_sub_label.pack(fill='x', pady=4)

# task_content
task_content=ttb.Label(task_content_frame,
                       text="Hello World",
                       font="Calibre 10")
task_content.pack(fill='x', pady=4)

# task_separator
task_separator=ttb.Separator(task_content_frame, style="success")
task_separator.pack(fill='x', pady=20)


# run
window.mainloop()