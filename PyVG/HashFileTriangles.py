import hashlib
from pathlib import Path
from dataclasses import dataclass
from tkinter import filedialog
from typing import Union

from PyVG.BuildSVG import BuildSVG
from PyVG.Shapes import Triangle

COLOURS = ["AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "BlanchedAlmond",
           "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse", "Chocolate", "Coral",
           "CornflowerBlue", "Cornsilk", "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod", "DarkGray",
           "DarkGrey", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid",
           "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray", "DarkSlateGrey",
           "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DimGrey", "DodgerBlue",
           "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "GoldenRod",
           "Gray", "Grey", "Green", "GreenYellow", "HoneyDew", "HotPink", "IndianRed", "Indigo", "Ivory", "Khaki",
           "Lavender", "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral", "LightCyan",
           "LightGoldenRodYellow", "LightGray", "LightGrey", "LightGreen", "LightPink", "LightSalmon",
           "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSlateGrey", "LightSteelBlue", "LightYellow",
           "Lime", "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquaMarine", "MediumBlue", "MediumOrchid",
           "MediumPurple", "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise",
           "MediumVioletRed", "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy",
           "OldLace", "Olive", "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenRod", "PaleGreen",
           "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink", "Plum", "PowderBlue",
           "Purple", "RebeccaPurple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown",
           "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue", "SlateGray", "SlateGrey", "Snow",
           "SpringGreen", "SteelBlue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White",
           "WhiteSmoke", "Yellow", "YellowGreen"]


@dataclass
class TrianglePoints:
    point_a: tuple[int, int]
    point_b: tuple[int, int]
    point_c: tuple[int, int]
    decider: int
    concat_total: int


def __hash_file() -> [str, str]:
    file_path_string = filedialog.askopenfilename()

    if file_path_string is None:
        print("File selection quit.")
        exit(1)

    buf_size = 65536
    sha512 = hashlib.sha3_512()

    with open(file_path_string, 'rb') as file:
        while True:
            data = file.read(buf_size)
            if not data:
                return sha512.hexdigest(), Path(file_path_string).stem
            sha512.update(data)


def __make_list(file_hash: Union[int, str]) -> list[int]:
    int_str: str
    if isinstance(file_hash, int):
        int_str = "{0:0{1}x}".format(file_hash, 512)
    else:
        int_str = file_hash

    number_list = []
    last_c = ""
    for c in int_str:
        if last_c == "":
            last_c = c
            continue
        number_list.append(int(last_c + c, 16))
        last_c = ""

    return number_list


def __build_triangle_limits(points: list[int]) -> list[list[int]]:
    tris = []
    tri = []
    for p in points:
        if len(tri) < 4:
            tri.append(p)
            continue

        sum_t = sum(tri)
        tri.append(sum_t)
        concat_t = tri[3] << 24 + tri[2] << 16 + tri[1] << 8 + tri[0]
        tri.append(concat_t)
        tris.append(tri)
        tri = []

    return tris


def __build_triangle_points(bounds: list[list[int]]) -> list[TrianglePoints]:
    triangles = []
    for limits in bounds:
        tri = [(limits[0], limits[2]), (limits[0], limits[3]), (limits[1], limits[2]), (limits[1], limits[3])]
        tri.pop(limits[4] % 4)
        triangle = TrianglePoints(tri[0], tri[1], tri[2], limits[4], limits[5])
        triangles.append(triangle)
    return triangles


def __make_triangles(triangle_points: list[TrianglePoints]) -> BuildSVG:
    img_builder: BuildSVG = BuildSVG()
    for points in triangle_points:
        tri = Triangle().define_shape_tuples(points.point_a, points.point_b, points.point_c)
        tri.add_style("fill", __get_rand_colour(points.concat_total))
        img_builder.add_shape(tri)

    return img_builder


def __get_rand_colour(concat_total: int) -> str:
    return COLOURS[concat_total % len(COLOURS)]



def main():
    file_hash: str
    file_name: str
    file_hash, file_name = __hash_file()
    points: list[int] = __make_list(file_hash)
    triangle_limits = __build_triangle_limits(points)
    triangle_points = __build_triangle_points(triangle_limits)
    img_builder = __make_triangles(triangle_points)
    img_builder.generate_image()
    img_builder.write_image_file(file_name + "TriangleHashed")



if __name__ == '__main__':
    main()