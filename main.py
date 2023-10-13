# modules
import tkinter as ttk
import ttkbootstrap as ttb
from ttkbootstrap import Style
import datetime as user_date

def show_hide():
    add_btn_var.get()

    if text_frame.winfo_viewable():
        search_bar_frame.pack(fill='x', padx=15, pady=15)
        search_bar.insert(0, "Search")
        text_frame.pack_forget()
        add_btn_var.set("ADD NOTES")
        task_main_frame.pack(fill="both", ipadx=10, ipady=10, padx=10, pady=10)
    else:
        search_bar.delete("0", "end")
        text_frame.pack(padx=15, pady=15)
        add_btn_var.set("BACK")
        text_area.delete("1.0", "end")
        task_main_frame.pack_forget()
        search_bar_frame.pack_forget()

def cancel_btn():
    search_bar_frame.pack(fill='x',
                          padx=15,
                          pady=15)
    search_bar.insert(0,"Search")
    text_frame.pack_forget()
    add_btn_var.set("ADD NOTES")
    text_area.delete("1.0","end")
    task_main_frame.pack(fill="both",
                         ipadx=10,
                         ipady=10,
                         padx=10,
                         pady=10)

def add_task():
    search_bar_frame.pack(fill='x',
                          padx=15,
                          pady=15)
    search_bar.insert(0,"Search")
    display_task()
    print(task)
    text_area.delete("1.0","end")
    text_frame.pack_forget()
    add_btn_var.set("ADD NOTES")
    task_main_frame.pack(fill="both",
                         ipadx=20,
                         ipady=20,
                         padx=10,
                         pady=10)

def display_task():
    current_datetime=user_date.datetime.now()
    current_date=current_datetime.date()
    formatted_date=current_date.strftime("%m-%d-%d")

    task_text=text_area.get("1.0", "end-1c")
    task.append(task_text)
    # task.reverse()
    print(task[-1])

    if task_text:
        task_frame=ttb.Frame(task_content)
        task_frame.pack(fill='x', pady=10)

        task_sub_label = ttb.Label(task_frame,text=formatted_date,style="secondary")
        task_sub_label.pack(fill='x')

        task_label=ttb.Label(task_frame, text=task[-1])
        task_label.pack(fill='x', pady=4)

        task_separator=ttb.Separator(task_frame, style="success")
        task_separator.pack(fill='x', pady=10)


task=[]

# window
window=ttb.Window()
window.geometry('530x800')
window.title("pyWRITE")
window.resizable(False, False)
style=Style(theme="vapor")

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
search_bar.bind("<FocusOut>", lambda e: search_bar.insert(0, "Search"))
search_bar.pack(fill='x')

def on_configure(event):
    task_canvas.config(scrollregion=task_canvas.bbox("all"))

def on_mousewheel(event):
    # Determine the direction of the scroll
    if event.delta > 0:
        task_canvas.yview_scroll(-1, "units")
    elif event.delta < 0:
        task_canvas.yview_scroll(1, "units")


# task_main_frame
task_main_frame=ttb.Frame(main_frame)
task_main_frame.pack(fill="both", padx=15)

# task_canvas
task_canvas=ttk.Canvas(task_main_frame, background="red")
task_canvas.pack(side="left", fill="both")

# task_scrollbar
task_scrollbar=ttb.Scrollbar(task_main_frame, style="info", command=task_canvas.yview)
task_scrollbar.pack(side="right", fill="y")

# Configure the canvas to work with the scrollbar
task_canvas.config(yscrollcommand=task_scrollbar.set)

# Bind the mouse scroll event to the canvas
task_canvas.bind("<MouseWheel>", on_mousewheel)

# task_content
task_content=ttb.Frame(task_canvas)
task_canvas.create_window((0,0), window=task_content, anchor="nw", width=500)

# Bind a function to handle changes to the frame's size
task_content.bind("<Configure>", on_configure)

# Add content to the frame
for i in range(50):
    label = ttb.Button(task_content, text=f"Item {i}")
    label.pack(fill='both')


# run
window.mainloop()