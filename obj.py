import random
import pygame

class Objects:
    def __init__(self):
        if random.randint(0, 1) > 0:
            # Dragon Ball
            self.imagem = pygame.image.load("Imagens/dball.png")
            self.item = "Esfera"
        else:
            # KI
            self.imagem = pygame.image.load("Imagens/ki-blast.png")
            self.item = "Ki"

        self.imagem = pygame.transform.scale(self.imagem, (64, 64))
        self.mascara = pygame.mask.from_surface(self.imagem)

        # Inicialização dos atributos de posição e velocidade
        self.pos_x = random.randint(0, 800)
        self.pos_y = 0
        self.speed = 1  # Defina a velocidade desejada aqui

    def movement(self):
        self.pos_y += self.speed
        if self.pos_y > 800:
            self.pos_y = 0

    def render(self, screen):
        screen.blit(self.imagem, (self.pos_x, self.pos_y))