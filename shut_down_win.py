#!/usr/bin/python
import threading

import tkinter as tk
from tkinter import *
import time
import os
def close_win():
        os.system('shutdown -s -t 0')
def main():
        top = tk.Tk()
        top.title('Table setting experiment')
        top.geometry('1920x1080')
        top.config(bg='azure')
        #abc=gui_main
        green_low_polite=tk.Button(top,padx=1.0,pady=1.0,height=25,width=45,bg='SeaGreen1',command=close_win)
        green_low_polite.grid(row=500,column=3,padx=10,pady=10)
        green_low_polite.place(relx=0.3,rely=0.5,anchor=CENTER)
        top.mainloop()
if __name__== "__main__":
        main()
