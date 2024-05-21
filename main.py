import pygame, random
from player import Player
from obstaculos import Obstaculo

pygame.init()


#Configurações básicas do jogo
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo do ano 2024")
clock = pygame.time.Clock()


#Sprites
jogador = Player("Imagens/goku.png", 100,100,100,375)



Fundo = pygame.image.load("Imagens/fundo.jpg")
Fundo = pygame.transform.scale(Fundo,(800,500))



#SOUND EFFECTS

pygame.mixer.music.load("sounds/ost.mp3")
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()


point_up = pygame.mixer.Sound("sounds/good_sound.mp3")

point_down = pygame.mixer.Sound("sounds/bad_sound.mp3")



#Obstáculos
obstaculos = []


#O jogo rodando em si e configurações
rodando = True


#Faz ser possível quitar do jogo kkkkkk
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    #Spawna os sprites e seus movimentos
    tela.blit(Fundo,(0,0))

    #PLAYER 1 CONFIG
    jogador.print_char(tela)
    jogador.movements(pygame.K_a, pygame.K_d)



    #OBSTACULOS
    if len(obstaculos) <= 7:
        novo_obstaculo = Obstaculo()  # Cria um novo obstáculo
        obstaculos.append(novo_obstaculo)  # Adiciona à lista de obstáculos
    for obstaculokk in obstaculos:
        if obstaculokk.pos_y > 600:
            obstaculos.remove(obstaculokk)
    

    # Atualiza e desenha os obstáculos
    for obstaculokk in obstaculos:
        obstaculokk.load(tela)
        obstaculokk.movimenta()
        if jogador.rect.colliderect(obstaculokk.rect):
            if obstaculokk.sts_dball == 1:
                point_up.play()
                obstaculos.remove(obstaculokk)
            elif obstaculokk.sts_ki == 1:
                point_down.play()
                obstaculos.remove(obstaculokk)



    pygame.display.update()

    clock.tick(60)