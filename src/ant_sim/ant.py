"""Implementation of the Ants."""

from typing import Self
from pathlib import Path

import numpy as np
import pygame

from ant_sim.board import Board

# Credits to sebastian lague to inspire this project and the creator of this sprite
# https://github.com/SebLague/Ant-Simulation/blob/main/Assets/Graphics/Ant%20sprite.png

SPRITE_PATH = Path(__file__).parent.parent.parent / 'sprite'
ANT_SPRITE = pygame.image.load(SPRITE_PATH / 'ant.png')


class Ant:

    __slots__ = ("x", "y", "theta", "speed")

    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        theta: float = 0.0,
        speed: float = 200,

    ):
        self.x = x
        self.y = y
        self.theta = theta
        self.speed = speed

    def update(self, dt: float, board: Board):
        dx = self.speed * np.cos(self.theta) * dt
        dy = self.speed * np.sin(self.theta) * dt
        inside_x = board.is_inside_x(self.x + dx)
        inside_y = board.is_inside_y(self.y + dy)
        dx = dx if inside_x else -dx
        dy = dy if inside_y else -dy

        self.x += dx
        self.y += dy

        self.theta = np.arctan2(dy, dx)

    def render(self, screen: pygame.Surface) -> None:
        # angle in deg and clockwise and not mathematical
        img = pygame.transform.rotozoom(ANT_SPRITE, np.rad2deg(-self.theta), 0.1)
        rect = img.get_rect(center=(self.x, self.y))
        screen.blit(img, rect.topleft)

    @classmethod
    def initialize_ants_circle(cls, number: int, board: Board) -> list[Self]:
        """Initialize the Ants in a circle facing outwards."""
        r = min(board.width, board.height) / 4
        angles = np.linspace(0, 2 * np.pi, number, endpoint=False)
        ants = []
        for angle in angles:
            ants.append(
                cls(
                    x=board.width / 2 + r * np.cos(angle),
                    y=board.height / 2 + r * np.sin(angle),
                    theta=angle,
                )
            )
        return ants
