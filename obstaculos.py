import pygame, random

class Obstaculo:
    def __init__(self):

        self.sts_dball = 0

        self.sts_ki = 0
        
        if random.randint(0,1) == 0:

            self.img = pygame.image.load("Imagens/dball.png")

            self.sts_dball = 1


        else:

            self.img = pygame.image.load("Imagens/ki-blast.png")

            self.sts_ki = 1


        self.img = pygame.transform.scale(self.img,(75,75))
        self.mascara = pygame.mask.from_surface(self.img)

        self.pos_x = random.randint(0,725)
        self.pos_y = -100
        
        self.speed = random.randint(3,5)

        
    def load(self, tela):
        tela.blit(self.img,(self.pos_x,self.pos_y))

    #TENTATIVA DE MOVIMENTO E TRISTEZA PELO AMOR DE CRISTO
    def movimenta(self):
        self.pos_y +=self.speed