import pygame

from component.component_sprite import Sprite

SPRITE_ACTION = {
    "attack_1": (0, 6),
    "attack_2": (1, 8),
    "attack_3": (2, 8),
    "Biker_climb": (3, 5),
    "Biker_death": (4, 6),
    "double_jump": (5, 6),
    "hurt": (6, 2),
    "idle": (7, 4),
    "jump": (8, 4),
    "punch": (9, 6),
    "run": (10, 6),
    "run_attack": (11, 6),
}


class Player(Sprite):
    def __init__(self, x: float, y: float, velocity: float, pygame_object: object, width: int = 48,
                 height: int = 48) -> None:
        Sprite.__init__(self, x, y, velocity, pygame_object, width, height)
        self.pygame_object_right_side = self.pygame_object.copy()
        self.pygame_object_left_side = list(map(self.flip, self.pygame_object))

    def listen_event(self, keys) -> None:
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self._velocity

        elif keys[pygame.K_DOWN] and self.y <= self.screen_height:
            self.y += self._velocity

        elif keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self._velocity
            self.pygame_object = self.pygame_object_left_side.copy()
            self.current_sprite_sheet, self.n_frame = SPRITE_ACTION["run"]

        elif keys[pygame.K_RIGHT] and self.x <= self.screen_width:
            self.x += self._velocity
            self.pygame_object = self.pygame_object_right_side.copy()
            self.current_sprite_sheet, self.n_frame = SPRITE_ACTION["run"]

        elif keys[pygame.K_SPACE]:
            self.current_sprite_sheet, self.n_frame = SPRITE_ACTION["attack_1"]

        else:
            self.current_sprite_sheet, self.n_frame = SPRITE_ACTION["idle"]
