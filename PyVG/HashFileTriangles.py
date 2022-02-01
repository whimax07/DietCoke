from dataclasses import dataclass

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


def hash_file() -> int:
    return 0xe2ae1d1492501ee34a4acb4913e3d8f0bf19d5b31498793f5a4cc94ccb542282e508a6c7c64be5cc5850a821f2dcf970760c7c8d9a4935f79ad2cdd097d2219e


def make_list(file_hash: int) -> list[int]:
    int_str = "{0:0{1}x}".format(file_hash, 512)
    number_list = []
    last_c = ""
    for c in int_str:
        if last_c == "":
            last_c = c
            continue
        number_list.append(int(last_c + c, 16))
        last_c = ""

    return number_list


def build_triangle_limits(points: list[int]) -> list[list[int]]:
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


def build_triangle_points(bounds: list[list[int]]) -> list[TrianglePoints]:
    triangles = []
    for limits in bounds:
        tri = [(limits[0], limits[2]), (limits[0], limits[3]), (limits[1], limits[2]), (limits[1], limits[3])]
        tri.pop(limits[4] % 4)
        triangle = TrianglePoints(tri[0], tri[1], tri[2], limits[4], limits[5])
        triangles.append(triangle)
    return triangles


def make_triangles(triangle_points: list[TrianglePoints]) -> BuildSVG:
    img_builder: BuildSVG = BuildSVG()
    for points in triangle_points:
        tri = Triangle().define_shape_tuples(points.point_a, points.point_b, points.point_c)
        tri.add_style("fill", get_rand_colour(points.concat_total))
        img_builder.add_shape(tri)

    return img_builder


def get_rand_colour(concat_total: int) -> str:
    return COLOURS[concat_total % len(COLOURS)]



def main():
    file_hash: int = hash_file()
    points: list[int] = make_list(file_hash)
    triangle_limits = build_triangle_limits(points)
    triangle_points = build_triangle_points(triangle_limits)
    img_builder = make_triangles(triangle_points)
    img_builder.generate_image()
    img_builder.write_image_file("HashedTriangles")



if __name__ == '__main__':
    main()