import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

#                                    IMAGENS DAS ANIMAÇÕES, BACKGROUND E INTRO
########################################################################################################################
jump_s = pygame.image.load('images/standingJUMP.png')
jump_l = pygame.image.load('images/LJUMP.png')
jump_r = pygame.image.load('images/RJUMP.png')
char = pygame.image.load('images/standing.png')

walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'),
             pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
             pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'),
             pygame.image.load('images/R9.png'), pygame.image.load('images/R10.png'),
             pygame.image.load('images/R11.png'),
             pygame.image.load('images/R12.png')]
walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'),
            pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
            pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png'),
            pygame.image.load('images/L10.png'), pygame.image.load('images/L11.png'),
            pygame.image.load('images/L12.png')]

background = pygame.image.load('images/forest.png')
intro_foto = pygame.image.load('images/introfoto.png')
########################################################################################################################


pygame.display.set_caption("Game IP")

window = pygame.display.set_mode((1100, 450))
clock = pygame.time.Clock()


class enemy(object):
    walkRight = pygame.image.load('images/fantasmaR.png')
    walkLeft = pygame.image.load('images/fantasmaL.png')

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y, 35, 35)

    def draw(self, win):
        self.move()

        if self.vel > 0:  # If we are moving to the right we will display our walkRight images
            win.blit(self.walkRight, (self.x, self.y))

        else:  # Otherwise we will display the walkLeft images
            win.blit(self.walkLeft, (self.x, self.y))

        self.hitbox = (self.x, self.y, 35, 35)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 39, 53)

    def draw(self, window):
        if self.walkCount + 1 >= 37:
            self.walkCount = 0

        if self.isJump and not self.left and not self.right:
            window.blit(jump_s, (self.x, self.y))

        if self.isJump and self.left:
            window.blit(jump_l, (self.x, self.y))

        if self.isJump and self.right:
            window.blit(jump_r, (self.x, self.y))

        if self.left and not self.isJump:
            window.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right and not self.isJump:
            window.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        if not self.left and not self.right and not self.isJump:
            window.blit(char, (self.x, self.y))
            self.walkCount = 0

        self.hitbox = (self.x, self.y, 39, 53)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

def redrawGameWindow():
    window.blit(background, (0, 0))
    fantasma.draw(window)
    fantasma_2.draw(window)
    fantasma_3.draw(window)
    jogador.draw(window)
    pygame.display.update()


run = False
intro = True
################################################## MÚSICA 1 ###########################################################
pygame.mixer.music.load('music/01 -Glorious morning-.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
########################################################################################################################

################################################## INTRO ###############################################################

while intro:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                intro = False

    window.blit(intro_foto, (0, 0))
    clock.tick(40)
    pygame.display.update()

################################################## MÚSICA 2 ###########################################################
pygame.mixer.music.load('music/76677_newgrounds_field_.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
########################################################################################################################

jogador = Player(50, 350, 50, 40)
fantasma = enemy(100, 300, 30, 30, 450)
fantasma_2 = enemy(200, 350, 30, 30, 400)
fantasma_3 = enemy(500, 100, 30, 30, 700)


run = True
while run:

    clock.tick(45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and jogador.x - 25 > jogador.vel:
        jogador.x -= jogador.vel
        jogador.left = True
        jogador.right = False


    elif keys[pygame.K_RIGHT] and jogador.x < 1100 - jogador.vel - jogador.width:
        jogador.x += jogador.vel
        jogador.left = False
        jogador.right = True

    else:
        jogador.left = False
        jogador.right = False
        jogador.walkCount = 0

    if not jogador.isJump:
        if keys[pygame.K_SPACE]:
            jogador.isJump = True
            jogador.left = False
            jogador.right = False
            jogador.walkCount = 0
    else:
        if jogador.jumpCount >= -10:
            neg = 1
            if jogador.jumpCount < 0:
                neg = -1

            jogador.y -= (jogador.jumpCount ** 2) * 0.6 * neg
            jogador.jumpCount -= 1
        else:
            jogador.jumpCount = 10
            jogador.isJump = False

    redrawGameWindow()

pygame.quit()
