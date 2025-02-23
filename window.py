from tkinter import Tk, BOTH, Canvas
from geometry import Line


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Mazer"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(width=width, height=height)
        self.__canvas.pack(fill='both')

        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)
