

class GameSettings():
    def __init__(self):
        self.screen_width = 750
        self.screen_height = 800

        # first map settings
        self.map_background = (1, 1, 1)
        self.map_dots_color = 'white'
        self.map_lines_color = 'blue'
        self.map_lines_door = 'white'

        self.pacman_speed = 1.0
        self.pacman_x = 450
        self.pacman_y = 631

        self.time_to_fruit_appearing1 = 15
        self.time_to_fruit_appearing2 = 35

        self.ghosts_speed = 1.0
        self.blinky_x = 310
        self.blinky_y = 380
        self.inky_x = 440
        self.inky_y = 330
        self.clyde_x = 310
        self.clyde_y = 330
        self.pinky_x = 440
        self.pinky_y = 380
        self.froze = 50
