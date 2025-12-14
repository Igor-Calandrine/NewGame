import pygame

arquivos_imagem = r"C:\Users\perni\OneDrive\Área de Trabalho\NewGame\configuracoes\personagem\img"   

def img_parado():

    imagens_parado = []
    mascaras_parado = []
  
    for i in range(1, 5):
        imagem_parado = pygame.image.load(f"{arquivos_imagem}/androide_01_parado{i}.png").convert_alpha()
        mascara_parado = pygame.mask.from_surface(imagem_parado)
        imagens_parado.append(imagem_parado)
        mascaras_parado.append(mascara_parado)
    for i in reversed(range(1, 5)):
        imagem_parado = pygame.image.load(f"{arquivos_imagem}/androide_01_parado{i}.png").convert_alpha()
        mascara_parado = pygame.mask.from_surface(imagem_parado)
        imagens_parado.append(imagem_parado)
        mascaras_parado.append(mascara_parado)

    return imagens_parado, mascaras_parado


def img_correndo():

    imagens_correndo = []
    mascaras_correndo = []

    for i in range(1, 17):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_d{i}.png").convert_alpha()
        mascara = pygame.mask.from_surface(imagem)
        imagens_correndo.append(imagem)
        mascaras_correndo.append(mascara)  

    return imagens_correndo, mascaras_correndo  

def img_pulando():

    imagens_pulando = []
    mascaras_pulando = []

    for i in range(1, 9):
        imagem = pygame.image.load(f"{arquivos_imagem}/androide_01_pulando{i}.png").convert_alpha()
        mascara = pygame.mask.from_surface(imagem)
        imagens_pulando.append(imagem)
        mascaras_pulando.append(mascara)  

    return imagens_pulando, mascaras_pulando 

