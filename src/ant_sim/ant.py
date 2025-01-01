"""Implementation of the Ants."""
import logging

import pygame


class Ant:

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.speed = 200.0
        self.size = 10

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # logging.debug(f'{keys=}')
        logging.debug(f'{dt=}')
        if keys[pygame.K_UP]:
            self.y -= self.speed * dt
        if keys[pygame.K_DOWN]:
            self.y += self.speed * dt
        if keys[pygame.K_LEFT]:
            self.x -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.x += self.speed * dt

    def render(self, screen: pygame.Surface) -> None:
        logging.debug('Rendering Ant.')
        logging.debug('Rendering Ant.')
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (self.x, self.y, self.size, self.size),
        )