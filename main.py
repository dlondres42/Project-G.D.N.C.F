import pygame

pygame.init()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png')]

char = pygame.image.load('standing.png')

window = pygame.display.set_mode((1100, 450))
pygame.display.set_caption("Game IP")

clock = pygame.time.Clock()

background = pygame.image.load('forest.png')


def redrawGameWindow():
    global walkCount

    window.blit(background, (0, 0))
    if walkCount + 1 >= 19:
        walkCount = 0

    if left:
        window.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        window.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        window.blit(char, (x, y))
        walkCount = 0

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


x = 10
y = 300
width = 51
height = 39
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

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
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False


    elif keys[pygame.K_RIGHT] and x < 1100 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

pygame.quit()
