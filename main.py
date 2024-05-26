import pygame, random
from player import Player
from obstaculos import Obstaculo

pygame.init()


#Configurações básicas do jogo
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Jogo do ano 2024")
clock = pygame.time.Clock()
pontos = 0

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

power_sound = pygame.mixer.Sound("sounds/power_sound.mp3")


#Obstáculos
obstaculos = []

#Pra tirar o bug chato insuportavel filho da puta de usar tudo de uma vez so
poder_ativado = False

#contagem de itens ruins que ele pegou
itens_ki = 0

#O jogo rodando em si 
rodando = True


#Faz ser possível quitar do jogo kkkkkk
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e and jogador.power > 0 and not poder_ativado:
                jogador.power -= 1
                power_sound.play()
                obstaculos.clear()
                poder_ativado = True

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_e:
                poder_ativado = False

    #Spawna os sprites e seus movimentos
    tela.blit(Fundo,(0,0))

    #PONTUAÇÃO
    font = pygame.font.SysFont("Comic Sans MS",30, True, False)
    pontuação = font.render(f"Poder de Luta: {pontos}",True,(232, 235, 52))
    tela.blit(pontuação,(0,4))

    #PLAYER 1 CONFIG
    jogador.print_char(tela)
    jogador.movements(pygame.K_a, pygame.K_d)



    #OBSTACULOS
    if len(obstaculos) <= 7:
        novo_obstaculo = Obstaculo()  # Cria um novo obstáculo
        obstaculos.append(novo_obstaculo)  # Adiciona na lista de obstáculos
    for obstaculokk in obstaculos:
        if obstaculokk.pos_y > 600:
            obstaculos.remove(obstaculokk)
    

    # COLOCA OS OBSTACULOS NA TELA E CHECKA A COLISAO
    for obstaculo in obstaculos:
        obstaculo.load(tela)
        obstaculo.movimenta()

        rel_pos = (obstaculo.pos_x - jogador.pos_x, obstaculo.pos_y - jogador.pos_y)
        if jogador.mascara.overlap(obstaculo.mascara, rel_pos):

            if obstaculo.sts_dball == 1:
                pontos += 100
                point_up.play()

            else:
                pontos -= 100
                itens_ki +=1
                if itens_ki >=3:
                    rodando = False
                if pontos < 0:
                    pontos = 0
                point_down.play()
            obstaculos.remove(obstaculo)


    pygame.display.update()

    clock.tick(60)