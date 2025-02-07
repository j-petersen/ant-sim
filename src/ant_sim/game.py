"""Main module which holds the game class and runs it."""

import logging

import pygame
from ant import Ant
from src.ant_sim.board import Board


class Game:
    def __init__(self, title: str, width: int, height: int, fps: int) -> None:
        """Initialize the game class with essential parameters."""
        self.title = title
        self.board = Board(width, height)
        self.fps = fps
        self.num_ants = 16

        self.running = True
        self._initial_setup()

    def _initial_setup(self) -> None:
        """Create pygame specific attributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.board.width, self.board.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()

        self.ants = Ant.initialize_ants_circle(self.num_ants, board=self.board)

    def handle_events(self) -> None:
        """Handle all events, such as key presses and mouse clicks."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt: float) -> None:
        """Update the game state. Override this method in subclasses."""
        for ant in self.ants:
            ant.update(dt, self.board)

    def render(self) -> None:
        """Render all game objects to the screen. Override this method in subclasses."""
        self.screen.fill((255, 255, 255))
        for ant in self.ants:
            ant.render(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""
        while self.running:
            dt = self.clock.tick(self.fps) / 1000.0  # Delta time in seconds
            self.handle_events()
            self.update(dt)
            self.render()
            self.clock.tick(self.fps)

        self.cleanup()

    @staticmethod
    def cleanup() -> None:
        """Cleanup resources before exiting the game."""
        pygame.quit()
        raise SystemExit("Game was terminated")


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    game = Game(title="Ant Simulation", width=1280, height=1280, fps=60)
    game.run()
