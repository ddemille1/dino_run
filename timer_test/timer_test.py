import os
import pyray

WIDTH = 800
HEIGHT = 450

class Game:
    def __init__(self):
        # Set up the window
        pyray.init_window(WIDTH, HEIGHT, "clock test")
        pyray.set_target_fps(60)
        
        
    
    def run(self):
            # Main loop
            
            
            while not pyray.window_should_close():
                pyray.begin_drawing()
                pyray.clear_background(pyray.RAYWHITE)
                
                #code to get time and display it: 
                frame_time_int = pyray.get_time()
                frame_time_float = round(frame_time_int, 2)
                frame_time_str = str(frame_time_float)
                print(frame_time_str)
                pyray.draw_text(frame_time_str, 10, 10, 20, pyray.BLACK)
                
                pyray.end_drawing()


            # clean up
            pyray.close_window()

if __name__ == '__main__':
    game = Game()
    game.run()