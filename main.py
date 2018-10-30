# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:06:12 2018

@name: main.py
@author: Cma
"""

import tkinter.filedialog as tkFiledialog

import app

def run():
    application = app.Application()
    """
    # Read from Config
    config = open('folder.conf', mode='r')
    folder = config.readline()
    config.close()
    print(folder)
    # Run Watcher
    watcher = watch.ChangeHandler()
    watcher.watch(folder)
    """
    
if __name__ == '__main__':
    run()
