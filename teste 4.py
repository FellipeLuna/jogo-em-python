import pygame
from random import randint

pygame.init()
x = 400
y = 300
pos_x = 240
pos_y = 800
pos_y_2 = 800
pos_y_3 = 800
pos_y_4 = 800
timer = 0
tempo_segundo = 0

velocidade = 40

velocidade_inimigos = 25
fundo = pygame.image.load('espaco universo.jpg')
nave = pygame.image.load('nave.png')
inimigo1 = pygame.image.load('inimigo1.png')
inimigo2 = pygame.image.load('inimigo2.png')
inimigo3 = pygame.image.load('inimigo3.png')
inimigo4 = pygame.image.load('inimigo4.png')

font = pygame.font.SysFont('arial black', 20)
texto = font.render("Sobreviveu: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)


janela = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("First game in pyton")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT] and x >= 130:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 1200:
        x += velocidade

    if (pos_y <= -200) and (pos_y_2 <= -200) and (pos_y_3 <= -200) :
        pos_y = randint(1000, 2300)
        pos_y_2 = randint(1400, 2000)
        pos_y_3 = randint(1000, 1900)
        pos_y_4 = randint(900, 2000)

        if (timer < 0):
            timer += 1
        else:
            tempo_segundo += 1
            texto = font.render("Sobreviveu: " + str(tempo_segundo), True, (255,255,255),(0,0,0))
            timer = 0

    pos_y -= velocidade_inimigos + 4
    pos_y_2 -= velocidade_inimigos + 10
    pos_y_3 -= velocidade_inimigos + 8
    pos_y_4 -= velocidade_inimigos + 12

    janela.blit(fundo, (0,0))
    janela.blit(nave, (x,y))
    nave_rect = pygame.Rect(x, y, nave.get_width(), nave.get_height())
    inimigo1_rect = pygame.Rect(pos_x, pos_y, inimigo1.get_width(), inimigo1.get_height())
    inimigo2_rect = pygame.Rect(pos_x + 10, pos_y_2, inimigo2.get_width(), inimigo2.get_height())
    inimigo3_rect = pygame.Rect(pos_x + 10, pos_y_3, inimigo3.get_width(), inimigo3.get_height())
    inimigo4_rect = pygame.Rect(pos_x + 10, pos_y_4, inimigo4.get_width(), inimigo4.get_height())
    if nave_rect.colliderect(inimigo1_rect) or nave_rect.colliderect(inimigo2_rect) or nave_rect.colliderect(
            inimigo3_rect) or nave_rect.colliderect(inimigo4_rect):
        janela.blit(font.render("GAME OVER", True, (255, 255, 255)), (630, 450))
        pygame.display.update()
        pygame.time.delay(100)


    janela.blit(inimigo1, (pos_x, pos_y))
    janela.blit(inimigo2, (pos_x + 350, pos_y_2))
    janela.blit(inimigo3, (pos_x + 850, pos_y_3))
    janela.blit(inimigo4, (pos_x + 650, pos_y_4))

    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()