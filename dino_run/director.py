#desert background from: https://opengameart.org/content/cethiels-desert-background-redux
# cactus also from https://opengameart.org



class Director():
    def __init__(self, keyboard_service, video_service, cactus, background):
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._cactus = cactus
        self._background = background

    def start_game(self):
        self._video_service.open_window() 
        self._background.load_texture()  
        self._cactus.load_texture()

        while self._video_service.is_window_open(): 
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
        self._video_service.close_window()    

    def _get_inputs(self):
        pass

    def _do_updates(self):
        pass

    def _do_outputs(self):
        self._video_service.clear_buffer()
        self._background.draw_self()
        self._cactus.draw_self()
        self._video_service.flush_buffer()

