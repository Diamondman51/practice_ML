from typing import Any, Type, TypeVar


# This is wrong
class Geom: pass
class Point2D(Geom): pass


def factory_object(cls_obj: Type[Geom]) -> Geom:
    return cls_obj()


# In this case we get object Geom
geom: Geom = factory_object(Geom)
# In this case we get Point2D, that is why here is the problem
point: Point2D = factory_object(Point2D) # TODO Problem




# This is right option
class Geom: pass
class Point2D(Geom): pass


T = TypeVar('T', bound=Geom)


def factory_object(cls_obj: Type[T]) -> T:
    return cls_obj()


# With help of TypeVar we fixed the problem before
# In this case we get Geom
geom: Geom = factory_object(Geom)
# In this case we get Point2D
point: Point2D = factory_object(Point2D) # Todo Fixed problem







class Geom: pass
class Point2D(Geom):
    # x: int
    # y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = 10
        self.y = y

    # This is wrong way of copying
    def copy(self) -> Point2D:
        return Point2D(self.x, self.y)

    # This is right way, but get old
    def copy(self) -> 'Point2D':
        return Point2D(self.x, self.y)


p = Point2D(10, 20)
p.x = '12'




# Required Python version 3.7+
from __future__ import annotations


class Geom: pass
class Point2D(Geom):
    # x: int
    # y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = 10
        self.y = y

    # This is right way of copying(see __future__ package)
    def copy(self) -> Point2D:
        return Point2D(self.x, self.y)


p = Point2D(10, 20)
p.x = '12'
