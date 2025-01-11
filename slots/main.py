
# Slots are used for restriction of variables

class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    __slots__ = 'z',

    # def __init__(self, z):

    #     self.z = z

pt3 = Point3D(12, 15)

print(pt3.x)
