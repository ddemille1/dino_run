import pyray

class VideoService():


    def __init__(self, caption, screen_width, screen_height, frame_rate):
    
        self._caption = caption
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._frame_rate = frame_rate

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)

    def flush_buffer(self):
        pyray.end_drawing()

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(self._screen_width, self._screen_height, self._caption)    
        pyray.set_target_fps(self._frame_rate)