#desert background from: https://opengameart.org/content/cethiels-desert-background-redux
# cactus also from https://opengameart.org
import pyray
from random import randint

class Director():
    def __init__(self, keyboard_service, video_service, cactus_1, cactus_2, background):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cactus_1 = cactus_1
        self._cactus_2 = cactus_2
        self._background = background
        # self._player = player

    def start_game(self):
        self._video_service.open_window() 
        self._background.load_texture()  
        self._cactus_1.load_texture()
        self._cactus_2.load_texture()

        while self._video_service.is_window_open(): 
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()    

    def _get_inputs(self):
        pass

    def _do_updates(self):
        self._cactus_1.move_cactus()
        self._cactus_1.reset_cactus()
        self._cactus_2.move_cactus()
        self._cactus_2.reset_cactus()
        self.ck_cactus_overlap()
        

    def _do_outputs(self):
        self._video_service.clear_buffer()
        self._background.draw_self()
        self._cactus_1.draw_self()
        self._cactus_2.draw_self()
        self._video_service.flush_buffer()

    
    
    def ck_cactus_overlap(self):
        # this ensures that the cacti aren't generated so close together that the player can't jump between them. 
        if abs(self._cactus_2._pos_x - self._cactus_1._pos_x) <= 150:
            self._cactus_2._pos_x = randint(818, 1800)
           