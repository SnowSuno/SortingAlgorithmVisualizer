import tkinter as tk
import _thread

class VisualArray(list):
    def __init__(self, root):
        parent = root.display
        size = root.array_size.get()

        super(VisualArray, self).__init__(range(1, size+1))
        self.points = [None] * (4 * self.__len__() + 4)

        self.w, self.h = 950, 640
        self.dx = self.w / self.__len__()
        self.dy = self.h / self.__len__()
        self.color = '#727272'

        self.visual = tk.Canvas(
            parent,
            width=self.w, height=self.h
        )
        self.array_id = None

        self.create_visual()
        self.visual.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.update_count = 0
        self.speed = root.sort_speed


    def set_size(self, size):
        self.clear()
        self.extend(range(1, size+1))
        self.points = [None] * (4 * self.__len__() + 4)

        self.dx = self.w / self.__len__()
        self.dy = self.h / self.__len__()

        self.set_points()
        self._visual_update()

    def get_update_step_interval(self):
        speed = self.speed.get()
        if speed < 50:
            return 1

        return 2 ** ((speed - 50)/20)


    def set_points(self):
        x = 0
        for i in range(self.__len__()):
            y = self.h - self[i] * self.dy

            self.points[4 * i], self.points[4 * i + 1] = x, y
            self.points[4 * i + 2], self.points[4 * i + 3] = x + self.dx, y
            # x, y, x + self.dx, y

            x += self.dx

        self.points[-2], self.points[-1] = 0, self.h
        self.points[-4], self.points[-3] = self.w, self.h


    def create_visual(self):
        self.set_points()
        self.array_id = self.visual.create_polygon(
            self.points, width=0, fill=self.color)

    def __getitem__(self, key):
        return super(VisualArray, self).__getitem__(key)

    def __setitem__(self, key, value):
        x = self.dx * key
        y = self.h - value * self.dy

        self.points[4 * key], self.points[4 * key + 1] = x, y
        self.points[4 * key + 2], self.points[4 * key + 3] = x + self.dx, y

        super(VisualArray, self).__setitem__(key, value)
        self._update()


    def _update(self):
        # self.visual.itemconfig(self.prev, fill=self.color)
        # self.visual.itemconfig(key + 1, fill='red')
        # self.prev = key + 1
        self.update_count += 1

        if self.update_count >= self.get_update_step_interval():
            self._visual_update()

            self.update_count = 0


    def _visual_update(self):
        self.visual.coords(self.array_id, self.points)
        # self.visual.update()

    def end(self):
        self._visual_update()


