
import pyray


class Background():
    """ This will serve as the parent class to the cactus and dinosaur"""

    def __init__(self, file_path, pos_x, pos_y):

        self._file_path = file_path
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._texture = []

    def load_texture(self):
        self._texture = pyray.load_texture(self._file_path)

    def draw_self(self):
        pyray.draw_texture(self._texture, self._pos_x, self._pos_y, pyray.RAYWHITE)
