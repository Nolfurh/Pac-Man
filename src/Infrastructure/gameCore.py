
class GameSettings():
    """
    A class that defines the settings for a Pacman game.

    Attributes
    ----------
    screen_width : int
        The width of the game screen in pixels.
    screen_height : int
        The height of the game screen in pixels.
    map_background : tuple
        The RGB color of the map background as a tuple of integers.
    map_dots_color : str
        The color of the dots on the map as a string.
    map_lines_color : str
        The color of the lines on the map as a string.
    map_lines_door : str
        The color of the door lines on the map as a string.
    pacman_speed : float
        The speed of Pacman in pixels per frame.
    pacman_x : int
        The starting x-coordinate of Pacman on the map.
    pacman_y : int
        The starting y-coordinate of Pacman on the map.
    time_to_fruit_appearing1 : int
        The time in seconds before the first fruit appears.
    time_to_fruit_appearing2 : int
        The time in seconds before the second fruit appears.
    ghosts_speed : float
        The speed of the ghosts in pixels per frame.
    blinky_x : int
        The starting x-coordinate of Blinky on the map.
    blinky_y : int
        The starting y-coordinate of Blinky on the map.
    inky_x : int
        The starting x-coordinate of Inky on the map.
    inky_y : int
        The starting y-coordinate of Inky on the map.
    clyde_x : int
        The starting x-coordinate of Clyde on the map.
    clyde_y : int
        The starting y-coordinate of Clyde on the map.
    pinky_x : int
        The starting x-coordinate of Pinky on the map.
    pinky_y : int
        The starting y-coordinate of Pinky on the map.
    froze : int
        The duration of time that the ghosts will be frozen in seconds when Pacman eats a power pellet.

    Methods
    -------
    init()
        Initializes the game settings with default values.
    """

    def __init__(self):
        """
        Initializes the game settings with default values.
        """

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
