# pip install polygenerator

from polygenerator import (
  random_polygon,
)
import matplotlib.pyplot as plt
import random

def LinearCong(n):
    m = 101
    c = 17
    a = 79
    res = [12]

    while len(res)-1!=n:
        si = (a*res[-1]+c)%m
        res.append(si)
    return res

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def onLine(l1, p):
    if (
        p.x <= max(l1.p1.x, l1.p2.x)
        and p.x >= min(l1.p1.x, l1.p2.x)
        and (p.y <= max(l1.p1.y, l1.p2.y) and p.y >= min(l1.p1.y, l1.p2.y))
    ):
        return True
    return False

def direction(a, b, c):
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if val == 0:
        return 0
    elif val < 0:

        return 2
    return 1

def isIntersect(l1, l2):
    dir1 = direction(l1.p1, l1.p2, l2.p1)
    dir2 = direction(l1.p1, l1.p2, l2.p2)
    dir3 = direction(l2.p1, l2.p2, l1.p1)
    dir4 = direction(l2.p1, l2.p2, l1.p2)

    if dir1 != dir2 and dir3 != dir4:
        return True

    if dir1 == 0 and onLine(l1, l2.p1):
        return True

    if dir2 == 0 and onLine(l1, l2.p2):
        return True

    if dir3 == 0 and onLine(l2, l1.p1):
        return True

    if dir4 == 0 and onLine(l2, l1.p2):
        return True

    return False

def checkInside(poly, n, p):
    if n < 3:
        return False

    exline = line(p, Point(9999, p.y))
    count = 0
    i = 0
    while True:
        side = line(poly[i], poly[(i + 1) % n])
        if isIntersect(side, exline):
            if (direction(side.p1, p, side.p2) == 0):
                return onLine(side, p);
            count += 1

        i = (i + 1) % n;
        if i == 0:
            break
    return count & 1;

def plot_polygon(polygon, out_file_name):
    plt.figure()
    plt.gca().set_aspect("equal")

    for i, (x, y) in enumerate(polygon):
        plt.text(x, y, str(i), horizontalalignment="center", verticalalignment="center")

    polygon.append(polygon[0])

    xs, ys = zip(*polygon)
    plt.plot(xs, ys, "r-", linewidth=0.4)

    plt.savefig(out_file_name, dpi=300)
    plt.close()

polygon = []
n = 10
random.seed(5)
points_inside = 0
total_points = 0
d_polygon = random_polygon(num_points=n)
print(d_polygon)

for ele in d_polygon:
    polygon.append(Point(ele[0], ele[1]))

plot_polygon(d_polygon, "random_polygon.png")

for i in range(100000):
    x = random.uniform(0, 1.0)
    y = random.uniform(0, 1.0)
    rand_point = Point(x, y)
    if checkInside(polygon, n, rand_point):
        points_inside+=1
    total_points+=1

print(points_inside/float(total_points))

