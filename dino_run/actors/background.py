
import pyray


class Background:
    """ This loads and draws the given file at the specified position. This will serve as the parent class to the cactus and player.
    
    Attributes:
        _file_path(file): This is the path used to find the desired file.
        _pos_x (int): the horizontal location for the left side of the picture to be displayed.
        _pos_y (int): the vertical location for the top side of the picture to be displayed."""

    def __init__(self, file_path, pos_x, pos_y):
        """Constructs a new background.
        
        Args: 
            file_path(file): This is the path used to find the desired file.
            pos_x (int): the horizontal location for the left side of the picture to be displayed.
            pos_y (int): the vertical location for the top side of the picture to be displayed."""
            
        self._file_path = file_path
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._texture = []

    def load_texture(self):
        """This loads the texture specified by the given file path."""

        self._texture = pyray.load_texture(self._file_path)

    def draw_self(self):
        """This draws the dexture."""

        pyray.draw_texture(self._texture, self._pos_x, self._pos_y, pyray.RAYWHITE)