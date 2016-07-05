import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle);
    ny = y - step * math.sin(angle);
    return nx, ny

#匿名函数 关键字lambda
f = lambda x: x*x

print(f(5))






x, y = move(100, 100, 60, math.pi/6)
print(x, y)