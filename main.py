import pygame

pygame.init()

window = pygame.display.set_mode((1100, 450))
pygame.display.set_caption("Game IP")

clock = pygame.time.Clock()

background = pygame.image.load('forest.png')


def redrawGameWindow():
    window.blit(background, (0, 0))
    pygame.display.update()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0


run = True
intro = True

while intro:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                intro = False

    window.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(15)

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    redrawGameWindow()
