#!/usr/bin/env python3
import pygame


class Component:
    def __init__(self, x: float, y: float, pygame_object: object | list[object]) -> None:
        self.x: float = x
        self.y: float = y
        self.current_image: int = 0
        self.screen_width: int = 0
        self.screen_height: int = 0
        self.pygame_object: object | list[object] = pygame_object

    def add(self, screen: object) -> None:
        """function to add component inside screen

        :param: screen is display
        :return: None
        """
        screen.blit(self.pygame_object, (self.x, self.y))

    @staticmethod
    def flip(image) -> object:
        """function for reverse image

        :param: image
        :return: object image transforms
        """
        return pygame.transform.flip(image, True, False)

    def listen_event(self, keys) -> bool:
        """listen event in screen if key get pressed

        :param keys:
        :return: bool
        """
        return False

    def anime(self) -> None:
        """anime the component if event is true

        :arg: None
        :return:
        """
        pass
