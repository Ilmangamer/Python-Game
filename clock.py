import tkinter as tk
from datetime import datetime, timedelta

# ####--- Note to developer---- #####
# Get a clock in tkinter GUI
# Imports 
# Size and geometry
# create a label with font. Display it
# Create a function where you create strftime
# Configure that variable to your existing label
# tell it to display after 1000 ms, then show time

root = tk.Tk()
root.geometry("250x100")


def moving_time():
    now = datetime.now()
    now_strftime = (now.strftime("%H:%M:%S %p"))
    now_timedelta = (now + timedelta(seconds =+1)).strftime("%H:%M:%S %p")
    return now_timedelta

clock_label = tk.Label(root, text= moving_time(), font=("ds-digital", 80), background="black", foreground="green")
clock_label.pack(anchor="center")

root.configure(bg="black")


def update():
    clock_label['text'] = moving_time()
    root.after(1000, update)

update()

root.mainloop()

#####---- Note to developer #########
# tkinter way of updating variables
""""
clock_label["text"] = moving_time()
What it does is that it updates the text variable object to what the moving_time function returns
"""
# normal way of updating variables
"""
my_obeject.my_value = new_value
"""



