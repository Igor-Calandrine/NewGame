import pygame
from pygame.sprite import Sprite, Group

class Blaster(Sprite):
    # Classe para configurar os ataques em blaster
    
    def __init__ (self, tela, androide_01):
        super().__init__() #herde comfigurações da Classe Sprite em pygame

        self.tela = tela
        self.tela_surface = tela.get_rect()
        self.androide_01 = androide_01

        self.blaster_velocidade = 0.2
        self.blaster_largura = 20
        self.blaster_altura = 10
        self.blaster_cor = (60, 60, 60)
        self.direção = androide_01.direção

        # Surface do blaster
        self.blaster_surface = pygame.Rect(0, 0, self.blaster_largura, self.blaster_altura)

        # Posição do tiro
        deslocamentoX = 22
        self.blaster_surface.centery = self.androide_01.imagem_margem.centery

        if self.androide_01.direção == "direita":
            self.blaster_surface.centerx = self.androide_01.imagem_margem.centerx + deslocamentoX
        elif self.androide_01.direção == "esquerda":
            self.blaster_surface.centerx = self.androide_01.imagem_margem.centerx - deslocamentoX

        self.blasterx_float = float(self.blaster_surface.x)

    def movimento_blaster(self):

        if self.direção == "direita":       
            self.blasterx_float += self.blaster_velocidade
            self.blaster_surface.x = int(round(self.blasterx_float))

            if self.blaster_surface.left > self.tela_surface.right:
                self.kill()

        elif self.direção == "esquerda":
            self.blasterx_float -= self.blaster_velocidade
            self.blaster_surface.x = int(round(self.blasterx_float))

            if self.blaster_surface.right < self.tela_surface.left:
                self.kill()

    def renderizar(self):
        pygame.draw.rect(self.tela, self.blaster_cor, self.blaster_surface)