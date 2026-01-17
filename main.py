"""
נקודת הכניסה למשחק פקמן.

אחראית על:
- יצירת חלון Arcade
- יצירת אובייקט PacmanGame
- אתחול המשחק
- הרצת לולאת המשחק
"""
from game import *
import arcade

def main():
    """פונקציית main שמריצה את המשחק."""
    arcade.Window()
    pacmen_game = PacmanGame()
    pacmen_game.setup()
    pacmen_game.on_draw()
    arcade.run()


if __name__ == "__main__":
    main()
