from PIL import Image
import os


class WI:
    def __init__(self, path='imgs/tests/img.jpg'):
        self.path = path
        self.img = Image.open(path)

    def Save(self, thumbnail=False, dim=(512, 512), path='imgs/tests/result/', exst='png', name='img'):
        if thumbnail: self.img.thumbnail(dim)
        else: self.img = self.img.resize(dim)

        Name = name.split('.')[0] + '.' + exst
        i=0
        while Name in os.listdir(path):
            Name = name.split('.')[0] + str(i) + '.' + exst
            i += 1

        self.img.save(path + '/' + Name)

    def Show(self, img=''):
        if img == '': img = self.img
        img.show('Result')


if __name__ == '__main__':
    WI().Save(name='resize')
    WI().Show()
    WI().Save(True, name='thumbnail')
    WI().Show()
