# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 23:07:50 2018

@name: watch.py
@author: Cma
"""

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import time
    
class ChangeHandler(FileSystemEventHandler):
    def __init__(self, application):
        self.application = application
        
    def on_created(self, event):
        filepath = event.src_path
        filepath = filepath.replace('/', '\\')
        time.sleep(1)
        print(filepath)
        self.application.imagepath = filepath
        
    def watch(self,path):
        print('Start watcing.')
        observer = Observer()
        observer.schedule(self, path, recursive=True)
        observer.start()
        
if __name__ == '__main__':
    path = 'E:\Recorded'
    handler = ChangeHandler()
    handler.watch(path)