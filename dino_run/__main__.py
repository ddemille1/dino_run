
import os
from random import randint
from actors.background import Background
from actors.cactus import Cactus
from actors.player import Player
from actors.timer import Timer
from director import Director
from services.keyboard_service import KeyboardService
from services.video_service import VideoService

#constants and filepaths for use in the game
SCREEN_WIDTH = 818
SCREEN_HEIGHT = 640
FRAME_RATE = 60
CAPTION = 'Cat Run!'
BACKGROUND = os.path.dirname(os.path.abspath(__file__)) + "/resources\pictures\cethiel-desert-edit.png"
CACTUS = os.path.dirname(os.path.abspath(__file__)) + '/resources\pictures\small_cactus.png'
PLAYER = os.path.dirname(os.path.abspath(__file__)) + '/resources\pictures\cat_resized.png'

def main():
    """The entry point for the game."""

    #create background
    background = Background(BACKGROUND, 0, 0)

    #create cacti. They are generated at random intervals to the right of the screen along the x-axis
    cactus_1 = Cactus(CACTUS, randint(818, 1800), 500)
    cactus_2 = Cactus(CACTUS, randint(818, 1800), 500)

    # Create the cat 
    player = Player(PLAYER, 60, 500)
    print ("Player loaded")

    # Create the timer
    timer = Timer()

    # start game
    keyboard_service = KeyboardService()
    video_service = VideoService(CAPTION, SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)
    director = Director(keyboard_service, video_service, cactus_1, cactus_2, player, background, timer)
    director.start_game()


if __name__ == "__main__":
    main()