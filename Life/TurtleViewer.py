import turtle
from Life.Viewer import AbstractViewer


class TurtleViewer(AbstractViewer):

    def __init__(self, _width, _height):
        self.__win = turtle.Screen()
        self.__win.title("Life Viewer")
        self.__win.bgcolor("white")
        self.__win.setup(width=_width, height=_height)
        self.__win.tracer(0)
        self.__x_align = 40
        self.__y_align = 40
        self.__STAMP_SIZE = 20

        self.__left_x = 0 - (self.__win.window_width() / 2) + self.__x_align
        self.__right_x = 0 + (self.__win.window_width() / 2) - self.__x_align
        self.__up_y = 0 + (self.__win.window_height() / 2) - self.__y_align
        self.__down_y = 0 - (self.__win.window_height() / 2) + self.__y_align
        self.__step_x = 1
        self.__step_y = 1

        self.__cell_turtle = turtle.Turtle()
        self.__cell_turtle.speed(0)
        self.__cell_turtle.shape("square")
        self.__cell_turtle.color("green")

        self.__pen = turtle.Turtle()
        self.__pen.speed(0)
        self.__pen.shape("square")
        self.__pen.hideturtle()
        self.__legend = ""

        self.__eraser = turtle.Turtle()
        self.__eraser.hideturtle()

    def test_draw(self):
        col_count = 10
        row_count = 10
        a = self.__get_test_cells(row_count)
        self.__inner_draw(row_count, col_count, a, True)
#        self.__win.mainloop()

    def show_world(self, world, fix_window, legend):
        cells = world.get_world()
        row_count = len(cells)
        if row_count == 0:
            raise Exception("empty world")
        col_count = len(cells[0])
        if col_count == 0:
            raise Exception("empty world")
        gen = world.get_generation()
        _l = legend
        if _l == '':
            _l = "GENERATION {}".format(gen)
        self.__inner_draw(row_count, col_count, cells, gen == 1, _l)
        self.__win.update()
        if fix_window:
            self.__win.mainloop()

    def __inner_draw(self,row_count, col_count, cells, refresh_grid, legend):
        self.__step_x = (self.__win.window_width() - (self.__y_align * 2)) / col_count
        self.__step_y = (self.__win.window_height() - (self.__x_align * 2)) / row_count
        self.__cell_turtle.shapesize((1 / self.__STAMP_SIZE) * (self.__step_x - 5),
                                     (1 / self.__STAMP_SIZE) * (self.__step_y - 5))
        if refresh_grid:
            self.__draw_grid(col_count, row_count)
            self.__pen.penup()
            self.__pen.goto(0, self.__up_y + self.__y_align / 2)

        self.__draw_cells(row_count, col_count, cells)
        self.__draw_legenf(legend)
        self.__win.update()

    def __draw_grid(self, row_count, col_count):
        border = turtle.Turtle()
        border.hideturtle()
        border.pensize(1)
        border.penup()
        border.goto(self.__left_x, self.__up_y)
        border.pendown()
        border.goto(self.__right_x, self.__up_y)
        border.goto(self.__right_x, self.__down_y)
        border.goto(self.__left_x, self.__down_y)
        border.goto(self.__left_x, self.__up_y)
        x = self.__left_x
        for row in range(col_count):
            x = x + self.__step_x
            border.penup()
            border.goto(x, self.__up_y)
            border.pendown()
            border.goto(x, self.__down_y)

        y = self.__up_y
        for row in range(row_count):
            y = y - self.__step_y
            border.penup()
            border.goto(self.__left_x, y)
            border.pendown()
            border.goto(self.__right_x, y)

    def __draw_cells(self, row_count, col_count, cells):
        self.__cell_turtle.right(90)
        self.__cell_turtle.hideturtle()
        self.__cell_turtle.clearstamps()
        for row in range(row_count):
            for col in range(col_count):
                state = cells[row][col]
                if state > 0:
                    self.__cell_turtle.penup()
                    self.__cell_turtle.goto(self.__left_x + self.__step_x * col + self.__step_x / 2,
                              self.__up_y - self.__step_y * row - self.__step_y / 2)
                    self.__cell_turtle.stamp()

    def __draw_legenf(self, legend):
        if self.__legend != "":
            self.__erase_legend()
        self.__pen.color("black")
        self.__pen.write(legend, align="center", font=("Verdana", 10, "normal"))
        self.__legend = legend

    def __erase_legend(self):
        self.__eraser.color(self.__win.bgcolor())
        self.__eraser.penup()
        self.__eraser.pensize(self.__y_align)
        self.__eraser.goto(self.__left_x,self.__up_y+self.__y_align / 2)
        self.__eraser.pendown()
        self.__eraser.goto(self.__right_x, self.__up_y + self.__y_align / 2)

    def __get_test_cells(self, size):
        a = [[0] * size for i in range(size)]
        a[0] = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        a[1] = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        a[2] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        a[3] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a[6] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a[7] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a[8] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a[9] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        return a



