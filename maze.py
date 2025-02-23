from window import Window
from geometry import Point, Line
from cell import Cell
from time import sleep
import random


class Maze():
    def __init__(self, top_left: Point, rows, cols, cell_edge_length, window: Window, seed=None):
        self._top_left = top_left
        self._rows = rows
        self._cols = cols
        self._cell_edge_length = cell_edge_length
        self._window = window
        
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        
        self.moves = []
        self.undos = []
        
        if seed is not None:
            random.seed(seed)
        else:
            random.seed()
    
    def _create_cells(self):
        cells = []
        
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                point = Point(self._top_left.x + j*self._cell_edge_length,
                              self._top_left.y + i*self._cell_edge_length)
                cell = Cell(self._window, point, self._cell_edge_length)
                row.append(cell)
            cells.append(row)
        return cells     
    
    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
        self._animate()
        
    def _draw_moves(self):
        for line in self.moves:
            self._window.draw_line(line, "green")
        for undo in self.undos:
            self._window.draw_line(undo, "red")
    
    def _animate(self):
        self._window.redraw()
        sleep(0.05)
        
    def _break_entrance_and_exit(self):
        entrace_cell:Cell
        entrace_cell = self._cells[0][0]
        entrace_cell.walls[0] = False
        
        exit_cell:Cell
        exit_cell = self._cells[self._rows-1][self._cols-1]
        exit_cell.walls[2] = False
        
    def _break_walls_r(self, i, j):
        cell: Cell
        cell = self._cells[i][j]
        cell.visited = True
        
        #print(i, j)
        
        while True:
            to_visit = []
            possible_directions = []
            
            ## possible neighbors
            # top
            if i != 0:
                if not self._cells[i-1][j].visited:
                    possible_directions.append((i-1,j))
            # right
            if j != self._cols-1:
                if not self._cells[i][j+1].visited:
                    possible_directions.append((i,j+1))
            # bottom
            if i != self._rows-1:
                if not self._cells[i+1][j].visited:
                    possible_directions.append((i+1,j))
            # left
            if j != 0:
                if not self._cells[i][j-1].visited:
                    possible_directions.append((i,j-1))
            
            if len(possible_directions) == 0:
                return
            
            random_direction = random.randint(0,len(possible_directions)-1)
            chosen_direction = possible_directions[random_direction]
            i_dif = i - chosen_direction[0]
            j_dif = j - chosen_direction[1]
            
            other_cell: Cell
            other_cell = self._cells[chosen_direction[0]][chosen_direction[1]]
            
            # we went top
            if i_dif == 1:
                cell.walls[0] = False
                other_cell.walls[2] = False
            # we went right
            if j_dif == -1:
                cell.walls[1] = False
                other_cell.walls[3] = False
            # we went bottom
            if i_dif == -1:
                cell.walls[2] = False
                other_cell.walls[0] = False
            # we went left
            if j_dif == 1:
                cell.walls[3] = False
                other_cell.walls[1] = False
                
            # self._window.clear()
            # self._draw_cells()
            # sleep(0.000625)
                
            self._break_walls_r(chosen_direction[0], chosen_direction[1])
            
    def _reset_visited(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].visited = False
    
    def solve(self, i=0, j=0):
        def solve_r(i, j):
            #self._window.clear()
            #self._draw_cells()
            #self._draw_moves()
            #sleep(0.000625)
            
            #print(len(self.moves))
            
            cell: Cell
            cell = self._cells[i][j]
            cell.visited = True
            
            if (i,j) == (self._rows-1, self._cols-1):
                return True
            
            ## possible neighbors
            # top
            if i != 0:
                top_cell: Cell
                top_cell = self._cells[i-1][j]
                if not top_cell.visited and not cell.has_top_wall():
                    self.moves.append(Line(cell.get_center(), top_cell.get_center()))
                    if solve_r(i-1, j):
                        return True
                    else:
                        self.undos.append(Line(cell.get_center(), top_cell.get_center()))
                        pass
            # right
            if j != self._cols-1:
                right_cell: Cell
                right_cell = self._cells[i][j+1]
                if not right_cell.visited and not cell.has_right_wall():
                    self.moves.append(Line(cell.get_center(), right_cell.get_center()))
                    if solve_r(i, j+1):
                        return True
                    else:
                        self.undos.append(Line(cell.get_center(), right_cell.get_center()))
                        pass
            # bottom
            if i != self._rows-1:
                bottom_cell: Cell
                bottom_cell = self._cells[i+1][j]
                if not bottom_cell.visited and not cell.has_bottom_wall():
                    self.moves.append(Line(cell.get_center(), bottom_cell.get_center()))
                    if solve_r(i+1, j):
                        return True
                    else:
                        self.undos.append(Line(cell.get_center(), bottom_cell.get_center()))
                        pass
            # left
            if j != 0:
                left_cell: Cell
                left_cell = self._cells[i][j-1]
                if not left_cell.visited and not cell.has_left_wall():
                    self.moves.append(Line(cell.get_center(), left_cell.get_center()))
                    if solve_r(i, j-1):
                        return True
                    else:
                        self.undos.append(Line(cell.get_center(), left_cell.get_center()))
                        pass
            return False       
        return solve_r(i, j)
    