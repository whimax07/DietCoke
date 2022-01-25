from math import floor
from random import random


def ChoseMap():
    maps = ['Biotics Lab', 'Black Forest', 'Burning Paris', 'Catacombs',
            'Containment Station', 'Evacuation Point', 'Farmhouse',
            'Hellmark Station', 'Hostile Grounds', 'Infernal Realm',
            'Lockdown', 'Monster Ball', 'Nuked', 'Outpost', 'Prison',
            'Shopping Spree', 'Spillway', 'The Tragic Kingdom',
            'Volter Manor', 'ZED Landing', 'Krampus Lair', 'Nightmare',
            'Power Core', 'The Descent', 'Airship', 'Santa''s Workshop']
    i = random() * (len(maps) - 1)
    i = floor(i)
    print(maps[i])


if __name__ == "__main__":
    ChoseMap()
