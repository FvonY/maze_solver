from window import Window
from geometry import Line, Point
from cell import Cell
from maze import Maze
from time import sleep


def test_playground(win):
    Line1 = Line(Point(0,0), Point(500,500))
    win.draw_line(Line1, 'red')
    
    cell = Cell(win, Point(50, 200))
    cell.draw()
    
    cell_damage = Cell(win, Point(200, 200))
    cell_damage.walls = [1, 1, 0, 1]
    
    cell_damage.draw()
    
    cell3 = Cell(win, Point(50,250))
    cell3.walls = [0,1,1,0]
    cell3.draw()
    
    cell.draw_connection(cell_damage)
    cell.draw_connection(cell3, True)
    cell3.draw_connection(cell_damage)
    
    
def main():
    win = Window(800, 600)

    #test_playground(win)
    point = Point(20, 20)
    maze = Maze(point, 8, 10, 50, win)
    
    maze._break_walls_r(0,0)
    win.running = True
    while win.running:       
        win.clear()
        maze._draw_cells()
    
    #win.wait_for_close()


if __name__ == "__main__":
    main()
