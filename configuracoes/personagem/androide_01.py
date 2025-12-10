""".get_rect, set_mode - transformam a imagem em dados de Surface retângular. Suas variáveis tem nomes para completar os dados. Por isso a variável #tela é usada aqui."""
import pygame

from .carregar_imagens import *


class Androide_01():
 
    def __init__ (self, tela):

        self.tela = tela 

        self.imagens_parado, self.mascaras_parado = img_parado()
        self.imagens_correndo, self.mascaras_correndo = img_correndo()
        self.imagem_pulo_direita = img_correndo()
        self.imagem_pulo_esquerda = img_correndo()

        #Criação da imagem e seu surface
        self.imagem = self.imagens_parado[0]
        self.retangulo = self.imagem.get_rect()

        #Referênia de posicionamento da imagem
        self.tela_margem = tela.get_rect() 
        self.retangulo.centerx = self.tela_margem.centerx
        self.retangulo.centery = self.tela_margem.centery
        self.retangulo.bottom = self.tela_margem.bottom
        
        self.centerx_float = float(self.retangulo.centerx)
        self.centery_float = float(self.retangulo.centery)

        #Movimentaação
        self.frame_atual = 0
        self.velocidade_frame = 0.01538
        
        self.direção = "direita"

        self.movimento_direita = False
        self.movimento_esquerda = False
        self.movimento_descer = False
        self.movimento_pulo = False
        
        self.velocidade = 0.25
        
        self.velocidade_pulo_i = -0.40
        self.velocidade_pulo = 0

        self.velocidade_y = 0
        self.gravidade = 0.00115
        
        self.pulos_maximo = 2
        self.contador_pulo = 2
        self.segundo_pulo = False
        
        self.posição_chão = True
        
        
    def movimentação (self):
        # Limitar na tela
        if self.retangulo.right >= self.tela_margem.right:
            self.movimento_direita = False
        if self.retangulo.left <= self.tela_margem.left:
            self.movimento_esquerda = False
        if self.retangulo.top <= self.tela_margem.top:
            self.movimento_pulo = False
        if self.retangulo.bottom >= self.tela_margem.bottom:
            self.movimento_descer = False
            
        # Direita
        if self.movimento_direita == True: 
            self.direção = "direita"  
            self.centerx_float += + self.velocidade
            
        # Esquerda
        if self.movimento_esquerda == True: 
            self.direção = "esquerda"  
            self.centerx_float += - self.velocidade
          
        # Flag se esta no chão
        if self.retangulo.bottom < self.tela_margem.bottom:
            self.posição_chão = False
        elif self.retangulo.bottom >= self.tela_margem.bottom:
            self.posição_chão = True
        
        # Pulo saindo do chão
        if self.movimento_pulo == True and self.posição_chão == True:
            self.velocidade_y = self.velocidade_pulo_i
            self.posição_chão = False
            self.segundo_pulo = False
            self.contador_pulo = 1

        # Segundo pulo
        elif self.movimento_pulo == True and self.posição_chão == False and self.contador_pulo > 0 and self.segundo_pulo == True:
            self.velocidade_y = self.velocidade_pulo_i
            self.contador_pulo = 0
                
        # Movimento Gravitcional
        self.velocidade_y += self.gravidade
        self.centery_float += self.velocidade_y

        # Chegou no chão
        if self.movimento_pulo == False and self.retangulo.bottom >= self.tela_margem.bottom: 
            self.retangulo.bottom = self.tela_margem.bottom
            self.centery_float = self.retangulo.centery

            self.contador_pulo = self.pulos_maximo
            self.velocidade_y = 0
            self.posição_chão = True

        # Animação de movimentos no chão
        if self.posição_chão == True:

            #Parado Direita
            if self.direção == "direita" and self.movimento_direita == False and self.movimento_esquerda == False:
                self.frame_atual += + self.velocidade_frame/4

                if self.frame_atual >= len(self.imagens_parado):
                    self.frame_atual = 0

                self.imagem = self.imagens_parado[int(self.frame_atual)]
                self.mascara = self.mascaras_parado[int(self.frame_atual)]

            #Parado Esquerda
            elif self.direção == "esquerda" and self.movimento_direita == False and self.movimento_esquerda == False:
                self.frame_atual += + self.velocidade_frame/4

                if self.frame_atual >= len(self.imagens_parado):
                    self.frame_atual = 0

                self.imagem = self.imagens_parado[int(self.frame_atual)]
                self.imagem = pygame.transform.flip(self.imagem, True, False)
                self.mascara = pygame.transform.flip(self.imagem, True, False)
            
            #Correndo Direita
            if self.direção == "direita" and self.movimento_direita == True:
                self.frame_atual += + self.velocidade_frame

                if self.frame_atual >= len(self.imagens_correndo):
                    self.frame_atual = 2

                self.imagem = self.imagens_correndo[int(self.frame_atual)]
                self.mascara = self.mascaras_correndo[int(self.frame_atual)]

            #Correndo Esquerda
            elif self.direção == "esquerda" and self.movimento_esquerda == True:
                self.frame_atual += + self.velocidade_frame

                if self.frame_atual >= len(self.imagens_correndo):
                    self.frame_atual = 2

                self.imagem = self.imagens_correndo[int(self.frame_atual)]
                self.imagem = pygame.transform.flip(self.imagem, True, False)
                self.mascara = self.mascaras_correndo[int(self.frame_atual)]

        #Posição arredondada
        self.retangulo.centerx = int(round(self.centerx_float))  
        self.retangulo.centery = int(round(self.centery_float)) 

    def blitme(self):
        #Desenha a imagem
        self.tela.blit(self.imagem, self.retangulo)


                
            

        
    
    


  
