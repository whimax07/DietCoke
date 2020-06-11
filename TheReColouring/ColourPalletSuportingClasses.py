

class APalletColour(object):
    '''Initialise the class with one colour described with one of the
    following forms:
    1) rgb1 = rgb, A list of 3 numbers from 0 to 1.
    2) rgb255 = RGB, A list of 3 intergers between 0 and 255.
    3) Hex = Hex Colour Code, A string of length 7 beging with a "#".
    4) hsl = hsl, A list of 3 numbers corresponding to hue 0 to 360, saturation
    and luminace both 0 to 1.'''
    def __init__(self, rgb1=None, rgb255=None, Hex=None, hsl=None):
        # Take the init input and construct all ways of describing  a colour
        # using that.
        self.Translation(rgb1, rgb255, Hex, hsl)

    def RgbUpdate(self, col=None, red=None, green=None, blue=None):
        newCol = self.rgb1
        if col is not None:
            Translation(rgb1=col)
        elif red is not None:
            newCol[0] = red
            Translation(rgb1=newCol)
        elif green is not None:
            newCol[1] = green
            Translation(rgb1=newCol)
        elif blue is not None:
            newCol[2] = blue
            Translation(rgb1=newCol)

    def HslUpdate(self, col=None, hue=None, saturation=None, luminace=None):
        newCol = self.hsl
        if col is not None:
            Translation(hsl=col)
        elif hue is not None:
            newCol[0] = hue
            Translation(hsl=newCol)
        elif saturation is not None:
            newCol[1] = saturation
            Translation(hsl=newCol)
        elif luminace is not None:
            newCol[2] = luminace
            Translation(hsl=newCol)

    def Translation(self, rgb1=None, rgb255=None, Hex=None, hsl=None):
        if hsl is not None:
            hsl[0] = hsl[0] % 360
            self.hsl = hsl
            state = 0
        elif rgb255 is not None:
            self.rgb255 = rgb255
            state = 1
        elif Hex is not None:
            self.Hex = Hex
            state = 2
        elif rgb1 is not None:
            self.rgb1 = rgb1
            state = 3
        else:
            raise TypeError('No arguments were passed or all were "None".')

        count = 0
        # Count ends at 3 because we start with one format already given.
        while count < 3:
            if state == 0:
                self.rgb255 = self.hsl2RGB(self.hsl)
                state = (state + 1) % 4
                count += 1
            elif state == 1:
                self.Hex = self.RGB2Hex(self.rgb255)
                state = (state + 1) % 4
                count += 1
            elif state == 2:
                self.rgb1 = self.Hex2rgb(self.Hex)
                state = (state + 1) % 4
                count += 1
            elif state == 3:
                self.hsl = self.rgb2hsl(self.rgb1)
                state = (state + 1) % 4
                count += 1

    def hsl2RGB(self, hsl):
        hue = hsl[0] / 360
        saturation = hsl[1]
        luminace = hsl[2]

        if saturation == 0:
            return [saturation * 255] * 3

        if luminace < 0.5:
            temp1 = luminace * (1 + saturation)
        else:
            temp1 = luminace + saturation - luminace * saturation

        temp2 = 2 * luminace - temp1
        tempC = [hue + 1/3 % 1, hue, hue - 1/3 % 1]

        out = list()
        for col in tempC:
            if 6 * col < 1:
                out.append(temp2 + (temp1 - temp2) * 6 * col)
            elif 2 * col < 1:
                out.append(temp1)
            elif 3 * col < 2:
                out.append(temp2 + (temp1 - temp2) * (2/3 - col) * 6)
            else:
                out.append(temp2)
        out = [round(i * 255) for i in out]
        return out

    def RGB2Hex(self, rgb255):
        val = [hex(i) for i in rgb255]
        Hex = '#'
        for i in val:
            i = i[2:]
            Hex = Hex + '{:0>2}'.format(i)
        return Hex

    def Hex2rgb(self, Hex):
        Hex = Hex[1:]
        rgb255 = [0, 0, 0]
        for i in range(3):
            val = Hex[i * 2: i * 2 + 2]
            rgb255[i] = int(val, 16)
        rgb1 = [i / 255 for i in rgb255]
        return rgb1

    def rgb2hsl(self, rgb1):
        low = min(rgb1)
        big = max(rgb1)
        luminace = (low + big) / 2
        # If low = big then the colour is a grey
        if low == big:
            return [0, 0, luminace]

        if luminace < 0.5:
            saturation = (big - low) / (low + big)
        else:
            saturation = (big - low) / (2 - big - low)

        idx = rgb1.index(max(rgb1))
        if idx == 0:
            hue = (rgb1[1] - rgb1[2]) / (big - low)
        elif idx == 1:
            hue = 2 + (rgb1[2] - rgb1[0]) / (big - low)
        else:
            hue = 4 + (rgb1[0] - rgb1[1]) / (big - low)

        hue = (hue * 60) % 360
        return [hue, saturation, luminace]

    def __str__(self, Format=None):
        rgb1S = self.Colour2Str(rgb1=self.rgb1)
        rgb255S = self.Colour2Str(rgb255=self.rgb255)
        HexS = self.Colour2Str(Hex=self.Hex)
        hslS = self.Colour2Str(hsl=self.hsl)
        out = '\n------------------------------------------------------'
        if Format is None:
            out = out + '\nIn rgb the colour is: ' + rgb1S + \
                '\nIn RGB the colour is: ' + rgb255S + \
                '\nIn Hex the colour is: ' + HexS + \
                '\nIn hsl the colour is: ' + hslS
        elif Format in {'rgb', 'rgb1'}:
            out = out + '\nIn rgb the colour is: ' + rgb1S
        elif Format in {'RGB', 'rgb255'}:
            out = out + '\nIn RGB the colour is: ' + rgb255S
        elif Format == 'Hex':
            out = out + '\nIn Hex the colour is: ' + HexS
        elif Format == 'hsl':
            out = out + '\nIn hsl the colour is: ' + hslS
        out = out + \
            '\n------------------------------------------------------\n'
        return out

    def Colour2Str(self, rgb1=None, rgb255=None, Hex=None, hsl=None):
        colStr = list()
        if rgb1 is not None:
            return '[{:.2f}, {:.2f}, {:.2f}]'.format(*rgb1)
        elif rgb255 is not None:
            return '[{}, {}, {}]'.format(*rgb255)
        elif Hex is not None:
            return Hex
        elif hsl is not None:
            return '[{:.0f}, {:.1%}, {:.1%}]'.format(*hsl)


if __name__ == "__main__":
    a = APalletColour(Hex='#0a141e')
    print(a)
