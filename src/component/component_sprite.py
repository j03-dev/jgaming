import pygame

from .component_template import Component


class Sprite(Component):
    def __init__(
        self,
        x: float,
        y: float,
        velocity: float,
        pygame_object: pygame.Surface | list[pygame.Surface],
        width: int = 48,
        height: int = 48,
    ) -> None:
        Component.__init__(self, x, y, pygame_object)
        self.width = width
        self.height = height
        self.n_col: float = 5
        self._velocity: float = velocity
        self.current_sprite_sheet: int = 0
        self.row, self.col = 0, 0
        self.side = "right"

    def anime(self) -> None:
        size_total = self.n_col * self.width
        self.col = (self.col + self.width) % size_total

    def add(self, screen: pygame.Surface) -> None:
        self.screen_width, self.screen_height = screen.get_size()
        image = pygame.Surface([self.width, self.height])
        sprite = self.pygame_object[self.current_sprite_sheet]
        image.set_colorkey([0, 0, 0])  # make background sprite transparent
        image.blit(sprite, (0, 0), (self.col, self.row, self.width, self.height))
        if self.side == "left":
            image = self.flip(image)
        screen.blit(image, (self.x, self.y))
