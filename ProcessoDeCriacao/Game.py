import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

pygame.mixer.music.set_volume(0.3)
musicaDeFundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

moeda = pygame.mixer.Sound('smw_coin.wav')
moeda.set_volume(5)
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Rua Do Hospicio')

x = (largura/2)
y = altura/2


relogio = pygame.time.Clock()

a = random.randrange(5, 600)
b = random.randrange(5, 400)

fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

while True:
    
    relogio.tick(60)
   
    tela.fill((0,0,0))
    
    mensagem = f"Pontos: {pontos}"
    textoFormatado = fonte.render(mensagem, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    
    if pygame.key.get_pressed()[K_a]:
        x= x-5
    if pygame.key.get_pressed()[K_w]:
        y=y-5 
    if pygame.key.get_pressed()[K_s]:
        y=y+5
    if pygame.key.get_pressed()[K_d]:
        x=x+5
    
        
    retangulo = pygame.draw.rect(tela, (255,0,0), (x,y,30,30))
    maca = pygame.draw.rect(tela, (0,255,0), (a, b, 20, 20))
    
    if retangulo.colliderect(maca):
        a = random.randrange(20, 600)
        b = random.randrange(20, 400)
        pontos = pontos+1
        moeda.play()
        
        
    if(y<0):
        y=altura
    elif(y>altura):
        y=0
    elif(x<0):
        x=largura
    elif(x>largura):
        x=0
    
    tela.blit(textoFormatado, (420,40))
    
    pygame.display.update()