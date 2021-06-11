import tkinter as tk
from tkinter import ttk



class Display(ttk.LabelFrame):
    def __init__(self, root):


        super(Display, self).__init__(
            root, text=' Visualization ',
            width=1000, height=695
        )

        # self.display = self.Displayer(self)

        # self.display = VisualArray(self, 500)
        # self.display.place(relx=0.5, rely=0.5, anchor=tk.CENTER)




    # def visual_update(self):
    #     self.display.
    # class Displayer(tk.Canvas):
    #     def __init__(self, parent):
    #         super().__init__(
    #             parent,
    #             width=950, height=650,
    #             bg='white'
    #         )


#
# class VisualArray(tk.Canvas):
#     def __init__(self, parent, n):
#         self.w, self.h = 950, 640
#         self.len = n
#         self.array = list(range(1, n+1))
#         self.color = '#727272'
#
#         self.dx = self.w / self.len
#         self.dy = self.h / self.len
#
#         super(VisualArray, self).__init__(
#             parent,
#             width=self.w, height=self.h
#         )
#         self.create_visual()
#
#
#     def create_visual(self):
#         x = 0
#         for i in range(self.len):
#             y = self.h - self.array[i] * self.dy
#
#             self.create_rectangle(
#                 x, self.h, x+self.dx, y, width=0, fill=self.color)
#             x += self.dx
#
#     def update_visual(self):
#         for i in range(self.len):
#             y = self.h - self.array[i] * self.dy
#             x0, _, x1, _ = self.coords(i+1)
#             self.coords(i+1, x0, self.h, x1, y)
#
#
