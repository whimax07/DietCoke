from typing.io import TextIO

from PyVG.Shapes import Shape


class BuildSVG(object):

    def __init__(self):
        super()
        self.shapes: list[Shape] = []
        self.body = ""
        self.image: str = ""


    def add_shape(self, shape: Shape) -> None:
        self.shapes.append(shape)


    def generate_image(self) -> None:
        self.__combine_shapes()

        base_csv: BaseCSV = BaseCSV()
        self.image = base_csv.wrap_with_img_base(self.body)


    def __combine_shapes(self) -> None:
        for shape in self.shapes:
            self.body += shape.generate_shape()


    def write_image_file(self, file_name: str) -> None:
        """Call :func:`generate_image()` before this method."""
        file: TextIO  = open(file_name + ".svg", "w")
        file.write(self.image)



class BaseCSV(object):

    def __init__(self):
        super()
        self.HEIGHT = 200
        self.WIDTH = 200
        self.baseString: str = ""


    def wrap_with_img_base(self, img: str) -> str:
        return self.__make_img_header() + img + self.__make_img_footer()


    def __make_img_header(self) -> str:
        header: str = f"<svg height=\"{self.HEIGHT}\" width=\"{self.WIDTH}\" xmlns=\"http://www.w3.org/2000/svg\">\n"
        return header


    @staticmethod
    def __make_img_footer() -> str:
        return "</svg>"

