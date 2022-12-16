import pygame

from .component_template import Component


class Sprite(Component):
    def __init__(
            self,
            x: float,
            y: float,
            velocity: float,
            pygame_object: object | list[object],
            width: int = 48,
            height: int = 48,
    ) -> None:
        Component.__init__(self, x, y, pygame_object)
        self.width = width
        self.height = height
        self.n_frame: float = 5
        self._velocity: float = velocity
        self.current_sprite_sheet: int = 0
        self.current_image: int = 0

    def anime(self) -> None:
        self.current_image += self.width
        self.current_image %= (self.n_frame * self.width)

    def add(self, screen) -> None:
        self.screen_width, self.screen_height = screen.get_size()
        image = pygame.Surface([self.width, self.height])
        sprite: object = self.pygame_object[self.current_sprite_sheet]
        image.set_colorkey([0, 0, 0])  # make background sprite transparent
        image.blit(sprite, (0, 0), (self.current_image, 0, self.width, self.height))
        screen.blit(image, (self.x, self.y))
