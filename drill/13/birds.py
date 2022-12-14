from pico2d import *
import game_framework
import random

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class BIRD:
    image = None
    def __init__(self):
        if BIRD.image == None:
            BIRD.image = load_image('bird_animation.png')
        self. x, self.y = random.randint(0,800), random.randint(0,600)
        self.x_dir = 1
        self.y_dir = 1
        self.reflect = ' '
        self.clip = 4
        self.action = 0
        self.frame = random.randint(0,3)
    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * 184, self.action , 184, 169, 0, self.reflect, self.x, self.y, 50, 50)

    def update(self):
        #self.frame = (self.frame + 1) % self.clip
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.clip
        if self.frame == 0:
            self.action += 169
            self.clip = 5
            if self.action > 169 * 2:
                self.action = 0
                self.clip = 4
        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.y_dir * RUN_SPEED_PPS * game_framework.frame_time


        print(self.frame)
        self.x = clamp(25, self.x, 780)
        self.y = clamp(90,self.y,580)
        if self.x >= 780:
            self.x_dir = -1
            self.reflect = 'h'
        if self.x_dir == -1 and self.x <= 25:
            self.x_dir = 1
            self.reflect = ' '

        if self.y >= 580:
            self.y_dir = -1
        if self.y_dir == -1 and self.y <= 90:
            self.y_dir = 1