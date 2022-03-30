import os
import player
import pyray

WIDTH = 800
HEIGHT = 450
TEXTURE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/cat_run.png"

class Game:
    def __init__(self):
        # Set up the window
        pyray.init_window(WIDTH, HEIGHT, "Running Test")
        pyray.set_target_fps(60)
        self._player = player.Player()

    def run(self):
            # Main loop
            CHARACTER = pyray.load_texture(TEXTURE_PATH)
            while not pyray.window_should_close():
                pyray.begin_drawing()
                pyray.clear_background(pyray.RAYWHITE)

                frame_time = pyray.get_frame_time()
                self._player.draw(frame_time)
                pyray.end_drawing()


            # clean up
            pyray.close_window()

if __name__ == '__main__':
    game = Game()
    game.run()