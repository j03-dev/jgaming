from os import walk, path

import pygame


def get_assets(directory: str, ext: str) -> list[str]:
    list_assets = \
        [[path.join(root, file) for file in files if f".{ext}" in file] for root, _, files in walk(directory)][0]
    return sorted(list_assets)


def load_image_assets(assets: list[str]):
    return [pygame.image.load(image) for image in assets]
