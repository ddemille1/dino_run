
import os
from actors.background import Background
from actors.cactus import Cactus
from director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService


SCREEN_WIDTH = 818
SCREEN_HEIGHT = 640
FRAME_RATE = 60
CAPTION = 'Dino Run!'
BACKGROUND = os.path.dirname(os.path.abspath(__file__)) + "/resources\pictures\cethiel-desert-edit.png"
CACTUS = os.path.dirname(os.path.abspath(__file__)) + '/resources\pictures\small_cactus.png'

def main():
    #create background
    background = Background(BACKGROUND, 0, 0)

    #create cactus
    cactus = Cactus(CACTUS, 700, 500)

    # start game
    keyboard_service = KeyboardService()
    video_service = VideoService(CAPTION, SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)
    director = Director(keyboard_service, video_service, cactus, background)
    director.start_game()


if __name__ == "__main__":
    main()