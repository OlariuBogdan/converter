import tkinter as tk
from lib2to3.pytree import convert
from tkinter import ttk
#import ttkbootstrap as ttk


def convert():
    mile_input = entryInt.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)
window = tk.Tk()
window.title('Convertor Mile in Kilometri')
window.geometry('300x150')
window.resizable(False, False)
title_label = tk.Label(window, text='Mile in kilometri', font=('Calibri', 24))
title_label.pack()
input_frame=ttk.Frame(window)
entryInt = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable=entryInt)
button = ttk.Button(input_frame, text='Transforma', command=convert)
entry.pack(side=tk.LEFT, padx=5, pady=5)
button.pack(side=tk.LEFT)
input_frame.pack(padx=10, pady=10)
output_string = tk.StringVar()
output_label = tk.Label(window, text='Mile in kilometri', font=('Calibri', 14), textvariable=output_string)
output_label.pack(padx=5, pady=5)
window.mainloop()