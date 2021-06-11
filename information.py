import tkinter as tk
from tkinter import ttk

class Information(ttk.LabelFrame):
    def __init__(self, root):
        super(Information, self).__init__(
            root, text=' Information ',
            width=230, height=305,
        )
        left, mid, right = 15, 100, 210

        self.algorithm_info = root.algorithm_info
        self.info = ttk.Label(self, wraplength=195)
        self.info.place(x=15, y=110)

        row = [10, 40, 70]
        self.variables = [
            ('Algorithm', ttk.Label(self), root.algorithm_name),
            ('Array Size', ttk.Label(self), root.array_size),
            ('Sort Speed', ttk.Label(self), root.sort_speed)
        ]
        for i in range(len(self.variables)):
            name_tag, label, variable = self.variables[i]

            ttk.Label(self, text=name_tag).place(x=left, y=row[i])
            ttk.Label(self, text=':').place(x=mid, y=row[i])
            label.place(x=right, y=row[i], anchor=tk.NE)

            variable.trace_add('write', self._update_callback(i))

            self._update_callback(i)()

        ttk.Label(self, text='Made by 19-006 권순호').place(x=220, y=265, anchor=tk.NE)
        
    def _update_callback(self, i):
        def _update(*args):
            name_tag, label, variable = self.variables[i]

            text = variable.get()
            if i == 0:
                self.info.config(text=self.algorithm_info[text])

            elif i == 2:
                text = int(text)
            label.config(text=text)

        return _update
