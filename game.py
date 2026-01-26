"""
מודול הלוגיקה הראשית של משחק הפקמן.

מכיל את המחלקה:
- PacmanGame: ניהול מצב המשחק, ציור, עדכון ותשובת מקלדת.
"""

import arcade
from constants import *
from characters import *


class PacmanGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player = None
        self.game_over = False
        self.background_color = arcade.color.BLACK
        self.start_x=0
        self.start_y=0

    def setup(self):
        rows = len(LEVEL_MAP)
        for row_idx, row in enumerate(LEVEL_MAP):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2
                if LEVEL_MAP[row_idx][col_idx] == "#":
                    wall_to_append = Wall(x,y,wall_texture)
                    self.wall_list.append(wall_to_append)
                elif LEVEL_MAP[row_idx][col_idx] == ".":
                    coin_to_append = Coin(x,y,coin_texture)
                    self.coin_list.append(coin_to_append)
                elif LEVEL_MAP[row_idx][col_idx] == "P":
                    player_to_append = Player(x,y,player_texture)
                    self.start_x = x
                    self.start_y = y
                    self.player_list.append(player_to_append)
                    self.player = player_to_append
                elif LEVEL_MAP[row_idx][col_idx] == "G":
                    ghost_to_append = Enemy(x,y,enemy_texture)
                    self.ghost_list.append(ghost_to_append)
                else:
                    print("Not valid")
    def on_draw(self):
        self.clear()
        if self.game_over is False:
            self.wall_list.draw()
            self.ghost_list.draw()
            self.coin_list.draw()
            self.player_list.draw()
            arcade.draw_text(f"{self.player.lives * "💛"}",0,WINDOW_HEIGHT//2,arcade.color.YELLOW)
            arcade.draw_text(f"Score {self.player.score}",0,WINDOW_HEIGHT//2-20,arcade.color.YELLOW,16)
        else:
            arcade.draw_text("The game is over",WINDOW_WIDTH//2,WINDOW_HEIGHT//2,arcade.color.YELLOW)
    def on_update(self,delta_time):
        if self.game_over is False:
            player_center_x = self.player.center_x
            player_center_y = self.player.center_y
            self.player.move()
            list_of_collision_walls_player = arcade.check_for_collision_with_list(self.player,self.wall_list)
            if len(list_of_collision_walls_player) > 0:
                self.player.center_x = player_center_x
                self.player.center_y = player_center_y
            for ghost in self.ghost_list:
                ghost_center_x=ghost.center_x
                ghost_center_y = ghost.center_y
                ghost.update(delta_time)
                list_of_collision_walls_ghost = arcade.check_for_collision_with_list(ghost,self.wall_list)
                if len(list_of_collision_walls_ghost) >0:
                    ghost.center_x = ghost_center_x
                    ghost.center_y = ghost_center_y
                    ghost.pick_new_direction()
            list_of_collision_coins_player = arcade.check_for_collision_with_list(self.player,self.coin_list)
            if len(self.coin_list) == 0:
                self.game_over = True
            for coin in list_of_collision_coins_player:
                self.player.score += coin.value
                coin.remove_from_sprite_lists()
            list_of_collision_ghosts_player = arcade.check_for_collision_with_list(self.player,self.ghost_list)
            if len(list_of_collision_ghosts_player) > 0:
                self.player.lives -=1
                self.player.center_x = self.start_x
                self.player.center_y = self.start_y
                if self.player.lives <= 0:
                    self.game_over = True
                    self.player.speed = 0

    def on_key_press(self,key,modifiers):
        if key== arcade.key.SPACE:
           return self.setup()
        elif key==arcade.key.UP:
             self.player.change_y = 1
        elif key==arcade.key.DOWN:
             self.player.change_y = -1
        elif key==arcade.key.RIGHT:
            self.player.change_x=1
        elif key == arcade.key.LEFT:
            self.player.change_x = -1

    def on_key_release(self,key,modifiers):
        if key==arcade.key.UP or key==arcade.key.DOWN:
            self.player.change_y=0
        elif key==arcade.key.RIGHT or key==arcade.key.LEFT:
            self.player.change_x = 0