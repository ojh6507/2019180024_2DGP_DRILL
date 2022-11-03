from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.y = 30
    def update(self):
        pass
    def set_y(self,newy):
        self.y = newy
    def draw(self):
        self.image.draw(400, self.y)


