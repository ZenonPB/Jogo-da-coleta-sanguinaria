import random, pygame

class Objects:
    def __init__(self,img, img_x,img_y):
        self.imagem = pygame.image.load(img)

        self.width = img_x
        self.height = img_y

        self.imagem = pygame.transform.scale(self.imagem,(self.width,self.height))

        self.pos_x = random.randint(0,800)
        self.pos_y = 0

        self.speed = random.randint(3,5)
        
        self.mascara = pygame.mask.from_surface(self.imagem)

    def pos_rng(pos_x):
        pos_x = random.randint()


    def movement(self):
        self.pos_y = self.pos_y + self.speed
        if self.pos_y > 800:
            self.pos_x = random.randint(0,800)
            self.speed = random.randint(3,5)
            self.pos_y = -100

    def render(self,screen):
        screen.blit(self.imagem,(self.pos_x,self.pos_y))