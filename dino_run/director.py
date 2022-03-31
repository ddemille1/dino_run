#desert background from: https://opengameart.org/content/cethiels-desert-background-redux
# cactus also from https://opengameart.org
from random import randint
import pyray
import time
# import pygame
# from pygame.locals import *


class Director():
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _cactus_1 (Cactus): For generating the first cactus.
        _cactus_2 (Cactus): For generating the second cactus.
        _player (Player): For generating the player.
        _background (Background): For generating the background.
        _timer(Timer): For generating the timer
        _is_game_over(bool): For tracking if the game is running.
    """
    def __init__(self, keyboard_service, video_service, cactus_1, cactus_2, player, background, timer):
        """Constructs a new Director using the specified keyboard service, video service, cacti, player, background, and timer.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            cactus_1 (Cactus): An instance of Cactus.
            cactus_2 (Cactus): An instance of Cactus.
            player (Player): An instance of Player.
            background (Background): An instance of Background.
            timer(Timer): An instance of Timer
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cactus_1 = cactus_1
        self._cactus_2 = cactus_2
        self._player = player
        self._background = background
        self._timer = timer
        self._is_game_over = False
        

    def start_game(self):
        """Starts the game by using the main game loop."""
        
        self._video_service.open_window() 
        self._background.load_texture()  
        self._cactus_1.load_texture()
        self._cactus_2.load_texture()
        self._player.load_texture()

        while self._video_service.is_window_open() and not self._is_game_over:
            self._do_updates()
            self._do_outputs()
        self.game_over()
        time.sleep(5)
        self._video_service.close_window()    

    def _do_updates(self):
        """Updates the time elapsed since window opened. Updates the cacti and player's position. Resolves any overlap between cacti. Handles collisions between player and cacti. Ends game."""

        self._timer.get_frame_time()
        self._cactus_1.move_cactus()
        self._cactus_1.reset_cactus()
        self._cactus_2.move_cactus()
        self._cactus_2.reset_cactus()
        self._player.move_player()
        self.ck_cactus_overlap()
        self.ck_collision()
        self.game_over()     
        

    def _do_outputs(self):
        """Starts drawing. Draws background, cacti, player, timer, then ends drawing."""

        self._video_service.clear_buffer()
        self._background.draw_self()
        self._cactus_1.draw_self()
        self._cactus_2.draw_self()
        self._player.animate_player()
        self._timer.draw_timer()
        self._video_service.flush_buffer()

    def ck_cactus_overlap(self):
        """this ensures that the cacti aren't generated so close together that the player can't jump between them."""

        if abs(self._cactus_2._pos_x - self._cactus_1._pos_x) <= 400:
            self._cactus_2._pos_x = randint(818, 1800)

    def ck_collision(self):
        """This function checks for collisions between the cacti and player. If they collide it sets is_game_over to True."""

        #This section reads the position values of the cactus and the player when they collide
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
        """Shows the 'game over' message if the game is over."""

        if self._is_game_over:
            # Not working
            # milli = self._clock.tic()
            # sec = milli / 1000
            pyray.draw_text("Game Over!", 20, 20, 140, pyray.VIOLET)
            # pyray.draw_text(f"{sec}", 20, 180, 100, pyray.VIOLET)
            pyray.end_drawing()

    