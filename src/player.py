import pygame

from component.component_sprite import Sprite

# Task
# -[ ] get all element in component and attack then

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

GRAVITY = 10
JUMP = 30


class Player(Sprite):
    def __init__(
            self,
            x: float,
            y: float,
            velocity: float,
            pygame_object: pygame.Surface | list[pygame.Surface],
            width: int = 48,
            height: int = 48,
    ) -> None:
        Sprite.__init__(self, x, y, velocity, pygame_object, width, height)
        self.is_attack: bool = False
        self.is_jump: bool = False
        self.is_hurt: bool = False
        self.special_action: str = ""
        self.support = self.y

    def update_sprite(self, action: str) -> None:
        self.current_sprite_sheet, self.n_col = SPRITE_ACTION[action]

    def listen_event(self, keys) -> None:
        action_now: str = "idle"

        if (keys[pygame.K_UP] or keys[pygame.K_k]) and self.y > 0:
            self.is_jump = True
            self.special_action = "jump"

        elif (keys[pygame.K_LEFT] or keys[pygame.K_h]) and self.x > 0:
            self.x -= self._velocity
            self.side = "left"
            action_now = "run"

        elif (
                keys[pygame.K_RIGHT] or keys[pygame.K_l]
        ) and self.x <= self.screen_width - self.width:
            self.x += self._velocity
            self.side = "right"
            action_now = "run"

        elif keys[pygame.K_a]:
            self.is_attack = True
            self.special_action = "attack_1"

        elif keys[pygame.K_s]:
            self.is_attack = True
            self.special_action = "attack_2"

        elif keys[pygame.K_d]:
            self.is_attack = True
            self.special_action = "attack_3"

        elif keys[pygame.K_SPACE]:
            self.is_attack = True
            self.special_action = "hurt"

        end = (self.n_col - 1) * self.width

        if (self.col < end) and (self.is_attack or self.is_jump or self.is_hurt):
            action_now = self.special_action
            if action_now == "jump":
                self.y -= JUMP
                if self.side == "right":
                    self.x += 5
                elif self.side == "left":
                    self.x -= 5

        elif self.col == end:
            self.is_attack = False
            self.is_jump = False
            self.is_hurt = False

        # gravity
        if self.y < self.support and self.y <= self.screen_height - self.height:
            self.y += GRAVITY

        self.update_sprite(action_now)
