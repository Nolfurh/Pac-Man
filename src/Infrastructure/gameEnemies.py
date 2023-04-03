import os
from abc import ABC, abstractmethod

import pygame as pg
from src.Infrastructure.gameProcesses.statistics import Statistics


class MovementAlgorithm(ABC):

    @abstractmethod
    def do_algorithm(self, var):
        pass


class GhostMovement():

    def __init__(self, movementAlgorithm: MovementAlgorithm) -> None:
        self._movementAlgorithm = movementAlgorithm

    @property
    def movementAlgorithm(self):
        return self._movementAlgorithm

    @movementAlgorithm.setter

    def movementAlgorithm(self, movementAlgorithm: MovementAlgorithm) -> None:
        self._movementAlgorithm = movementAlgorithm

    def do_movement(self, var) -> None:
        self._movementAlgorithm.do_algorithm(var)

    def check_position(self, var):

        x_pos = var.settings.screen_width // 30
        y_pos = (var.settings.screen_height - 50) // 32
        tweaker = 15
        center_x = var.x + 17
        center_y = var.y + 17
        var.turns = [False, False, False, False]
        if 0 < center_x // 30 < 29:


            if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9:
                var.turns[2] = True


            if var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] < 3 \
                    or (var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[1] = True


            if var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] < 3 \
                    or (var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[0] = True


            if var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                    or (var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[3] = True


            if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                    or (var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                    var.in_box or var.eaten)):
                var.turns[2] = True



            if var.moving_up or var.moving_down:
                if 1 <= center_x % x_pos <= 25:
                    if var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y + tweaker) // y_pos)][
                                    int(center_x // x_pos)] == 9 and (
                                        var.in_box or var.eaten)):
                        var.turns[3] = True
                    if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y - tweaker) // y_pos)][
                                    int(center_x // x_pos)] == 9 and (
                                        var.in_box or var.eaten)):
                        var.turns[2] = True
                if 1 <= center_y % y_pos <= 25:
                    if var.map_matrix[int(center_y // y_pos)][int((center_x - x_pos) // x_pos)] < 3 \
                            or (
                            var.map_matrix[int(center_y // y_pos)][int((center_x - x_pos) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[1] = True
                    if var.map_matrix[int(center_y // y_pos)][int((center_x + x_pos) // x_pos)] < 3 \
                            or (
                            var.map_matrix[int(center_y // y_pos)][int((center_x + x_pos) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[0] = True



            if var.moving_right or var.moving_left:
                if 1 <= center_x % x_pos <= 25:
                    if var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y + tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[3] = True
                    if var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] < 3 \
                            or (var.map_matrix[int((center_y - tweaker) // y_pos)][int(center_x // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[2] = True
                if 1 <= center_y % y_pos <= 25:
                    if var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] < 3 \
                            or (var.map_matrix[int(center_y // y_pos)][int((center_x - tweaker) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[1] = True
                    if var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] < 3 \
                            or (var.map_matrix[int(center_y // y_pos)][int((center_x + tweaker) // x_pos)] == 9 and (
                            var.in_box or var.eaten)):
                        var.turns[0] = True
        else:
            var.turns[0] = True
            var.turns[1] = True


        if 350 < var.x < 550 and 370 < var.y < 480:
            var.in_box = True
        else:
            var.in_box = False
        return var.turns, var.in_box



    def check_collision(self, var):

        player_circle = pg.draw.circle(var.screen, 'black', (var.player_x, var.player_y), 21, 2)
        if not Statistics().activatedBonuses:
            if (player_circle.colliderect(var.rect)) and not var.eaten:
                if Statistics.lives > 0:
                    Statistics.lives -= 1
                    var.x = 300
                    var.y = 300
                    var.rect.x = var.x
                    var.rect.y = var.y
                    var.player.x = 50
                    var.player.y = 50
                    var.moving_right = True
                    var.moving_left = False
                    var.moving_up = False
                    var.moving_down = False
                    var.eaten_ghost = [False, False, False, False]
                    var.eaten = False
                else:
                    Statistics.lose = True
        if Statistics().activatedBonuses and player_circle.colliderect(var.rect) and not var.eaten:
            if Statistics.lives > 0:
                power_counter = 50
                power_counter -= 1
                var.x = 300
                var.y = 300
                var.rect.x = var.x
                var.rect.y = var.y
                var.moving_right = False
                var.moving_left = False
                var.moving_up = False
                var.moving_down = False
                var.eaten_ghost = [True, False, False, False]
                var.eaten = True
                var.eat_sound.play()
                if power_counter == 1:
                    var.eaten = False
            else:
                Statistics.lose = True
                pg.mixer.Sound(os.path.join('src', os.path.join('Core',os.path.join('sounds', 'pacman_death.wav')))).play()
        if var.eaten:
            var.cooldown -= 1
            if var.cooldown == 1:
                var.eaten = False
                var.moving_right = True
                var.moving_left = False
                var.moving_up = False
                var.moving_down = False
                var.cooldown = 250



    def draw(self, var):

        center_x = var.rect.x + 17
        center_y = var.rect.y + 17
        if not Statistics().activatedBonuses and not var.eaten:
            var.screen.blit(var.image, (var.rect.x, var.rect.y))
        elif Statistics().activatedBonuses and not var.eaten:
            var.screen.blit(var.vulnerable, (var.x, var.y))
        else:
            var.screen.blit(var.spunky, (var.x, var.y))
        ghost_rect = pg.rect.Rect((center_x - 17, center_y - 17), (35, 35))
        return ghost_rect


class ConcreteMovementOne(MovementAlgorithm):

    def __init__(self):
        self.clock = pg.time.Clock()

    def do_algorithm(self, var):

        center_x = var.x + 17
        center_y = var.y + 17

        delta_time = self.clock.tick()

        if var.moving_right:
            if var.ghost_targets[0] > center_x and var.turns[0]:
                var.x += var.speed * (delta_time / 10)
            elif not var.turns[0]:
                var.moving_right = False
                if var.ghost_targets[1] > center_y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < center_y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < center_x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
            elif var.turns[0]:
                if var.ghost_targets[1] > center_y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                    var.moving_right = False
                if var.ghost_targets[1] < center_y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                    var.moving_right = False
                else:
                    var.x += var.speed
        elif var.moving_left:
            if var.ghost_targets[1] > center_y and var.turns[3]:
                var.moving_down = True
                var.moving_left = False
            elif var.ghost_targets[0] < center_x and var.turns[1]:
                var.x -= var.speed * (delta_time / 10)
            elif not var.turns[1]:
                var.moving_left = False
                if var.ghost_targets[1] > center_y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < center_y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] > center_x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[1]:
                if var.ghost_targets[1] > center_y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                    var.moving_left = False
                if var.ghost_targets[1] < center_y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                    var.moving_left = False
                else:
                    var.x -= var.speed * (delta_time / 10)
        elif var.moving_up:
            if var.ghost_targets[0] < center_x and var.turns[1]:
                var.moving_left = True
                var.x -= var.speed * (delta_time / 10)
                var.moving_up = False
            elif var.ghost_targets[1] < center_y and var.turns[2]:
                var.moving_up = True
                var.y -= var.speed * (delta_time / 10)
            elif not var.turns[2]:
                var.moving_up = False
                if var.ghost_targets[0] > center_x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < center_x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] > center_y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[2]:
                if var.ghost_targets[0] > center_x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                    var.moving_up = False
                elif var.ghost_targets[0] < center_x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                    var.moving_up = False
                else:
                    var.y -= var.speed * (delta_time / 10)
        elif var.moving_down:
            if var.ghost_targets[1] > center_y and var.turns[3]:
                var.y += var.speed * (delta_time / 10)
            elif not var.turns[3]:
                var.moving_down = False
                if var.ghost_targets[0] > center_x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < center_x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < center_y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[3]:
                if var.ghost_targets[0] > center_x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                    var.moving_down = False
                elif var.ghost_targets[0] < center_x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                    var.moving_down = False
                else:
                    var.y += var.speed * (delta_time / 10)

        if center_x > 700:
            var.x = -10
            center_x = var.x
        elif center_x < -10:
            var.x = 700
            center_x = var.x
        return var.x, var.y, var.moving_left, var.moving_right, var.moving_up, var.moving_down


class ConcreteMovementTwo(MovementAlgorithm):
    def __init__(self):
        self.clock = pg.time.Clock()

    def do_algorithm(self, var):
    
        delta_time = self.clock.tick()

        if var.moving_right:
            if var.ghost_targets[0] > var.x and var.turns[0]:
                var.x += var.speed * (delta_time / 10)
            elif not var.turns[0]:
                var.moving_right = False
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
            elif var.turns[0]:
                var.x += var.speed * (delta_time / 10)
        elif var.moving_left:
            if var.ghost_targets[0] < var.x and var.turns[1]:
                var.x -= var.speed * (delta_time / 10)
            elif not var.turns[1]:
                var.moving_left = False
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_up = True
                    var.x += var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_up = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[1]:
                var.x -= var.speed * (delta_time / 10)
        elif var.moving_up:
            if var.ghost_targets[1] < var.y and var.turns[2]:
                var.moving_up = True
                var.y -= var.speed * (delta_time / 10)
            elif not var.turns[2]:
                var.moving_up = False
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_up = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_up = True
                    var.x += var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
            elif var.turns[2]:
                var.y -= var.speed * (delta_time / 10)
        elif var.moving_down:
            if var.ghost_targets[1] > var.y and var.turns[3]:
                var.y += var.speed * (delta_time / 10)
            elif not var.turns[3]:
                var.moving_down = False
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_up = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_up = True
                    var.x += var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
            elif var.turns[3]:
                var.y += var.speed * (delta_time / 10)


        if var.x > 700:
            var.x = -10
        elif var.x < -10:
            var.x = 700
        return var.x, var.y, var.moving_left, var.moving_right, var.moving_up, var.moving_down


class ConcreteMovementThree(MovementAlgorithm):
    def __init__(self):
        self.clock = pg.time.Clock()
    
    def do_algorithm(self, var):

        delta_time = self.clock.tick()

        if var.moving_right:
            if var.ghost_targets[0] > var.x and var.turns[0]:
                var.x += var.speed * (delta_time / 10)
            elif not var.turns[0]:
                var.moving_right = False
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
            elif var.turns[0]:
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                if var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                else:
                    var.x += var.speed * (delta_time / 10)
        elif var.moving_left:
            if var.ghost_targets[1] > var.y and var.turns[3]:
                var.moving_down = True
            elif var.ghost_targets[0] < var.x and var.turns[1]:
                var.x -= var.speed * (delta_time / 10)
            elif not var.turns[1]:
                var.moving_left = False
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[1]:
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                if var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                else:
                    var.x -= var.speed * (delta_time / 10)
        elif var.moving_up:
            if var.ghost_targets[1] < var.y and var.turns[2]:
                var.moving_up = True
                var.y -= var.speed * (delta_time / 10)
            elif not var.turns[2]:
                var.moving_up = False
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[2]:
                var.y -= var.speed * (delta_time / 10)
        elif var.moving_down:
            if var.ghost_targets[1] > var.y and var.turns[3]:
                var.y += var.speed * (delta_time / 10)
            elif not var.turns[3]:
                var.moving_down = False
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[3]:
                var.y += var.speed * (delta_time / 10)


        if var.x > 700:
            var.x = -10
        elif var.x < -10:
            var.x = 700
        return var.x, var.y, var.moving_left, var.moving_right, var.moving_up, var.moving_down


class ConcreteMovementFour(MovementAlgorithm):
    def __init__(self):
        self.clock = pg.time.Clock()
    
    def do_algorithm(self, var):

        delta_time = self.clock.tick()

        if var.moving_right:
            if var.ghost_targets[0] > var.x and var.turns[0]:
                var.x += var.speed * (delta_time / 10)
            elif not var.turns[0]:
                var.moving_right = False
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
            elif var.turns[0]:
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                    var.moving_right = False
                if var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                    var.moving_right = False
                else:
                    var.x += var.speed * (delta_time / 10)
        elif var.moving_left:
            if var.ghost_targets[1] > var.y and var.turns[3]:
                var.moving_down = True
                var.moving_left = False
            elif var.ghost_targets[0] < var.x and var.turns[1]:
                var.x -= var.speed * (delta_time / 10)
            elif not var.turns[1]:
                var.moving_left = False
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[1]:
                if var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                    var.moving_left = False
                if var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                    var.moving_left = False
                else:
                    var.x -= var.speed * (delta_time / 10)
        elif var.moving_up:
            if var.ghost_targets[0] < var.x and var.turns[1]:
                var.moving_left = True
                var.x -= var.speed * (delta_time / 10)
                var.moving_up = False
            elif var.ghost_targets[1] < var.y and var.turns[2]:
                var.moving_up = True
                var.y -= var.speed * (delta_time / 10)
            elif not var.turns[2]:
                var.moving_up = False
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] > var.y and var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[3]:
                    var.moving_down = True
                    var.y += var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[2]:
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                    var.moving_up = False
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                    var.moving_up = False
                else:
                    var.y -= var.speed * (delta_time / 10)
        elif var.moving_down:
            if var.ghost_targets[1] > var.y and var.turns[3]:
                var.y += var.speed * (delta_time / 10)
            elif not var.turns[3]:
                var.moving_down = False
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.ghost_targets[1] < var.y and var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[2]:
                    var.moving_up = True
                    var.y -= var.speed * (delta_time / 10)
                elif var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                elif var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
            elif var.turns[3]:
                if var.ghost_targets[0] > var.x and var.turns[0]:
                    var.moving_right = True
                    var.x += var.speed * (delta_time / 10)
                    var.moving_down = False
                elif var.ghost_targets[0] < var.x and var.turns[1]:
                    var.moving_left = True
                    var.x -= var.speed * (delta_time / 10)
                    var.moving_down = False
                else:
                    var.y += var.speed * (delta_time / 10)


        if var.x > 700:
            var.x = -10
        elif var.x < -10:
            var.x = 700
        return var.x, var.y, var.moving_left, var.moving_right, var.moving_up, var.moving_down

class Blinky():


    """
    Checking if the ghost has been eaten 
    by Pacman and if so it will change its movement to a new one If not it will check 
    for collisions with walls or other ghosts and move accordingly Finally it checks 
    whether the ghost is in a box which means that he can't be moved or not
    """
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/blinky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.blinky_x
        self.rect.centery = self.settings.blinky_y

        self.cooldown = 250

        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.eat_sound = pg.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                                         os.path.join('sounds',
                                                                                      'pacman_eatghost.wav'))))
        self.clock = pg.time.Clock()

        self.ghostMovement = GhostMovement(ConcreteMovementOne())

    def update(self, var):
        """
        Update in a loop all data about ghost
        """
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.ghostMovement.draw(self)
        self.ghostMovement.check_position(self)
        self.ghostMovement.do_movement(self)
        self.rect.x = self.x
        self.rect.y = self.y
        self.ghostMovement.check_collision(self)


class Inky():

    """
    Checking if the ghost has been eaten 
    by Pacman and if so it will change its movement to a new one If not it will check 
    for collisions with walls or other ghosts and move accordingly Finally it checks 
    whether the ghost is in a box which means that he can't be moved or not
    """
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/inky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.inky_x
        self.rect.centery = self.settings.inky_y

        self.cooldown = 250

        self.moving_right = False
        self.moving_left = True
        self.moving_up = False
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.eat_sound = pg.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                                         os.path.join('sounds',
                                                                                      'pacman_eatghost.wav'))))
        self.clock = pg.time.Clock()


        self.ghostMovement = GhostMovement(ConcreteMovementTwo())

    def update(self, var):
        """
        Update in a loop all data about ghost
        """
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.ghostMovement.draw(self)
        self.ghostMovement.check_position(self)
        self.ghostMovement.do_movement(self)
        self.rect.x = self.x
        self.rect.y = self.y
        self.ghostMovement.check_collision(self)


class Pinky():


    """
    Checking if the ghost has been eaten 
    by Pacman and if so it will change its movement to a new one If not it will check 
    for collisions with walls or other ghosts and move accordingly Finally it checks 
    whether the ghost is in a box which means that he can't be moved or not
    """
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/pinky.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.pinky_x
        self.rect.centery = self.settings.pinky_y

        self.cooldown = 250

        self.moving_right = True
        self.moving_left = False
        self.moving_up = True
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.eat_sound = pg.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                                         os.path.join('sounds',
                                                                                      'pacman_eatghost.wav'))))
        self.clock = pg.time.Clock()

        self.ghostMovement = GhostMovement(ConcreteMovementThree())

    def update(self, var):
        """
        Update in a loop all data about ghost
        """
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.ghostMovement.draw(self)
        self.ghostMovement.check_position(self)
        self.ghostMovement.do_movement(self)
        self.rect.x = self.x
        self.rect.y = self.y
        self.ghostMovement.check_collision(self)


class Clyde():


    """
    Checking if the ghost has been eaten 
    by Pacman and if so it will change its movement to a new one If not it will check 
    for collisions with walls or other ghosts and move accordingly Finally it checks 
    whether the ghost is in a box which means that he can't be moved or not
    """
    def __init__(self, var):
        self.image = pg.transform.scale(pg.image.load('src/Core/images/clyde.png'), (35, 35))
        self.vulnerable = var.vulnerable
        self.spunky = var.spunky

        self.turns = [False, False, False, False]

        self.rect = self.image.get_rect()
        self.screen = var.screen

        self.settings = var.settings
        self.map_matrix = var.map_matrix
        self.eaten_ghost = var.eaten_ghost
        self.speed = var.settings.ghosts_speed

        self.rect.centerx = self.settings.clyde_x
        self.rect.centery = self.settings.clyde_y

        self.cooldown = 250

        self.moving_right = False
        self.moving_left = False
        self.moving_up = True
        self.moving_down = False

        self.eaten = False
        self.in_box = False

        self.ghost_targets = var.ghost_targets[0]

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.eat_sound = pg.mixer.Sound(os.path.join('src', os.path.join('Core',
                                                                             os.path.join('sounds',
                                                                                          'pacman_eatghost.wav'))))
        self.clock = pg.time.Clock()

        self.ghostMovement = GhostMovement(ConcreteMovementFour())

    def update(self, var):
        """
        Update in a loop all data about ghost
        """
        self.ghost_targets = var.ghost_targets[0]
        self.eaten_ghost = var.eaten_ghost

        self.player_x, self.player_y = var.player_x, var.player_y
        self.player = var.player

        self.ghostMovement.draw(self)
        self.ghostMovement.check_position(self)
        self.ghostMovement.do_movement(self)
        self.rect.x = self.x
        self.rect.y = self.y
        self.ghostMovement.check_collision(self)
