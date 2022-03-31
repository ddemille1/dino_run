import pyray
import os

TEXTURE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/cat_run.png"

class Game:
    def __init__ (self):
        # Set up window
        pyray.init_window(800, 450, "Walking Test")
        pyray.set_target_fps(60)

    def run(self):
        # Load character picture (texture)
        CHARACTER = pyray.load_texture(TEXTURE_PATH)

        # Main loop
        while not pyray.window_should_close():
            pyray.begin_drawing()
            pyray.clear_background(pyray.RAYWHITE)
            pyray.draw_text ("Congrats! You created your first window!", 190, 200, 20, pyray.LIGHTGRAY)
            
            # Draw texture (first step)
            pyray.draw_texture_rec(
                CHARACTER,
                pyray.Rectangle(0, 0, 195, 163),
                pyray.Vector2(20.0, 20.0),
                pyray.RAYWHITE
            )

            # Draw texture (feet together)
            pyray.draw_texture_rec(
                CHARACTER,
                pyray.Rectangle(195, 0, 195, 163),
                pyray.Vector2(250.0, 20.0),
                pyray.RAYWHITE
            )

            # Draw texture (second step)
            pyray.draw_texture_rec(
                CHARACTER,
                pyray.Rectangle(390, 0, 195, 163),
                pyray.Vector2(500.0, 20.0),
                pyray.RAYWHITE
            )

            pyray.end_drawing()

        pyray.close_window()

if __name__ == "__main__":
    game = Game()
    game.run()