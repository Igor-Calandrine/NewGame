""".get_rect, set_mode - transformam a imagem em dados de Surface retângular. Suas variáveis tem nomes para completar os dados. Por isso a variável #tela é usada aqui."""
import pygame

from .carregar_imagens import *


class Androide_01():
 
    def __init__ (self, tela):

        self.tela = tela 

        self.imagens_parado, self.mascaras_parado = img_parado()
        self.imagens_correndo, self.mascaras_correndo = img_correndo()
        self.imagens_pulando, self.mascaras_pulando = img_pulando()
        self.imagens_aterrisando, self.mascaras_aterrisando = img_aterrisando()
        

        # Criação da surface da tela, imagem
        self.imagem = self.imagens_parado[0]
        self.tela_margem = tela.get_rect() 
        self.imagem_margem = self.imagem.get_rect()

        # Referênia de posicionamento da imagem
        self.imagem_margem.centerx = self.tela_margem.centerx
        self.imagem_margem.bottom = self.tela_margem.bottom
        
        self.centerx_float = float(self.imagem_margem.centerx)
        self.centery_float = float(self.imagem_margem.centery)

        # Frame Animação
        self.frame_parado = 0
        self.frame_parado_vel = 0.003845
        self.frame_correndo = 0
        self.frame_correndo_vel = 0.01538
        self.frame_pulando = 0
        self.frame_pulando_vel = 0.0119
        self.frame_aterrisando = 0
        self.frame_aterrisando_vel = 0.01685

        # Flag de movimentação bool from check_eventos.py
        self.direção = "direita"
        self.movimento_direita = False
        self.movimento_esquerda = False
        self.movimento_correr = False
        self.movimento_descer = False
        self.movimento_pulo = False
        self.movimento_aterrisando = False
        
        # Velocidade de movimento
        self.velocidade = 0.25
        self.velocidade_pulo_i = -0.40
        self.velocidade_pulo = 0

        self.velocidade_y = 0
        self.gravidade = 0.00115
        
        self.pulos_maximo = 2
        self.contador_pulo = self.pulos_maximo
        self.segundo_pulo = False
        
        self.posição_chão = True
        
        
    def movimentação (self):
        # Limitar na tela
        if self.imagem_margem.right >= self.tela_margem.right:
            self.movimento_direita = False
        if self.imagem_margem.left <= self.tela_margem.left:
            self.movimento_esquerda = False
        if self.imagem_margem.top <= self.tela_margem.top:
            self.movimento_pulo = False
        if self.imagem_margem.bottom >= self.tela_margem.bottom:
            self.movimento_descer = False

        # Direita
        if self.movimento_correr == True and self.movimento_direita == True: 
            self.direção = "direita"  
            self.centerx_float += self.velocidade
            
        # Esquerda
        if self.movimento_correr == True and self.movimento_esquerda == True: 
            self.direção = "esquerda"  
            self.centerx_float -= self.velocidade
          
        # Parado
        if self.movimento_direita == False and self.movimento_esquerda == False:
            self.movimento_correr = False

        # Flag se esta no chão
        if self.imagem_margem.bottom < self.tela_margem.bottom:
            self.posição_chão = False
        elif self.imagem_margem.bottom >= self.tela_margem.bottom:
            self.posição_chão = True
        
        # Pulo saindo do chão
        if self.movimento_pulo == True and self.posição_chão == True:
            self.velocidade_y = self.velocidade_pulo_i
            self.posição_chão = False
            self.segundo_pulo = False
            self.contador_pulo = 1

        # Segundo pulo
        elif self.movimento_pulo == True and self.posição_chão == False:
            if self.segundo_pulo == True and self.contador_pulo > 0:
                self.velocidade_y = self.velocidade_pulo_i
                self.contador_pulo = 0
                
        # Movimento Gravitcional
        self.velocidade_y += self.gravidade
        self.centery_float += self.velocidade_y

        # Chegou no chão
        if self.movimento_pulo == False and self.imagem_margem.bottom >= self.tela_margem.bottom: 
            self.imagem_margem.bottom = self.tela_margem.bottom
            self.centery_float = self.imagem_margem.centery

            self.contador_pulo = self.pulos_maximo
            self.velocidade_y = 0
            self.posição_chão = True

