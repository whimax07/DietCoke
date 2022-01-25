import abc


class Shape(abc.ABC):

    @abc.abstractmethod
    def generate_shape(self) -> str:
        pass



class Rectangle(Shape):

    def __init__(self) -> None:
        super()
        self.bounds: str = ""
        self.styles: map[str, str] = {}


    def generate_shape(self) -> str:
        return ""


    # Note(Max): Could these be kwargs?
    def define_bounds(self, x: int, y:int, width: int, height: int) -> None:
        self.bounds = f"x=\"{x}\" y=\"{y}\" width=\"{width}\" height=\"{height}\""


    # Note(Max): This is a very naive way of doing this as it doesn't give the user any feed back.
    # It lacks info on what keys can be given and what values they can accept.
    def add_style(self, key: str, value: str):
        self.styles[key] = value



class Triangle(Shape):

    def __init__(self) -> None:
        super().__init__()


    def generate_shape(self) -> str:
        return ""



class Polygon(Shape):

    def __init__(self) -> None:
        super()
        self.shape: str = ""
        self.points: list[tuple[int, int]] = []


    def addPoint(self, x: int, y: int) -> 'Polygon':
        self.points.append((x, y))
        return self


    def generate_shape(self) -> str:
        return self.shape