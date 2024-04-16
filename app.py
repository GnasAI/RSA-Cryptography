from tkinter import * 
import os

from settings import *

class App():
    def __init__(self,root) -> None:
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (WINDOW_WIDTH/2))
        y_cordinate = int((screen_height/2) - (WINDOW_HEIGHT/2)-50)
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_cordinate}+{y_cordinate}")
        root["bg"] = COLOR_GRAY
        root.title('RSA Cryptography')
        root.iconbitmap(os.path.join(PATH_IMG,'icon.ico'))
        root.resizable(False,False)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.columnconfigure(2, weight=1)
        root.columnconfigure(3, weight=2)
        root.columnconfigure(4, weight=1)
        root.rowconfigure(0, weight=2)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
        root.rowconfigure(3, weight=1)
        root.rowconfigure(4, weight=1)
        root.rowconfigure(5, weight=1)
        root.rowconfigure(6, weight=1)
        root.rowconfigure(7, weight=1)
        root.rowconfigure(8, weight=1)
        root.rowconfigure(9, weight=2)
        root.rowconfigure(10, weight=2)
        
