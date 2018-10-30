# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:25:12 2018

@name: app.py
@author: Cma
"""

import tkinter as tk
import tkinter.filedialog as tkFiledialog
from PIL import Image, ImageTk, ImageFile

import const
import watch

ImageFile.LOAD_TRUNCATED_IMAGES = True
    
class Application(tk.Frame):
    def __init__(self, master=None):
        if master is None:
            self.root = self.make_root()
        super().__init__(master)
        self['height'] = const.DEFAULT_HEIGHT
        self['width'] = const.DEFAULT_WIDTH
        self.pack(fill=tk.BOTH)
        
        # Ask Folder saves screenshot
        self.folder = tkFiledialog.askdirectory()
        if self.folder == '':
            self.root.destroy()
            return
        
        # Init Widgets
        self.root.resizable(False, False)
        self.pack_propagate(0)
        
        self.control = tk.Frame(self)
        self.text = tk.Label(self.control)
        self.text['text'] = const.SS_FOLDER_MESSAGE.replace('<!>', self.folder)
        self.text.pack(anchor=tk.W, side=tk.LEFT)
        self.reset_button = tk.Button(self.control, text="Reset", command=self.reset_image)
        self.reset_button.pack(anchor=tk.E, side=tk.LEFT)
        self.control.pack()
        
        self.viewer = tk.Label(self)
        self.viewer.pack(anchor=tk.N)

        
        # Start to watch
        watcher = watch.ChangeHandler(self)
        watcher.watch(self.folder)
        # Init image path
        self.imagepath = None
        
        # Start watch imagepath value
        self.show_image()
        
        # Launch the Application
        self.mainloop()


    def make_root(self):
        root = tk.Tk()
        root.title(const.TITLE)
        root.geometry(const.DEFAULT_SIZE)
        return root
    
    def show_image(self):
        if self.imagepath is not None:
            img = ImageTk.PhotoImage(
                    Image.open(self.imagepath).resize((const.IMAGE_WIDTH, const.IMAGE_HEIGHT)))
            self.viewer.configure(image=img)
            self.viewer.image = img
            # Reset my imagepath value
            self.imagepath = None
        self.after(500, self.show_image)
        
    def reset_image(self):
        self.viewer.image = None
        
    def start_watch(self):
        self.watcher = watch.ChangeHandler(self)
        self.watcher.watch(self.folder)
        
    def bye(self):
        self.root.destroy()
        
        
    """
        Event when file created
    """
    def on_created_image(self, path):
        self.viewer = tk.Label(self)
        img = ImageTk.PhotoImage(Image.open(path).resize((const.DEFAULT_WIDTH, const.DEFAULT_HEIGHT)))
        self.viewer.configure(image=img)
        self.viewer.image = img
        self.viewer.grid()
        
    """
        Push Event to queue
    """
    def notify(self, event):
        self.queue.put(event)
        self.root.event_generate("<<WatchdogEvent>>", when="tail")
