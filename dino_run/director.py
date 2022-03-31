#desert background from: https://opengameart.org/content/cethiels-desert-background-redux
# cactus also from https://opengameart.org
from random import randint
import pyray
import time
# import pygame
# from pygame.locals import *


class Director():
    def __init__(self, keyboard_service, video_service, cactus_1, cactus_2, player, background):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cactus_1 = cactus_1
        self._cactus_2 = cactus_2
        self._background = background
        self._player = player
        self._is_game_over = False
        # self._clock = pygame.time.Clock()

    def start_game(self):
        self._video_service.open_window() 
        self._background.load_texture()  
        self._cactus_1.load_texture()
        self._cactus_2.load_texture()
        self._player.load_texture()
        # self._clock.tic()

        while self._video_service.is_window_open() and not self._is_game_over:
            self._do_updates()
            self._do_outputs()
        self.game_over()
        time.sleep(5)
        self._video_service.close_window()    

    def _do_updates(self):
        self._cactus_1.move_cactus()
        self._cactus_1.reset_cactus()
        self._cactus_2.move_cactus()
        self._cactus_2.reset_cactus()
        self._player.move_player()
        self.ck_cactus_overlap()
        self.ck_collision()
        self.game_over()     

    def _do_outputs(self):
        self._video_service.clear_buffer()
        self._background.draw_self()
        self._cactus_1.draw_self()
        self._cactus_2.draw_self()
        self._player.animate_player()
        self._video_service.flush_buffer()

    def ck_cactus_overlap(self):
        # this ensures that the cacti aren't generated so close together that the player can't jump between them. 
        if abs(self._cactus_2._pos_x - self._cactus_1._pos_x) <= 400:
            self._cactus_2._pos_x = randint(818, 1800)

    def ck_collision(self):
        # This function reads the position values of the cactus and the player when they collide
        cactus1_pos = abs(self._cactus_1._pos_x)
        cactus2_pos = abs(self._cactus_2._pos_x)
        player_pos = abs(self._player._pos_y)

        # This section runs for every frame when the cactus collides with the player, it should stop once self._is_game_over is True
        if (cactus1_pos >= 60 and cactus1_pos <= 107 and player_pos >= 415) or (cactus2_pos >= 60 and cactus2_pos <= 107 and player_pos >= 415 ):
            self._is_game_over = True
            # print ("Game Over!")
            # print ("Cactus 1:" + str(self._cactus_1._pos_x) + "," + str(self._cactus_1._pos_y))
            # print ("Cactus 2:" + str(self._cactus_2._pos_x) + "," + str(self._cactus_2._pos_y))
            # print ("Player:" + str(self._player._pos_x) + "," + str(self._player._pos_y))

    def game_over(self):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            # Not working
            # milli = self._clock.tic()
            # sec = milli / 1000
            pyray.draw_text("Game Over!", 20, 20, 140, pyray.VIOLET)
            # pyray.draw_text(f"{sec}", 20, 180, 100, pyray.VIOLET)
            pyray.end_drawing()
