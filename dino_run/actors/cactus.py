from actors.background import Background
from random import randint

class Cactus(Background):
    """A child class of Background."""

  
    def move_cactus(self):
        """This moves the cactus from right to left across the screen."""
        
        self._pos_x -= 6
        return self._pos_x
    
    def reset_cactus(self):
        """When the cactus gets to the left side of the screen this resets the x position of the cactus. It will randomly be placed to the right of the screen between 818 and 1800 pixels. 
        
        Returns:
            _pos_x
            """

        if self._pos_x < 0:
            self._pos_x = randint(818, 1800)
        return self._pos_x
