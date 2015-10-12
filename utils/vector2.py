import math


class Vector2:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

        if hasattr(x, "__getitem__"):
            x, y = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @x.deleter
    def x(self):
        del self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @y.deleter
    def y(self):
        del self.__y

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = 1.0 * value

    def __repr__(self):
        return "Vector2(x={0}, y={1})".format(self.__x, self.__y)

    # rhs: Right Hand Side (lado direito)
    def __add__(self, rhs):
        return Vector2(self.__x + rhs.x, self.__y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.__x - rhs.x, self.__y - rhs.y)

    def __mul__(self, scalar):
        return Vector2(self.__x * scalar, self.__y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.__x / scalar, self.__y / scalar)

    def __neg__(self):
        return Vector2(-self.__x, -self.__y)

    def __str__(self):
        return "({0}, {1})".format(self.__x, self.__y)

    def points(p1, p2):
        return Vector2(p2[0] - p1[0], p2[1] - p1[1])

    def magnitude(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def normalize(self):
        magnitude = self.magnitude()
        self.__x /= magnitude
        self.__y /= magnitude

if __name__ == "__main__":

    # A = (10.0, 20.0)
    # B = (30.0, 35.0)
    # C = (15.0, 45.0)
    # AB = Vector2.points(A, B)
    # BC = Vector2.points(B, C)
    # AC = Vector2.points(A, C)
    # print("Vector AC is", AC)
    #
    # AC = AB + BC
    # print("AB + BC is", AC)

    # A = (10.0, 20.0)
    # B = (30.0, 35.0)
    # AB = Vector2.points(A, B)
    # step = AB * 0.1
    # position = Vector2(*A)
    # for n in range(10):
    #     position += step
    #     print(position)
    v = Vector2(1, 2)
    v.x = 1000.2
    print(v.x)
