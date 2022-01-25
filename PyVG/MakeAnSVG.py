from PyVG.BuildSVG import BuildSVG
from PyVG.Shapes import Rectangle


def main():
    img_builder: BuildSVG = BuildSVG()

    rect: Rectangle = Rectangle()  \
                          .define_bounds(10, 10, 100, 100)  \
                          .add_style("stroke", "blue")  \
                          .add_style("stroke-width", "2")


    img_builder.add_shape(rect)
    img_builder.generate_image()
    img_builder.write_image_file("TestVG")



if __name__ == '__main__':
    main()

