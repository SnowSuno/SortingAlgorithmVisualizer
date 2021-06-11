import time
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from visual_array import VisualArray

from display import Display
from controls import Controls
from information import Information

import _thread

import random
import importlib

SORT_ALGORITHMS = [
    'bubble', 'insertion', 'selection', 'shell', 'merge', 'quick', 'radix'
]

def visual(func):
    def wrapper(self, *args):
        def thread():
            func(self, *args)
            self.array.end()
        _thread.start_new_thread(thread, ())
    return wrapper


class Root(tk.Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.tk.call('source', './Azure-ttk-theme/azure-dark.tcl')
        ttk.Style().theme_use('azure-dark')

        self.algorithm = {}
        self.algorithm_info = {'': ''}

        for algorithm in SORT_ALGORITHMS:
            module = importlib.import_module(f'algorithms.{algorithm}')

            self.algorithm[module.NAME] = module.sort
            self.algorithm_info[module.NAME] = module.INFO


        self.title('Sorting Algorithm Visualization')
        self.geometry('1275x720+100+100')
        self.resizable(False, False)

        self.algorithm_name = tk.StringVar()
        self.array_size = tk.IntVar()
        self.array_size.set(10)
        self.sort_speed = tk.DoubleVar()
        self.sort_speed.set(75)
        self.running_flag = tk.BooleanVar()
        self.running_flag.set(False)

        self.display = Display(self)
        self.display.place(x=15, y=10)
        self.controls = Controls(self)
        self.controls.place(x=1030, y=10)
        self.information = Information(self)
        self.information.place(x=1030, y=400)

        self.array = VisualArray(self)


    def set_array_size(self, *args):
        self.array.set_size(self.array_size.get())

    def get_update_time_interval(self):
        speed = self.sort_speed.get()
        if speed >= 50:
            return 0

        return 0.0002 * ((50 - speed) ** 2)


    @visual
    def reset(self):
        for i in range(self.array_size.get()):
            self.array[i] = i + 1

    @visual
    def shuffle(self):
        random.shuffle(self.array)

    @visual
    def sort(self):
        step = self.algorithm[self.algorithm_name.get()](self.array)

        for _ in step:
            time.sleep(self.get_update_time_interval())

            if not self.running_flag.get():
                return

        self.controls.stop()
