import pyray


class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self):
        """Constructs a new KeyboardService using the specified cell size.

        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._dx = 0
        # v = velocity
        self._v = 0
        # m = mass
        self._m = 1
        self._jump = False
        self._initial_jump_velocity = -9

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            force: The change in y.
        """
        if pyray.is_key_down(pyray.KEY_SPACE):
            if not self._jump:
                self._jump = True
                self._v = self._initial_jump_velocity

        if self._jump:
            force = (1 / 2) * self._m * (self._v **2)
            if self._v < 0:
                force *= -1
            self._v = self._v + 0.4
        else:
            force = 0

        force = int(force)

        return force

    def clear_jump(self):
        self._jump = False
