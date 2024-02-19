from tkinter import *
import time


a_root = Tk()
a_root.title("Digital Clock")
a_root.geometry("800x300")
a_root.config(bg="black")


def now():
    current_time = time.strftime("%I:%M:%S  %p")
    clock.config(text=current_time)
    clock.after(200, now)


Label(a_root, text="Digital Clock", font="calibri 50", bg="black", fg="green").pack()
clock = Label(a_root, font="calibri 90", bg="black", fg="white")
clock.pack()
now()
a_root.mainloop()
