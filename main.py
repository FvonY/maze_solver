from window import Window
from geometry import Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    
    Line1 = Line(Point(0,0), Point(500,500))
    win.draw_line(Line1, 'red')
    
    cell = Cell(win, Point(50, 200))
    cell.draw()
    
    cell_damage = Cell(win, Point(200, 200))
    cell_damage.walls = [1, 1, 0, 1]
    
    cell_damage.draw()
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
