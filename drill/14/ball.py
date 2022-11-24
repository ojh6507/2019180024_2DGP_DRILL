import game_world
import server
from pico2d import *
import random
class BALL:
    image = None
    def __init__(self):
        if BALL.image == None:
            BALL.image = load_image('ball21x21.png')
        self.x = random.randint(25, server.background.w - 1 -25)
        self.tx = self.x
        self.y = random.randint(25, server.background.h - 1 -25)
        self.ty = self.y
    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)
    def update(self):
        pass
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            try:
                game_world.remove_object(self)
            except:
                pass
