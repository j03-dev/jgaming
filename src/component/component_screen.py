#!/usr/bin/env python3
import pygame

from .component_template import Component

pygame.init()


class Screen:
    def __init__(
            self, title: str, width: int, height: int, screen_color: tuple = (0, 0, 0), fps: int = 90,
    ) -> object:
        pygame.display.set_caption(title)
        self.width: int = width
        self.height: int = height
        self.screen_color = screen_color
        self.fps = fps
        self.play: bool = True
        self._screen = pygame.display.set_mode((self.width, self.height))
        self.__components: list[Component] = []

    def add(self, component: Component) -> None:
        self.__components.append(component)

    def mainloop(self) -> None:
        loop = True
        while loop:
            self._screen.fill(self.screen_color)
            pygame.time.delay(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False

            keys = pygame.key.get_pressed()

            # pause and play
            if keys[pygame.K_ESCAPE]:
                if self.play is True:
                    self.play = False
                elif self.play is False:
                    self.play = True

            for compnt in self.__components:
                compnt.add(self._screen)
                if self.play:
                    response = compnt.listen_event(keys)
                    if response is True or response is None:
                        compnt.anime()

            pygame.display.update()
