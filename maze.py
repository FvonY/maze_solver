from window import Window
from geometry import Point
from cell import Cell
from time import sleep


class Maze():
    def __init__(self, top_left: Point, rows, cols, cell_edge_length, window: Window):
        self._top_left = top_left
        self._rows = rows
        self._cols = cols
        self._cell_edge_length = cell_edge_length
        self._window = window
        
        self._cells = self._create_cells()
    
    def _create_cells(self):
        cells = []
        
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                point = Point(self._top_left.x + j*self._cell_edge_length,
                              self._top_left.y + i*self._cell_edge_length)
                cell = Cell(self._window, point)
                row.append(cell)
            cells.append(row)
        return cells     
    
    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
        self._animate()
    
    def _animate(self):
        self._window.redraw()
        sleep(0.05)
    