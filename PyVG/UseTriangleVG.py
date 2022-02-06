from PyVG.HashFileTriangles import *


def make_all_none():
    make_triangle_hash()


def yellow_fg_blue_bg():
    make_triangle_hash(foreground_colours=YELLOWS, background_colour="rgb(25,25,80)")


def blue_fg_yellow_bg():
    # make_triangle_hash(foreground_colours=BLUES, background_colour="Orange")
    # make_triangle_hash(foreground_colours=BLUES, background_colour="Khaki") # Good.
    make_triangle_hash(foreground_colours=BLUES, background_colour="LemonChiffon")



def main():
    blue_fg_yellow_bg()


if __name__ == '__main__':
    main()
