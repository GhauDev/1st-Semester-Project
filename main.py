import pygame, sys

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Github Test")
clock = pygame.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill("dark green")

    pygame.display.update()
    clock.tick(60)

