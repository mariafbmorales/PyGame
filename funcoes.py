import pygame
import random
from assets import *


def desenhar_textos_instrucoes(window, linhas, x_inicial, y_inicial, espacamento):
    """Desenha na tela as linhas de instrução."""
    y = y_inicial
    for linha in linhas:
        texto = font_instrucoes.render(linha, True, (0, 0, 0))
        window.blit(texto, (x_inicial, y))
        y += espacamento


# Tela inicial do jogo
def tela_inicial(window, WIDTH, HEIGHT):
    """ Função responsável por exibir a tela inicial """
    inicio = True
    
    # Definindo posição e tamanho dos botões que aparecem na tela inicial do jogo
    ret_start = pygame.Rect(250, 570, 175, 150)

    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inicio = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                pos = pygame.mouse.get_pos()
                if ret_start.collidepoint(pos):
                    inicio = False

        window.blit(background_inicio, (0, 0))
        window.blit(logo, (WIDTH // 2 - 235, 70))
        window.blit(botaoinicio_img_small, (175, 490))
        pygame.display.update()


# Criando tela de instruções
def tela_instrucoes(window, WIDTH, HEIGHT):
    """ Função responsável por exibir a tela de instruções """
    tela_meio = True 

    # Definindo posição e tamanho dos botões que aparecem na de instruções
    ret_continuar = pygame.Rect(250, 570, 175, 150)

    linhas_instrucoes = [
        'Instruções: o jogador da vez poderá rodar o',
        'dado quantas vezes desejar. Para isso, deve',
        'clicar no botão “rodar” . Quando quiser parar',
        'clicara no botão “parar”, e os pontos feitos',
        'na rodada serão adicionados a pontuação total',
        'Entretanto, se cair a face do dado com o nú-',
        'mero 1, o jogador perderá sua vez de jogar e',
        'sua pontuação da rodada será zerada, passando',
        'a vez para o seguinte jogador. O jogo é fina-',
        'lizado quando algum dos dois jogadores fizer',
        '100 pontos.'
    ]

    while tela_meio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tela_meio = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                pos = pygame.mouse.get_pos()
                if ret_continuar.collidepoint(pos):
                    tela_meio = False

        window.blit(fundo_instrucoes, (0, -20))
        window.blit(botao_continuar, (175, 560))

        desenhar_textos_instrucoes(window, linhas_instrucoes, 80, 70, 40)

        pygame.display.update()

    
# Tela final do jogo
def tela_final(window, WIDTH, HEIGHT, jogador_vencedor):
    """
    window: recebendo tela do pygame
    WIDTH: tamanho no eixo x
    HEIGHT: tamanho no eixo y
    jogador_vencedor: qual dos jogadores venceu 
    """

    # Carrega a imagem do vencedor de acordo com o jogador
    if jogador_vencedor == 1:
        imagem_vencedor = pygame.image.load('assets/img/1vencedor.png').convert_alpha()
    elif jogador_vencedor == 2:
        imagem_vencedor = pygame.image.load('assets/img/2vencedor.png').convert_alpha()

    # Ajusta o tamanho da imagem
    imagem_vencedor = pygame.transform.scale(imagem_vencedor, (400, 400))
    # Posição da imagem do vencedor
    pos_imagem = imagem_vencedor.get_rect(center=(WIDTH // 2, HEIGHT // 2.3))

    # Posição botão de sair
    ret_fimdejogo = pygame.Rect(250, 570, 175, 150)

    # Carregando as imagens da animação
    pinkfireworks_imgs = []
    purplefireworks_imgs = []
    yellowfireworks_imgs = []

    # Fazendo o loop que ira gerar a animação
    for i in range(1, 8):
        pinkimg_path = 'assets/img/pinkfireworks/' + str(i) + '.png'
        pink_img = pygame.image.load(pinkimg_path).convert_alpha()
        pinkfireworks_imgs.append(pygame.transform.scale(pink_img, (250, 250)))

        purpleimg_path = 'assets/img/purplefireworks/' + str(i) + '.png'
        purple_img = pygame.image.load(purpleimg_path).convert_alpha()
        purplefireworks_imgs.append(pygame.transform.scale(purple_img, (250, 250)))

        yellowimg_path = 'assets/img/yellowfireworks/' + str(i) + '.png'
        yellow_img = pygame.image.load(yellowimg_path).convert_alpha()
        yellowfireworks_imgs.append(pygame.transform.scale(yellow_img, (250, 250)))

    clock = pygame.time.Clock()
    frame = 0  # Controla o índice da animação

    fim = True
    while fim:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                pos = pygame.mouse.get_pos()
                if ret_fimdejogo.collidepoint(pos):
                    fim = False

        window.blit(fundo, (0, 0))
        window.blit(imagem_vencedor, pos_imagem)
        window.blit(botao_sair, (WIDTH // 2 - 125, 560))

        # Exibe a imagem atual da animação (em loop)
        pinkfireworks_img = pinkfireworks_imgs[frame // 5 % len(pinkfireworks_imgs)]
        window.blit(pinkfireworks_img, (-20, 100))
        window.blit(pinkfireworks_img, (20, 420))

        purplefireworks_img = purplefireworks_imgs[frame // 5 % len(purplefireworks_imgs)]
        window.blit(purplefireworks_img, (175, -4))

        yellowfireworks_img = yellowfireworks_imgs[frame // 5 % len(yellowfireworks_imgs)]
        window.blit(yellowfireworks_img, (600 - 230, 100))
        window.blit(yellowfireworks_img, (600 - 270, 420))

        pygame.display.update()
        clock.tick(30)

        frame += 1
    

# Função para animar o dado girando
def animar_dado(window, lista_dados, WIDTH, HEIGHT):
    """Função responsável por rodar o dado"""
    for _ in range(10):
        n_animado = random.randint(1, 6)
        imagem = lista_dados[n_animado]
        window.blit(fundo, (0, 0))
        window.blit(imagem, ((WIDTH - DADO_WIDTH) // 2, (HEIGHT - DADO_HEIGHT) // 2))
        pygame.display.update()
        pygame.time.delay(70)