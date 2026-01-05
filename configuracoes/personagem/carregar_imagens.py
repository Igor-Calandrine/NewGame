import pygame

arquivos_imagem = r"C:\Users\perni\OneDrive\Área de Trabalho\NewGame\configuracoes\personagem\img"

# Tool para evitar repetições
def inserir_imagens_lista(imagem, imagens, mascaras):
        mascara = pygame.mask.from_surface(imagem)
        imagens.append(imagem)
        mascaras.append(mascara) 

# --------------------------------------------------------------------------------------------------------------- #

def img_parado():
    imagens = []
    mascaras = []
  
    for i in range(1, 5):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_parado{i}.png").convert_alpha()
        inserir_imagens_lista(imagem, imagens, mascaras)
    for i in reversed(range(1, 5)):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_parado{i}.png").convert_alpha()
        inserir_imagens_lista(imagem, imagens, mascaras)
    return imagens, mascaras


def img_correndo():
    imagens = []
    mascaras = []

    for i in range(1, 17):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_d{i}.png").convert_alpha()
        inserir_imagens_lista(imagem, imagens, mascaras) 
    return imagens, mascaras  


def img_pulando():
    imagens = []
    mascaras = []

    for i in range(1, 9):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_pulando{i}.png").convert_alpha()
        inserir_imagens_lista(imagem, imagens, mascaras)
    return imagens, mascaras 


def img_aterrisando():
    imagens = []
    mascaras = []

    for i in range(1, 4):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_aterrisando{i}.png").convert_alpha()
        inserir_imagens_lista(imagem, imagens, mascaras) 
    return imagens, mascaras


def img_atirando_parado ():
    imagens = []
    mascaras = []

    for i in range(1, 9):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_atirando_pa{i}.png").convert_alpha()
        inserir_imagens_lista(imagem, imagens, mascaras)
    return imagens, mascaras



