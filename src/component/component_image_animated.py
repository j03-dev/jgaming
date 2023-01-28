import pygame

from .component_template import Component


class ComponentImageAnimated(Component):
    def __init__(
        self,
        x: float,
        y: float,
        velocity: float,
        pygame_object: pygame.Surface | list[pygame.Surface],
    ):
        Component.__init__(self, x, y, pygame_object)
        self._velocity = velocity
        self.pygame_object_right_side = self.pygame_object.copy()
        self.pygame_object_left_side = list(map(self.flip, self.pygame_object))
        self.image_width, self.image_height = self.pygame_object_right_side[
            0
        ].get_size()

    def add(self, screen: pygame.Surface) -> None:
        self.screen_width, self.screen_height = screen.get_size()
        if self.current_image < len(self.pygame_object):
            screen.blit(self.pygame_object[int(self.current_image)], (self.x, self.y))
        else:
            self.current_image = 0

    def anime(self) -> None:
        self.current_image = (self.current_image + 0.1) % len(self.pygame_object)

    def listen_event(self, keys) -> bool:
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self._velocity
            return False

        elif keys[pygame.K_DOWN] and self.y <= self.screen_height - self.image_height:
            self.y += self._velocity
            return False

        elif keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self._velocity
            self.pygame_object = self.pygame_object_left_side.copy()
            return True

        elif keys[pygame.K_RIGHT] and self.x <= self.screen_width - self.image_width:
            self.x += self._velocity
            self.pygame_object = self.pygame_object_right_side
            return True

        return False
