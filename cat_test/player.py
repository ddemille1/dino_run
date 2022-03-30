import os
import pyray
from enum import Enum

WIDTH = 800
HEIGHT = 450
TEXTURE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/cat_run.png"


class Direction(Enum):
    FORWARD = 0

class Action(Enum):
    WALK = 1

class AnimationInfo:
    def __init__(self, frame_count, sprite_size, offset):
        self.frame_count = frame_count
        self.sprite_size = sprite_size
        self.offset = offset

class Player:
    """ Create a new player running """
    def __init__(self, texture = TEXTURE_PATH):

        self._texture =  pyray.load_texture(texture)

        self._animation_values = {}
        self._animation_values[(Direction.FORWARD, Action.WALK)] = AnimationInfo(3, (195,163), (0,0))
        
        self._timer = 0
        self._frame = 0
        self._player_direction = Direction.FORWARD
        self._player_action = Action.WALK

        self._position = (40, 150)

    def set_direction(self, direction):
        self._player_direction = direction

    def set_action(self, action):
        self._player_action = action

    def draw(self, frame_time):
        self._timer += frame_time
        animation_values = self._animation_values[(self._player_direction, self._player_action)]
        if (self._timer >= 0.1): 
            self._timer = 0.0
            self._frame += 1

        self._frame = self._frame % animation_values.frame_count
        o = animation_values.offset
        s = animation_values.sprite_size

        pyray.draw_texture_rec(
                self._texture,
                pyray.Rectangle(o[0] + self._frame * s[0], o[1], 
                             s[0], s[1]),
                pyray.Vector2(self._position[0], self._position[1]),
                pyray.RAYWHITE
            )