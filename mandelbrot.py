import math
import time

FILL=" -+o%#@"

SIZE_X = 200
SIZE_Y = 50
X_RANGE = (-2.5, 1.0)
Y_RANGE = (-1.2, 1.2)

X_STEP = (X_RANGE[1] - X_RANGE[0]) / SIZE_X
Y_STEP = (Y_RANGE[1] - Y_RANGE[0]) / SIZE_Y

V_RANGE = (0.0, 1.0)

output = ""

MAX_ITER = 20

def draw_value(v):
    return FILL[math.floor((v - V_RANGE[0]) / (V_RANGE[1] - V_RANGE[0]) * (len(FILL) - 1) )]

def mandel(x0, y0):
    x = 0.0
    y = 0.0
    i = 0

    while x * x + y * y < 4 and i < MAX_ITER:
        x1 = x * x  - y * y + x0
        y = 2 * x * y + y0
        x = x1
        i += 1

    return draw_value(i / MAX_ITER)



from datetime import datetime


start = datetime.now()

for ys in range(0, SIZE_Y):
    y = Y_RANGE[0] + Y_STEP * ys
    for xs in range(0, SIZE_X):
        x = X_RANGE[0] + X_STEP * xs
        output += mandel(x, y)
    output += "\n"





end = datetime.now()

print(output)

print(end - start)
