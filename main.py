from player import Player
from obj import Objects
import pygame, random

pygame.init()

#CONFIGURAÇÕES BASICAS JOGO
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

pygame.display.set_caption("Jogo das gotas de sangue caindo do céu")

in_screen = []


#CARREGANDO IMAGENS JOGOS
Fundo = pygame.image.load("Imagens/fundo.jpg")

Fundo = pygame.transform.scale(Fundo,(800,600))


obj_dball = Objects("Imagens/dball.png",75,75)
obj_ki = Objects("Imagens/ki-blast.png",71.02,63.22)




#PLAYER CONFIG
player = Player("Imagens/goku.png",98.25,183,400,400)


#INGAME
running = True

while running == True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False


    screen.blit(Fundo,(0,0))


    #LOAD NO PLAYER
    player.print_char(screen)

    player.movements(pygame.K_a,pygame.K_d)


    #LOAD IMG
    obj_dball.render(screen)
    obj_dball.movement()
    obj_ki.render(screen)
    obj_ki.movement()

    pygame.display.update()


    clock.tick(60)


