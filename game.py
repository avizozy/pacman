"""
מודול הלוגיקה הראשית של משחק הפקמן.

מכיל את המחלקה:
- PacmanGame: ניהול מצב המשחק, ציור, עדכון ותשובת מקלדת.
"""
import arcade
from constants import TILE_SIZE,WINDOW_TITLE,WINDOW_WIDTH,WINDOW_HEIGHT,LEVEL_MAP
from characters import Wall,Coin,Character,Enemy,Player
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
                    wall_to_append = arcade.Sprite(Wall(x,y))
                    self.wall_list.append(wall_to_append)
                elif LEVEL_MAP[row_idx][col_idx] == ".":
                    coin_to_append = arcade.Sprite(Coin(x,y))
                    self.coin_list.append(coin_to_append)
                elif LEVEL_MAP[row_idx][col_idx] == "P":
                    player_to_append = arcade.Sprite(Player(x,y))
                    self.player_list.append(player_to_append)
                elif LEVEL_MAP[row_idx][col_idx] == "G":
                    ghost_to_append = arcade.Sprite(Enemy(x,y))
                else:
                    print("Not valid")
    def on_draw(self):



