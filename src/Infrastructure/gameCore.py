

class GameSettings():
    def __init__(self):
        self.screen_width = 750
        self.screen_height = 800

        # first map settings
        self.map_background = (1, 1, 1)
        self.map_dots_color = 'white'
        self.map_lines_color = 'blue'
        self.map_lines_door = 'white'

        self.pacman_speed = 1.4
        self.pacman_x = 450
        self.pacman_y = 631

        self.ghosts_speed = 1.0
        self.blinky_x = 56
        self.blinky_y = 58
        self.inky_x = 400
        self.inky_y = 350
        self.clyde_x = 365
        self.clyde_y = 360
        self.pinky_x = 370
        self.pinky_y = 352
