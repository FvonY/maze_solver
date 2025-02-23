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
    #seeds...
    # 12312512

    #test_playground(win)
    point = Point(20, 20)
    maze = Maze(point, 23, 30, 25, win)
    #maze = Maze(point, 10, 10, 50, win)
    #input("Press to start")
    maze._break_walls_r(0,0)
    maze._reset_visited()
    maze._draw_cells()
    maze.solve()
    print("solved")
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
