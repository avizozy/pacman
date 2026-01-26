"""
נקודת הכניסה למשחק פקמן.

אחראית על:
- יצירת חלון Arcade
- יצירת אובייקט PacmanGame
- אתחול המשחק
- הרצת לולאת המשח
"""

from game import *
from constants import *
import arcade

def main():
    """פונקציית main שמריצה את המשחק."""
    arcade.play_sound(arcade.load_sound("assets/pacman_sound.mp3"))
    window = arcade.Window(WINDOW_WIDTH,WINDOW_HEIGHT)
    pacmen_game = PacmanGame()
    window.show_view(pacmen_game)
    pacmen_game.setup()
    arcade.run()


if __name__ == "__main__":
    main()