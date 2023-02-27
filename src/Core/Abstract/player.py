import pygame as pg
import pygame.transform

from src.Infrastructure.gameProcesses.statistics import Statistics
from  src.Infrastructure.gameProcesses import fruits, bonuses

class Pacman:
    """
    A class representing Pacman character in the game.
    It is responsible for controlling Pacman's movement, animation, and behavior in the game.

    Attributes:
    -----------
    screen : pygame.Surface
        The screen on which the Pacman object will be displayed.
    screen_rect : pygame.Rect
        A rectangular area that defines the dimensions of the screen.
    spritesheet : list
        A list containing Pacman's sprite images.
    current_sprite : int
        The current sprite index in the spritesheet list.
    image : pygame.Surface
        The image object for the current sprite.
    rect : pygame.Rect
        A rectangular area that defines the dimensions and location of the image on the screen.
    settings : Settings
        The game settings object.
    map_matrix : list
        A list containing the game map matrix.
    moving_right : bool
        A flag that indicates if Pacman is moving right.
    moving_left : bool
        A flag that indicates if Pacman is moving left.
    moving_up : bool
        A flag that indicates if Pacman is moving up.
    moving_down : bool
        A flag that indicates if Pacman is moving down.
    x : float
        The x-coordinate of the Pacman object on the screen.
    y : float
        The y-coordinate of the Pacman object on the screen.
    turns : list
        A list containing boolean values that indicate if Pacman can make a turn in each direction.
    clock : pygame.time.Clock
        A clock object to keep track of time in the game.

    Methods:
    --------
    update():
        Updates the position and behavior of the Pacman object.
    check_position():
        Checks if Pacman can move in a certain direction based on the game map matrix.
    animate():
        Animates the Pacman object by updating the current sprite image index.
    eat():
        Removes the food object from the game map if Pacman collides with it.
    blitme():
        Draws objects on the screen
    """
    def __init__(self, var):
        """
        Initializes the Pacman object.

        Parameters:
        -----------
        var : VariableContainer
            A container object that contains various game variables.
        """
        self.screen = var.screen
        self.screen_rect = var.screen.get_rect()

        self.spritesheet = []
        self.current_sprite = 0
        self.spritesheet.append(pg.transform.scale(pg.image.load('src/Core/images/Pacman1.png'), (35, 35)))
        self.spritesheet.append(pg.transform.scale(pg.image.load('src/Core/images/Pacman2.png'), (35, 35)))
        self.spritesheet.append(pg.transform.scale(pg.image.load('src/Core/images/Pacman3.png'), (35, 35)))
        self.image = self.spritesheet[self.current_sprite]
        self.rect = self.image.get_rect()

        self.settings = var.settings
        self.map_matrix = var.game_map.map_matrix

        self.rect.centerx = self.settings.pacman_x
        self.rect.centery = self.settings.pacman_y

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.turns = [True, True, True, True]
        self.clock = pg.time.Clock()


    def update(self):
        """
        Updates the position and behavior of the Pacman object.
        """
        delta_time = self.clock.tick()
        self.check_position()
        if self.moving_right and self.turns[0]:
            self.x += self.settings.pacman_speed * (delta_time / 10)
            self.turns[0] = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False

            self.animate()

        if self.moving_left and self.turns[1]:
            self.x -= self.settings.pacman_speed * (delta_time / 10)
            self.turns[1] = False
            self.moving_right = False
            self.moving_up = False
            self.moving_down = False

            self.animate()

        if self.moving_up and self.turns[2]:
            self.y -= self.settings.pacman_speed * (delta_time / 10)
            self.turns[2] = False
            self.moving_right = False
            self.moving_left = False
            self.moving_down = False

            self.animate()

        if self.moving_down and self.turns[3]:
            self.y += self.settings.pacman_speed * (delta_time / 10)
            self.turns[3] = False
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False

            self.animate()

        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.x > 700:
            self.x = -10
            self.rect.x = self.x
        elif self.rect.x < -10:
            self.x = 700
            self.rect.x = self.x


        self.eat()

    def check_position(self):
        """
        Checks if Pacman can move in a certain direction based on the game map matrix.
        """
        x_pos = self.settings.screen_width // 30
        y_pos = (self.settings.screen_height - 50) // 32
        tweaker_1 = 15
        centerx = self.x + 17
        centery = self.y + 17
        if -16 < centerx // 30 < 29:
            if self.moving_right:
                if self.map_matrix[int(centery // y_pos)][int((centerx - tweaker_1) // x_pos)] < 3:
                    self.turns[1] = True
            if self.moving_left:
                if self.map_matrix[int(centery // y_pos)][int((centerx + tweaker_1) // x_pos)] < 3:
                    self.turns[0] = True

            if self.moving_up:
                if self.map_matrix[int((centery + tweaker_1) // y_pos)][int(centerx // x_pos)] < 3:
                    self.turns[3] = True
            if self.moving_down:
                if self.map_matrix[int((centery - tweaker_1) // y_pos)][int(centerx // x_pos)] < 3:
                    self.turns[2] = True

            if self.moving_up or self.moving_down:
                if 1 <= centerx % x_pos <= 25:
                    if self.map_matrix[int((centery + tweaker_1) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[3] = True
                    if self.map_matrix[int((centery - tweaker_1) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[2] = True
                if 1 <= self.y % y_pos <= 25:
                    if self.map_matrix[int(centery // y_pos)][int((centerx - x_pos) // x_pos)] < 3:
                        self.turns[1] = True
                    if self.map_matrix[int(centery // y_pos)][int((centerx + x_pos) // x_pos)] < 3:
                        self.turns[0] = True

            if self.moving_right or self.moving_left:
                if 1 <= centerx % x_pos <= 25:
                    if self.map_matrix[int((centery + y_pos) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[3] = True
                    if self.map_matrix[int((centery - y_pos) // y_pos)][int(centerx // x_pos)] < 3:
                        self.turns[2] = True
                if 5 <= centery % y_pos <= 25:
                    if self.map_matrix[int(centery // y_pos)][int((centerx - tweaker_1) // x_pos)] < 3:
                        self.turns[1] = True
                    if self.map_matrix[int(centery // y_pos)][int((centerx + tweaker_1) // x_pos)] < 3:
                        self.turns[0] = True

        else:
            self.turns[0] = True
            self.turns[1] = True
        return self.turns

    def blitme(self):
        """
        Draws objects on the screen
        """

        img = self.image

        if self.moving_right:
            img = pygame.transform.rotate(img, 0)

        if self.moving_left:
            img = pygame.transform.rotate(img, 180)

        if self.moving_up:
            img = pygame.transform.rotate(img, 90)

        if self.moving_down:
            img = pygame.transform.rotate(img, 270)

        self.screen.blit(img, self.rect)

    def animate(self):
        """
        Animates the Pacman object by updating the current sprite image index.
        """
        self.current_sprite += 1
        if self.current_sprite >= len(self.spritesheet):
            self.current_sprite = 0

        self.image = self.spritesheet[self.current_sprite]

    def eat(self):
        """
        Removes the food object from the game map if Pacman collides with it.
        """
        x_pos = self.settings.screen_width // 30
        y_pos = (self.settings.screen_height - 50) // 32
        centerx = self.x + 17
        centery = self.y + 17

        if self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] == 1:
            self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] = 0
            PacDot = fruits.PacDot()
            Statistics.score += PacDot.score
            Statistics.collectedPacDots += 1
            Statistics.check_win()

        if self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] == 2:
            self.map_matrix[int(centery // y_pos)][int(centerx // x_pos)] = 0
            PowerPellet = bonuses.PowerPellet()
            PowerPellet.use()
