import pygame

class Controle_Tiro():
    def __init__(self):
        self.blaster_tiro = True
        self.blaster_tempo_delay = 400
        self.blaster_tempo_atual = 0
        self.blaster_tempo_inicial = 0

    def tempo_tiro(self):
        self.blaster_tempo_atual = pygame.time.get_ticks()

        if self.blaster_tempo_atual - self.blaster_tempo_inicial >= self.blaster_tempo_delay:
            self.blaster_tiro = True
            
        else:
            self.blaster_tiro = False