import pygame
from random import randint
from pygame import mixer

pygame.init()
# CARRO PRINCIPAL
x = 480   # horizontal   (POSIÇÃO: máx E260 C480 D720)
y = 50    # vertical

px = 280
py = 800     #Policial
py_a = 1200  #Porshe
py_c = 2500  #Ferrari
py_d = 1000  #Viatura

timer = 0
tempo_segundo = 0
fim = timer + tempo_segundo

velocidade = 10
vel_outros = 10

fundo = pygame.image.load('PISTA 01.jpg')
carroprincipal = pygame.image.load('mustang 1.png')
policia = pygame.image.load('policia 1.png')
ferrari = pygame.image.load('ferrari 1.png')
porshe = pygame.image.load('amarelo 1.png')
viatura = pygame.image.load('viatura.jpg')

fonte = pygame.font.SysFont('arial black', 30)
texto = fonte.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = 65, 50

janela = pygame.display.set_mode((1071, 600)) # largura/altura
pygame.display.set_caption("Race Street")

# MÚSICA
mixer.init()
mixer.music.load('Top Gear.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.1)
#mixer.init()
#mixer.music.load('mustang acelerando.wav')
#mixer.music.play(-1)
#mixer.music.set_volume(0.4)

janela_aberta= True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
    #    y-=velocidade
    #if comandos[pygame.K_DOWN]:
    #    y+=velocidade
    if comandos[pygame.K_RIGHT] and x <= 710:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 260:
        x -= velocidade

    # COLISÕES
    if ((px + 100 > x and y + 330 > py)):        #colisão lad esquerdo e traseira
       break

    if ((px + 100 < x - 200 and y + 330 > py_a)): #colisão lad direito e traseira 230
        break

    if ((px + 80 > x - 220 and y + 220 > py_c)) and ((px - 80 < x - 180 and y + 180 > py_c)):
        break                                    #colisão central e laterais

    if (py <= - 80):
        py = randint(800, 1000)
    if (py_a <= - 80):
        py_a = randint(1200, 2000)
    if (py_c <= - 80) :
        py_c = randint(2200, 3000)

    #if (py <= 180) and (py_a <= - 180) and  (py_c <= - 180):
    #    py = randint(800,1000) #Policial
    #    py_a = randint(800,2000) #Porshe
    #    py_c = randint(800,3000) #Ferrari
        #py_d = randint(800,2000)

    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = fonte.render("Tempo: "+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    py -= vel_outros         # Policial
    py_a -= vel_outros + 2   # Porshe
    py_c -= vel_outros + 6   # Ferrari
    py_d -= vel_outros + 3   # Viatura

    #janela.fill((0,0,0))
    janela.blit(fundo, (0, 0))
    janela.blit(carroprincipal, (x, y))
    janela.blit(policia, (px, py - 100))
    janela.blit(porshe, (px+390, py_a - 100))
    janela.blit(ferrari, (px+200, py_c))
    #janela.blit(viatura,(px,py_d- 1000))
    janela.blit(texto, pos_texto)

    #pygame.draw.circle(janela, (0,255,0), (x,y), 50)#(verm,verde,azul) (posição) (raio do pixls)
    pygame.display.update()

pygame.quit()

