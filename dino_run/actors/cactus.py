from actors.background import Background
from random import randint

class Cactus(Background):
    # def __init__(self, pos_x):
    #     self._pos_x = pos_x
  
    def move_cactus(self):
        #print(self._pos_x)
        self._pos_x -= 6
        return self._pos_x
    
    def reset_cactus(self):
        if self._pos_x < 0:
            self._pos_x = randint(818, 1800)
        return self._pos_x

    # def get_pos_x(self):
    #     print(self._pos_x)
    #     #return self._pos_x