import pyray

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 

    Attribures:
        _caption(str): The title to be displayed on the window.
        _screen_width (int): The width in pixles of the window.
        _screen_height (int): The height in pixles of the window.
        _frame_rate (int): The frame rate for the window.

    """


    def __init__(self, caption, screen_width, screen_height, frame_rate):
        """Constructs a new VideoService.
        
        Args:
            caption(str): The title to be displayed on the window.
            screen_width (int): The width in pixles of the window.
            screen_height (int): The height in pixles of the window.
            frame_rate (int): The frame rate for the window.
        """
    
        self._caption = caption
        self._screen_width = screen_width
        self._screen_height = screen_height
        self._frame_rate = frame_rate

    def close_window(self):
        """Closes the window and releases all computing resources."""

        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase."""
        
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """
        pyray.end_drawing()

    def is_window_open(self):
        """Checks whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided width, height, caption, and frame rate.
        """
        pyray.init_window(self._screen_width, self._screen_height, self._caption)    
        pyray.set_target_fps(self._frame_rate)