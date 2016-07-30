import array
import random
import struct
import sys

from opensimplex import OpenSimplex

class Game(object):
    def __init__(self):
        self.gen = OpenSimplex(random.randint(0, sys.maxint))

    def noise(self, nx, ny):
        return self.gen.noise2d(nx, ny) / 2.0 + 0.5

    def create_height_map(self, width, height):
        fwidth = float(width)
        fheight = float(height)
        result = array.array('B')
        for y in xrange(height):
            for x in xrange(width):
                nx = x / fwidth - 0.5
                ny = y / fheight - 0.5
                value = self.noise(10 * nx, 10 * ny)
                result.append(int(255 * value if value != 1.0 else 255))
        return result

if __name__ == '__main__':
    import pprint
    import PIL.Image
    image = PIL.Image.new('L', (640, 480))
    image.putdata(Game().create_height_map(640, 480))
    image.save('out.jpg')

