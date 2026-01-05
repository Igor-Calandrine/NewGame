import sys
import pygame
from pygame.sprite import Group
import configuracoes.eventos.check_eventos as eventos

from configuracoes.config_tela import Config_tela
from configuracoes.controle_tiro import Controle_Tiro
from configuracoes.personagem.androide_01 import Androide_01
from configuracoes.personagem.ataques.blaster import Blaster

def jogo_aberto():
    #Inicia o jogo e abre a tela
    pygame.init()

    config_tela = Config_tela()

    tela = pygame.display.set_mode((config_tela.horizontal, config_tela.vertical))
    tela_fundo = (config_tela.fundo)
    pygame.display.set_caption("Android 01")

    androide_01 = Androide_01(tela)
    blaster = Blaster(tela, androide_01)
    blasters = Group()
    controle_tiro = Controle_Tiro()
    

    #Laço que mantém o jogo funcionando
    while True:

        eventos.check(tela, androide_01, blasters, controle_tiro)

        tela.fill(tela_fundo) #Pinta o fundo da tela
        androide_01.movimentação()
        androide_01.renderizar()
        
        for blaster in blasters:
            blaster.movimento_blaster()
            blaster.renderizar()

        controle_tiro.tempo_tiro()
        

        pygame.display.flip() #Deixa a tela mais recente visível

jogo_aberto()


        