# ------------------------------------------------------------------
        # Animação de movimentos no chão
        if self.posição_chão == True and self.movimento_pulo == False:
            self.frame_pulando = 0
        
            # Parado
            if self.movimento_aterrisando == False and self.movimento_correr == False:
                self.frame_parado += + self.frame_parado_vel
                if self.frame_parado >= len(self.imagens_parado):
                    self.frame_parado = 0
                
                # Direita
                if self.direção == "direita":
                    self.imagem = self.imagens_parado[int(self.frame_parado)]
                    self.mascara = self.mascaras_parado[int(self.frame_parado)]
                # Esquerda
                elif self.direção == "esquerda":
                    self.imagem = self.imagens_parado[int(self.frame_parado)]
                    self.imagem = pygame.transform.flip(self.imagem, True, False)
                    self.mascara = pygame.mask.from_surface(self.imagem)

            # Aterrisando
            if self.movimento_aterrisando == True and self.movimento_correr == False:
                self.frame_aterrisando += self.frame_aterrisando_vel
                self.frame_aterrisando = min(max((self.frame_aterrisando), 0), 2)
                print(self.frame_aterrisando)
                
                if self.frame_aterrisando == 2:
                    self.movimento_aterrisando = False
                    self.frame_aterrisando = 0

                # Direita
                if self.direção == "direita":
                    self.imagem = self.imagens_aterrisando[int(self.frame_aterrisando)]
                    self.mascara = self.mascaras_aterrisando[int(self.frame_aterrisando)]
                # Esquerda
                elif self.direção == "esquerda":
                    self.imagem = self.imagens_aterrisando[int(self.frame_aterrisando)]
                    self.imagem = pygame.transform.flip(self.imagem, True, False)
                    self.mascara = pygame.mask.from_surface(self.imagem)
            
            # Correndo
            if self.movimento_correr == True:
                self.frame_correndo += self.frame_correndo_vel
                
                if self.frame_correndo >= len(self.imagens_correndo):
                    self.frame_correndo = 2

                # Direita
                if self.direção == "direita":
                    self.imagem = self.imagens_correndo[int(self.frame_correndo)]
                    self.mascara = self.mascaras_correndo[int(self.frame_correndo)]
                # Esquerda
                elif self.direção == "esquerda":
                    self.imagem = self.imagens_correndo[int(self.frame_correndo)]
                    self.imagem = pygame.transform.flip(self.imagem, True, False)
                    self.mascara = pygame.mask.from_surface(self.imagem)

        # No ar
        if self.posição_chão == False:
            self.frame_pulando += self.frame_pulando_vel

            # Sudindo
            if self.velocidade_y <= 0:
                self.frame_pulando = min(max((self.frame_pulando), 0), 3)
            # Descendo
            elif self.velocidade_y > 0:
                self.frame_pulando = min(max(self.frame_pulando, 4), 7)
                self.movimento_aterrisando = True

            if self.direção == "direita":
                self.imagem = self.imagens_pulando[int(self.frame_pulando)]
                self.mascara = self.mascaras_pulando[int(self.frame_pulando)]
            elif self.direção == "esquerda":
                self.imagem = self.imagens_pulando[int(self.frame_pulando)]
                self.imagem = pygame.transform.flip(self.imagem, True, False)
                self.mascara = pygame.mask.from_surface(self.imagem) 

        #Posição arredondada e atualizada
        self.imagem_margem.centerx = int(round(self.centerx_float))  
        self.imagem_margem.centery = int(round(self.centery_float)) 

    def redenrizar (self):
        #Desenha a imagem
        self.tela.blit(self.imagem, self.imagem_margem)


                
            

        
    
    


  
