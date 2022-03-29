import os
import pyray
from actors.background import Background
from services.keyboard_service import KeyboardService

# TEXTURE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/resources\pictures\cat_run.png"
FORWARD = 0
WALK = 1


class AnimationInfo:
    def __init__(self, frame_count, sprite_size, offset):
        self.frame_count = frame_count
        self.sprite_size = sprite_size
        self.offset = offset


class Player(Background):
    def __init__(self, file_path, pos_x, pos_y):
        Background.__init__(self, file_path, pos_x, pos_y)
        self._keyboard_service = KeyboardService()
        self._ground = pos_y
        self._animation_values = {(FORWARD, WALK): AnimationInfo(3, (195, 163), (0, 0))}
        self._timer = 0
        self._frame = 0
        self._player_direction = FORWARD
        self._player_action = WALK

    def move_player(self):
        delta_y = self._keyboard_service.get_direction()
        self._pos_y += delta_y
        if self._pos_y >= self._ground:
            self._pos_y = self._ground
            self._keyboard_service.clear_jump()

    def draw(self, frame_time):
        # self._texture =  pyray.load_texture(self._texture)


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
                pyray.Vector2(self._pos_x, self._pos_y),
                pyray.RAYWHITE
            )

    def animate_player(self):
        frame_time = pyray.get_frame_time()
        self.draw(frame_time)
