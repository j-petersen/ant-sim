"""Contain information and functionality concerning the board information."""


class Board:
    """Board for simulation."""

    def __init__(self, width: int = 1280, height: int = 720):
        self.width = width
        self.height = height

    def is_inside_x(self, x: float) -> bool:
        """Check if x is inside the board."""
        if x <= 0:
            return False
        if x >= self.width:
            return False
        return True

    def is_inside_y(self, y: float) -> bool:
        """Check if y is inside the board."""
        if y <= 0:
            return False
        if y >= self.height:
            return False
        return True

    def is_inside(self, x: float, y: float) -> bool:
        """Check if point is in the board."""
        if not self.is_inside_x(x):
            return False
        if not self.is_inside_y(y):
            return False

        return True
