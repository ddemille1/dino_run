import pyray

class Timer:
    """ This times the amount of time elapsed since the window has opened and displays it on the screen
    
    Attributes:
        _frame_time_str(str): The amount of time that has elapsed since the window has been opened."""
    def __init__(self):
        """Creates an instance of the Timer class."""
        self._frame_time_str = ''

    def get_frame_time(self):
        """This method gets the time elapsed since the window has opened. It rounds the number to decimal points and then converts it into a string.
        
        Returns:
            _frame_time_str(str): This is a string representing the amount of time elapsed since the window was opened. """

        frame_time_int = pyray.get_time()
        frame_time_float = round(frame_time_int, 2)
        self._frame_time_str = str(frame_time_float)
        return self._frame_time_str
        
    def draw_timer(self):
        """This method traws the timer on the screen."""
        
        pyray.draw_text(self._frame_time_str, 10, 10, 20, pyray.BLACK)
                
