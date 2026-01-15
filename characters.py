import random
import arcade


from constants import TILE_SIZE
player_texture=arcade.make_soft_circle_texture(TILE_SIZE,arcade.color.YELLOW,255,255)
enemy_texture=arcade.make_soft_circle_texture(TILE_SIZE,arcade.color.RED,255,255)
coin_texture=arcade.make_soft_circle_texture(TILE_SIZE//6,arcade.color.YELLOW,255,255)
wall_texture = arcade.make_soft_square_texture(TILE_SIZE,arcade.color.BLUE,255,255)
class Coin(arcade.Sprite):
    def __init__(self,center_x,center_y,texture):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.texture=texture
        self.value = 10

class Character(arcade.Sprite):
    def __init__(self,center_x,center_y,texture):
        super().__init__()
        self.center_x = center_x
        self.texture=texture
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.center_y = center_y
        self.speed = 0
        self.change_x = 0
        self.change_y = 0


class Player(Character):
    def __init__(self,center_x,center_y,texture):
        super().__init__(center_x,center_y,texture)
        self.score = 0
        self.lives = 3

    def move(self):
        self.center_x = self.change_x*self.speed
        self.center_y = self.change_y*self.speed

class Enemy(Character):
    def __init__(self,center_x,center_y,texture):
        super().__init__(center_x,center_y,texture)
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

class Wall(arcade.Sprite):
    def __init__(self,center_x,center_y,texture):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.texture = texture
