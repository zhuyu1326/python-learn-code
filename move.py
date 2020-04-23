import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 50, 40, math.pi / 6)
print(x, y)