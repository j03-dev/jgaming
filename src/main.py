import pygame

import player
from component.component_screen import Screen
from component.component_template import Component

# from component.component_image_animated import ComponentImageAnimated
from tools import assets

if __name__ == "__main__":
    image_background = pygame.image.load("../assets/decoration/Background.png")
    width, height = image_background.get_size()

    screen = Screen("Second game I made", width, height, fps=60)
    biker_sprite_sheet: list[str] = assets.get_assets("../assets/3 Cyborg/", "png")

    # image_runner = assets.get_assets("../assets/player/", "png")

    # image_runner = assets.load_image_assets(image_runner)
    # runner = ComponentImageAnimated(
    #          x=screen.width // 2,
    #          y=screen.height // 2,
    #          velocity=1,
    #          pygame_object=image_runner)

    background = Component(0, 0, image_background)
    screen.add(background)

    biker = player.Player(
        x=screen.width // 2,
        y=screen.height - 50,
        velocity=5,
        pygame_object=assets.load_image_assets(biker_sprite_sheet),
    )

    screen.add(biker)
    # screen.add(runner)
    screen.mainloop()
