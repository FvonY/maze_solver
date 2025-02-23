from window import Window
from geometry import Line, Point


class Cell():
    edge_length = 50
    
    def __init__(self, window: Window, top_left: Point):
        self._window = window
        self._top_left = top_left
        self._top_right = Point(top_left.x + self.edge_length, top_left.y)
        self._bottom_right = Point(top_left.x + self.edge_length, top_left.y + self.edge_length)
        self._bottom_left = Point(top_left.x, top_left.y + self.edge_length)
        
        ## Order: top, right, bottom, left
        self.walls = [True for i in range(4)]
        
    def draw(self):
        if self.has_top_wall():
            self._window.draw_line(Line(self._top_left, self._top_right), 'green')
        if self.has_right_wall():
            self._window.draw_line(Line(self._top_right, self._bottom_right), 'blue')
        if self.has_bottom_wall():
            self._window.draw_line(Line(self._bottom_right, self._bottom_left), 'red')
        if self.has_left_wall():
            self._window.draw_line(Line(self._bottom_left, self._top_left), 'yellow')
            
    def draw_connection(self, target_cell: "Cell", undo=False):
        connection_line = Line(self.get_center(), target_cell.get_center())
        self._window.draw_line(connection_line, "red" if undo else "springgreen")
            
    def get_center(self):
        return Point(self._top_left.x + self.edge_length / 2,
                     self._top_left.y + self.edge_length / 2)
        
    def has_top_wall(self):
        return self.walls[0]
    
    def has_right_wall(self):
        return self.walls[1]
    
    def has_bottom_wall(self):
        return self.walls[2]
    
    def has_left_wall(self):
        return self.walls[3]
        