import abc
from abc import ABC


"""This sucks."""

class Style(ABC):

    @abc.abstractmethod
    def get_style(self) -> str:
        pass



class Fill(Style):

    def __init__(self) -> None:
        super().__init__()
        self.value: str = ""
        """Sets the fill colour of the shape. Use colour name or rgb triplet."""


    def get_style(self) -> str:
        return "fill=" + self.value



class Stoke(Style):

    def __init__(self):
        super().__init__()
        self.value: str = ""
        """Sets the colour of the Stoke. Use colour name or rgb triplet."""


    def get_style(self) -> str:
        return "stoke=" + self.value



class StrokeWidth(Style):

    def __init__(self):
        super().__init__()
        self.value: int = 2;



