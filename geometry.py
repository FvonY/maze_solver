from tkinter import Canvas


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line():
    def __init__(self, a: Point, b: Point):
        self.__a = a
        self.__b = b
        
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.__a.x, self.__a.y, 
                           self.__b.x, self.__b.y, 
                           fill=fill_color, 
                           width=2)
        