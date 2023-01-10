import pygame
from pygame import mixer
#Tela
largura = 1200  # WIDTH
altura = 600    # HEIGHT
SPEED = 10
GAME_SPEED = 15
GROUND_largura = 2 * largura #Chão
GROUND_altura = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
#X1
        #self.image_run = [pygame.image.load('X 00.png').convert_alpha(),
        #              pygame.image.load('X 01.png').convert_alpha(),
        #              pygame.image.load('X 02.png').convert_alpha(),
        #              pygame.image.load('X 03.png').convert_alpha(),
        #              pygame.image.load('X 04.png').convert_alpha(),
        #              ]
        #self.image_fall = pygame.image.load("X CAINDO.png").convert_alpha()
        #self.image = pygame.image.load('X 00.png').convert_alpha()
#X2
        self.image_run = [pygame.image.load('X4 - 2.png').convert_alpha(),
                          pygame.image.load('X4 - 3.png').convert_alpha(),
                          pygame.image.load('X4 - 4.png').convert_alpha(),
                          pygame.image.load('X4 - 5.png').convert_alpha(),
                          pygame.image.load('X4 - 6.png').convert_alpha(),
                          pygame.image.load('X4 - 7.png').convert_alpha(),
                          pygame.image.load('X4 - 8.png').convert_alpha(),
                          pygame.image.load('X4 - 9.png').convert_alpha(),
                          ]
        #self.image_Parado = pygame.image.load("X4_-PARADO.png").convert_alpha()
        self.image_fall = pygame.image.load("X4 - Caindo.png").convert_alpha()
        self.image = pygame.image.load('X4 - 2.png').convert_alpha()

        self.rect = pygame.Rect(100, 100, 100, 100)
                               # x
        self.current_image = 0

    def update(self, *args):

        #def Parado(self):
        #    key = pygame.key.get_pressed()
        #    if not KeyboardInterrupt:
        #        self.image = self.image_Parado
        #        self.image = pygame.transform.scale(self.image, [100, 100])
        #        print("Parado")
        #Parado(self)

        def move_player(self):
            key = pygame.key.get_pressed()
            # K = tecla que vc quer presionar (Right, left).
            if key[pygame.K_RIGHT]:
                self.rect[0] += GAME_SPEED   # 0 = x
            if key[pygame.K_LEFT]:
                self.rect[0] -= GAME_SPEED
            self.current_image = (self.current_image + 1) % 8
            self.image = self.image_run[self.current_image]
            self.image = pygame.transform.scale(self.image, [100, 100])
        move_player(self)
        self.rect[1] += SPEED

        def fly(self): # Personagem Pulando
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                self.rect[1] -= 30
                #self.image = pygame.image.load("X PULO.png") #X1
                self.image = pygame.image.load("X4 - Pulo.png")
                self.image = pygame.transform.scale(self.image, [100, 100])
                print("fly")
        fly(self)

        def fall(self): # Personagem Caindo
            key = pygame.key.get_pressed()
            if not pygame.sprite.groupcollide(playerGroup, groundGroup, False, False) and not key[pygame.K_SPACE]:
                self.image = self.image_fall
                self.image = pygame.transform.scale(self.image, [100, 100])
                print("Falling")
        fall(self)

class Ground(pygame.sprite.Sprite): # Chão
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("chao 1.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_largura, GROUND_altura))
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = altura - GROUND_altura

    def update(self, *args):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < - (sprite.rect[2])

#MÚSICA
mixer.init()
mixer.music.load('X6 Infinity Mijinion Stage.mp3')
mixer.music.play(-1) #repete -1
mixer.music.set_volume(0.1)

#Criando uma Tela
pygame.init()
janela_jogo = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Mega X')

BACKGROUD = pygame.image.load("planeta 2.jpg")
BACKGROUD = pygame.transform.scale(BACKGROUD, [largura, altura])

playerGroup = pygame.sprite.Group()
player = Player()
playerGroup.add(player)

groundGroup = pygame.sprite.Group()
for i in range(2):
    ground = Ground(largura * i)
    groundGroup.add(ground)

gameloop = True
def draw():
    #janela_jogo.fill([255,255,0]) # cor da tela
    playerGroup.draw(janela_jogo)
    groundGroup.draw(janela_jogo)

def update():
    groundGroup.update()
    playerGroup.update()
clock = pygame.time.Clock() #tempo de movimentação do personagem
while gameloop:
    clock.tick(15)          #tempo de movimentação do personagem
    janela_jogo.blit(BACKGROUD, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    if is_off_screen(groundGroup.sprites()[0]):
        groundGroup.remove(groundGroup.sprites()[0])
        newGround = Ground(largura - 20)
        groundGroup.add(newGround)
    if pygame.sprite.groupcollide(playerGroup, groundGroup, False, False):
        SPEED = 0
        print("collision")
    else:
        SPEED = 20
    update()
    draw()
    pygame.display.update()

