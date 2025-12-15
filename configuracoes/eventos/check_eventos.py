import sys
import pygame
from ..personagem.androide_01 import Androide_01

#Laço para eventos do teclado e mouse
def check(androide_01):

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
          sys.exit()
        
        # Movimento eixo X
        if evento.type == pygame.KEYDOWN:
        
            if evento.key == pygame.K_RIGHT:
                androide_01.movimento_correr = True
                androide_01.movimento_direita = True
                androide_01.movimento_esquerda = False
            elif evento.key == pygame.K_LEFT:
                androide_01.movimento_correr = True
                androide_01.movimento_direita = False
                androide_01.movimento_esquerda = True
     
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                androide_01.movimento_direita = False
            elif evento.key == pygame.K_LEFT:
                androide_01.movimento_esquerda = False

        if androide_01.movimento_esquerda == False and androide_01.movimento_direita == False:
            androide_01.movimento_correr = False

        # Pulo
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
            androide_01.movimento_pulo = True

        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
            androide_01.movimento_pulo = False
            androide_01.segundo_pulo = True
            
            # Limita altura do pulo
            if androide_01.velocidade_y < 0:
                androide_01.velocidade_y = 0

        # Descer
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
            androide_01.movimento_descer = True
        
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
            androide_01.movimento_descer = False
        

        
