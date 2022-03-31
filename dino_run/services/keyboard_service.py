import pyray
class KeyboardService:
    """Detects player input. 

    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        _dx (int): the x position
        _v (int): velocity of jump.
        _m (int): mass of player
        _jump (Bool): True if jumpint
        _initial_jump_velocity (int): initial velocity of the player's jump
    """

    def __init__(self):
        """Constructs a new KeyboardService using the given attributes."""

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
        """Returns the bool: False for when the player is not jumping. """
        
        self._jump = False