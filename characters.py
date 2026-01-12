import random
import arcade
from pymunk.examples.index_video import radius

from constants import TILE_SIZE
LEVEL_MAP = [
    "###########",
    "#P....G...#",
    "#.........#",
    "###########",
]

class Coin:
    def __init__(self,center_x,center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.value = 10

class Character(arcade.Sprite):
    def __init__(self,center_x,center_y,color):
        super().__init__()
        radius = TILE_SIZE // 2 - 2
        texture = arcade.make_circle_texture(radius*2,color)
        self.width = texture.width - 9
        self.height = texture.height - 9
        self.texture = texture
        self.center_x = center_x
        self.center_y = center_y
        self.speed = 0
        self.change_x = 0
        self.change_y = 0


class Player(Character):
    def __init__(self,center_x,center_y):
        super().__init__(center_x,center_y)
        self.score = 0
        self.lives = 3

    def move(self):
        self.center_x = self.change_x*self.speed
        self.center_y = self.change_y*self.speed

class Enemy(Character):
    def __init__(self,center_x,center_y):
        super().__init__(center_x,center_y)
        self.time_to_change_direction = 0

    def pick_new_direction(self):
        directions=[(0,1),(0,-1),(1,0),(-1,0),(0,0)]
        chosen_direction = random.choice(directions)
        self.change_y = chosen_direction[1]
        self.change_x = chosen_direction[0]
        self.time_to_change_direction = random.uniform(0.3, 1.0)

    def update(self):
        delta_time = 1 / 60
        self.time_to_change_direction -= delta_time
        if self.time_to_change_direction<=0:
            self.pick_new_direction()
        self.center_y += self.change_y * self.speed
        self.center_x += self.change_x * self.speed

class Wall:
    def __init__(self,center_x,center_y):
        self.center_x = center_x
        self.center_y = center_y
