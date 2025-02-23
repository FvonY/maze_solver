from window import Window
from geometry import Line, Point


def main():
    win = Window(800, 600)
    
    Line1 = Line(Point(0,0), Point(500,500))
    win.draw_line(Line1, 'red')
    
    win.wait_for_close()


if __name__ == "__main__":
    main()
