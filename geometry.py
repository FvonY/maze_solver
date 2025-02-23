from tkinter import Canvas


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line():
    def __init__(self, a: Point, b: Point):
        self._a = a
        self._b = b
        
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self._a.x, self._a.y, 
                           self._b.x, self._b.y, 
                           fill=fill_color, 
                           width=2)
        