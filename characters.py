"""
מודול הדמויות (Sprites) במשחק פקמן.

מכיל את המחלקות:
- Character: מחלקת בסיס לדמויות (שיתוף שדה speed וכו')
- Pacman: השחקן הראשי
- Ghost: רוחות שנעות בצורה רנדומלית
- Coin: מטבעות לאיסוף
- Wall: קירות שחוסמים תנועה
"""
class Coin(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.texture = arcade.make_soft_circle_texture(TILE_SIZE // 3,arcade.color.YELLOW,)
        self.width = TILE_SIZE // 3
        self.height = TILE_SIZE // 3
        self.center_x = x
        self.center_y = y
        self.value = 10
class Wall(arcade.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.texture = arcade.make_soft_square_texture(TILE_SIZE,arcade.color.BLUE)
            self.width = TILE_SIZE
            self.height = TILE_SIZE
            self.center_x = x
            self.center_y = y

class Character:
    def __init__(self, center_x, center_y, speed=1):
        self.center_x = center_x
        self.center_y = center_y
        self.speed = speed
        self.change_x = 0
        self.change_y = 0


class Player(Character):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, speed=1)
        self.score = 0
        self.lives = 3

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Enemy(Character):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, speed=1)
        self.time_to_change_direction = 0

    def pick_new_direction(self):
        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
        direction = random.choice(directions)
        self.change_x = direction[0]
        self.change_y = direction[1]
        self.time_to_change_direction = random.uniform(0.3, 1.0)

    def update(self, delta_time=1/60):
        self.time_to_change_direction -= delta_time

        if self.time_to_change_direction <= 0:
            self.pick_new_direction()

        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


