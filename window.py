from tkinter import Tk, BOTH, Canvas
from geometry import Line


class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title = "Mazer"
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self._canvas = Canvas(width=width, height=height, background='gray16')
        self._canvas.pack(fill='both')

        self.running = False
        
    def clear(self):
        self._canvas.delete("all")

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self._canvas, fill_color)
