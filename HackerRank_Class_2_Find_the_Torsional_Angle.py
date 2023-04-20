# this is about the HackerRank test: Class 2 - Find the Torsional Angle
# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem 

# I found many solutions around but nobody explained really the code. Also the problem description itself might bring
# confusion for the way it is written. I will try to go as less as possible in Math ground because the test is about 
# Python Classes. In the Problem description, the coordinates are named X, Y and Z. The results of the cross products
# are named X and Y too, but these values are not related. Mathematicians could name coordinates with lower case x, 
# y and z and leave the cross product names with upper case X and Y to be clear. Instead for the pythonic way to name
# variables, I wouldn't use upper case anyway in the problem description. As you can see in the help code already 
# provided, they are lower cases. The same for the points A, B, C and D, written upper case in the problem 
# description and lower case in the help code 
import math


class Points(object):
    # these arguments could lead to confusion: most of the people who solved the problem, named these arguments x, y
    # and z: besides the naming confusion mentioned above (they are not related to x = (b - a).cross(c - b) and y = (c
    # - b).cross(d - c)), these arguments will be assigned not only to the input coordinate values but even to the
    # results of AB=B-A, BC=C-B and CD=C-D and the results of the cross products. I would rather consider them sort of
    # accumulators. For this reason I will name them u, v, w.
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __sub__(self, no):
        # here is where AB=B-A, BC=C-B and CD=C-D is defined
        return Points((self.u - no.u), (self.v - no.v), (self.w - no.w))

    def dot(self, no):
        # here is where dot product X.Y is defined
        return (self.u * no.u) + (self.v * no.v) + (self.w * no.w)

    def cross(self, no):
        # here is where cross product X=ABxBC and Y=BCxCD are defined
        return Points((self.v * no.w - self.w * no.v), (self.w * no.u - self.u * no.w), (self.u * no.v - self.v * no.u))

    def absolute(self):
        # here is where the absolute value |X| and |Y| are defined
        return pow((self.u ** 2 + self.v ** 2 + self.w ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)
        # "a" is confusing: there is no relation with the following "a, b, c, d". This "a" should be defined something
        # like "lst" or any other letter rather than "a"

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
