import tkinter as tk
from tkinter import ttk

class Controls(ttk.LabelFrame):
    def __init__(self, root):
        super(Controls, self).__init__(
            root, text=' Controls ',
            width=230, height=380,
        )
        self.sort = root.sort
        self.running_flag = root.running_flag

        ttk.Label(self, text='Algorithm Type').place(x=15, y=15)
        self.algorithms = ttk.Combobox(
            self, state='readonly',
            textvariable=root.algorithm_name,
            values=list(root.algorithm.keys()),
            width=24
        )
        self.algorithms.place(x=15, y=40)
        self.algorithms.bind('<<ComboboxSelected>>', self.algorithm_change)


        ttk.Label(self, text='Array Size').place(x=15, y=100)
        self.size_scale = ttk.Scale(
            self, length=200, from_=10, to=1000, variable=root.array_size, command=root.set_array_size)
        self.size_scale.place(x=15, y=125)


        ttk.Label(self, text='Sort Speed').place(x=15, y=175)
        self.speed_scale = ttk.Scale(
            self, length=200, from_=1, to=150, variable=root.sort_speed)
        self.speed_scale.place(x=15, y=200)


        self.reset_btn = ttk.Button(self, text='Reset', command=root.reset)
        self.reset_btn.place(x=15, y=260)

        self.shuffle_btn = ttk.Button(
            self, text='Shuffle', command=root.shuffle
        )
        self.shuffle_btn.place(x=120, y=260)


        self.start_btn = ttk.Button(
            self, text='Start', style='AccentButton', width=25, command=self.start, state=tk.DISABLED)
        self.start_btn.place(x=15, y=305)

    def algorithm_change(self, *args):
        self.start_btn.config(state=tk.NORMAL)


    def start(self):
        self.running_flag.set(True)
        self.algorithms.config(state=tk.DISABLED)
        self.shuffle_btn.config(state=tk.DISABLED)
        self.size_scale.config(state=tk.DISABLED)

        self.start_btn.config(text='Stop', command=self.stop)

        self.sort()

    def stop(self):
        self.running_flag.set(False)

        self.algorithms.config(state='readonly')
        self.shuffle_btn.config(state=tk.NORMAL)
        self.size_scale.config(state=tk.NORMAL)

        self.start_btn.config(text='Start', command=self.start)
