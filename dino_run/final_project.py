#desert background from: https://opengameart.org/content/cethiels-desert-background-redux

import pyray

def main():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 533

    pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'raylib [core] example - basic window')
    texture2D_background = pyray.load_texture('picture.jpg')
    scrolling_back = float(0.0)

    pyray.set_target_fps(60)

    while not pyray.window_should_close():
        scrolling_back -= 1
        if scrolling_back <= -400*2:
             scrolling_back = 0

        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        pyray.draw_texture(texture2D_background, 0, 0, pyray.WHITE)
        #pyray.draw_texture_ex(texture2D_background, [scrolling_back, 20], 0, 1, pyray.BLANK)
        #pyray.draw_texture_ex(texture2D_background, [400*2 + scrolling_back, 20], 0, 1, pyray.BLANK)
        #pyray.draw_text('Congratulations! You created your first window!' 190, 200, 20, LIGHTGRAY)
        pyray.end_drawing()
    pyray.close_window()

if __name__ == "__main__":
    main()
