import pygame

pygame.init()

#CONFIGURAÇÕES BASICAS JOGO
tela = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Jogo das gotas de sangue caindo do céu")

#CARREGANDO IMAGENS JOGOS
Fundo = pygame.image.load("Imagens/fundo.jpg")
Fundo = pygame.transform.scale(Fundo,(800,600))

running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    
    pygame.display.update()

    clock.tick(60)

    tela.blit(Fundo,(0,0))