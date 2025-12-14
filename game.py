import sys
import pygame
import configuracoes.eventos.check_eventos as eventos

from configuracoes.config_tela import Config_tela
from configuracoes.personagem.androide_01 import Androide_01

def jogo_aberto():
    #Inicia o jogo e abre a tela
    pygame.init()

    config_tela = Config_tela()

    tela = pygame.display.set_mode((config_tela.horizontal, config_tela.vertical))
    tela_fundo = (config_tela.fundo)
    pygame.display.set_caption("Android 01")

    androide_01 = Androide_01(tela)
    
    #Laço que mantém o jogo funcionando
    while True:

        eventos.check(androide_01)

        tela.fill(tela_fundo) #Pinta o fundo da tela
        androide_01.movimentação()
        androide_01.redenrizar()
        pygame.display.flip() #Deixa a tela mais recente visível

jogo_aberto()


        

