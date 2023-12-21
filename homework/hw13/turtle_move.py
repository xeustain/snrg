import time
import datetime

class Черепашка:
    def __init__(self, x, y, s):
        self.x = x

        self.y = y

        self.s = s

        self.start_time = time.time()


    def go_up(self):
        self.y += self.s


    def go_down(self):
        self.y -= self.s


    def go_left(self):
        self.x -= self.s


    def go_right(self):
        self.x += self.s


    def evolve(self):
        self.s += 1


    def degrade(self):
        if self.s <= 1:
            raise ValueError("Количество клеточек перемещения не может быть меньше или равно 1")
        else:
            self.s -= 1


    def count_moves(self, x2, y2):
        x_moves = abs(x2 - self.x)

        y_moves = abs(y2 - self.y)

        return x_moves + y_moves


x_start = int(input("Введите начальную позицию по оси X: "))
y_start = int(input("Введите начальную позицию по оси Y: "))
s_start = int(input("Введите количество клеточек перемещения за ход: "))


черепашка = Черепашка(x_start, y_start, s_start)

print("Черепашка создан с начальными координатами ({}, {}) и количеством клеточек перемещения: {}".format(черепашка.x, черепашка.y, черепашка.s))


x_end = int(input("Введите координату X конечной точки: "))
y_end = int(input("Введите координату Y конечной точки: "))

moves_required = черепашка.count_moves(x_end, y_end)
print("Черепашке потребуется минимум", moves_required, "ходов, чтобы добраться до указанной точки")

while черепашка.x != x_end or черепашка.y != y_end:
    if черепашка.x < x_end:
        черепашка.go_right()
        print("Текущие координаты: ({}, {}) *черепашка ползёт*".format(черепашка.x, черепашка.y))
        time.sleep(5)
    elif черепашка.x > x_end:
        черепашка.go_left()
        print("Текущие координаты: ({}, {}) *черепашка ползёт*".format(черепашка.x, черепашка.y))
        time.sleep(5)

    if черепашка.y < y_end:
        черепашка.go_up()
        print("Текущие координаты: ({}, {}) *черепашка ползёт*".format(черепашка.x, черепашка.y))
        time.sleep(5)
    elif черепашка.y > y_end:
        черепашка.go_down()
        print("Текущие координаты: ({}, {}) *черепашка ползёт*".format(черепашка.x, черепашка.y))
        time.sleep(5)

end_time = time.time()

total_time = int(end_time - черепашка.start_time)

time_string = str(datetime.timedelta(seconds=total_time))
print("Черепашка достигла конечной точки за", time_string)
