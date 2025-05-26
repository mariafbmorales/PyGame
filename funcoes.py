import pygame
import random
from assets import *

#Tela inicial do jogo (feito 50% pelo ChatGPT)
def tela_inicial(window, WIDTH, HEIGHT):
    """ Função responsável por exibir a tela inicial 

    Args:
        window: recebendo tela do pygame
        WIDTH: tamanho da tela no eixo x
        HEIGHT: tamanho da tela no eixo y
    """
    inicio = True
    
    #Definindo posição e tamanho dos botões que aparecem na tela inicial do jogo
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

        window.blit(background_inicio, (0,0))
        window.blit(logo, (WIDTH//2-235, 70))
        window.blit(botaoinicio_img_small, ((175, 490)))
        pygame.display.update()


#Criando tela de instruções
def tela_instrucoes(window, WIDTH, HEIGHT):
    """ Função responsável por exibir a tela de instruções

    Args:
        window: recebendo tela do pygame
        WIDTH: tamanho da tela no eixo x
        HEIGHT: tamanho da tela no eixo y
    """
    tela_meio = True 

    #Definindo posição e tamanho dos botões que aparecem na de intruções
    ret_continuar = pygame.Rect(250, 570, 175, 150)

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

        #Texto das intruções
        texto = font_instrucoes.render('Instruções: o jogador da vez poderá rodar o', True, (0, 0, 0))
        texto2 = font_instrucoes.render('dado quantas vezes desejar. Para isso, deve', True, (0, 0, 0))
        texto3 = font_instrucoes.render('clicar no botão “rodar” . Quando quiser parar', True, (0, 0, 0))
        texto4 = font_instrucoes.render('clicara no botão “parar”, e os pontos feitos', True, (0, 0, 0))
        texto5 = font_instrucoes.render('na rodada serão adicionados a pontuação total', True, (0, 0, 0))
        textox = font_instrucoes.render('Entretanto, se cair a face do dado com o nú-', True, (0, 0, 0))
        texto6 = font_instrucoes.render('mero 1, o jogador perderá sua vez de jogar e', True, (0, 0, 0))
        texto7 = font_instrucoes.render('sua pontuação da rodada será zerada, passando', True, (0, 0, 0))
        texto8 = font_instrucoes.render('a vez para o seguinte jogador. O jogo é fina-', True, (0, 0, 0))
        texto9 = font_instrucoes.render('lizado quando algum dos dois jogadores fizer', True, (0, 0, 0))
        texto10 = font_instrucoes.render('100 pontos.', True, (0, 0, 0))

    #Posição dos textos
        window.blit(texto, (80, 70))
        window.blit(texto2, (80, 110))
        window.blit(texto3, (80, 150))
        window.blit(texto4, (80, 190))
        window.blit(texto5, (80, 230))
        window.blit(textox, (80, 270))
        window.blit(texto6, (80, 310))
        window.blit(texto7, (80, 350))
        window.blit(texto8, (80, 390))
        window.blit(texto9, (80, 430))
        window.blit(texto10, (80, 470))

        pygame.display.update()

    
#Tela final do jogo (feito 50% pelo ChatGPT)
def tela_final(window, WIDTH, HEIGHT, jogador_vencedor):
    """_summary_

    Args:
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
    pos_imagem = imagem_vencedor.get_rect(center=(WIDTH//2, HEIGHT//2.3))

    #Posição botão de sair
    ret_fimdejogo = pygame.Rect(250, 570, 175, 150)

    #Carregando as imagens da animação
    pinkfireworks_imgs = []
    purplefireworks_imgs = []
    yellowfireworks_imgs = []
    #Fazendo o loop que ira gerar a animação
    for i in range(1, 8):  #Imagens numeradas de 1 a 7
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
    frame = 0  #Controla o índice da animação

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
        window.blit(botao_sair, (WIDTH//2-125, 560))

        # Exibe a imagem atual da animação (em loop)
        pinkfireworks_img = pinkfireworks_imgs[frame // 5 % len(pinkfireworks_imgs)]  # Controla velocidade com "// 5"
        window.blit(pinkfireworks_img, (-20, 100))  
        pinkfireworks_img = pinkfireworks_imgs[frame // 5 % len(pinkfireworks_imgs)]  # Controla velocidade com "// 5"
        window.blit(pinkfireworks_img, (20, 420))  

        purplefireworks_img = purplefireworks_imgs[frame // 5 % len(purplefireworks_imgs)]  # Controla velocidade com "// 5"
        window.blit(purplefireworks_img, (175, -4))  
        

        yellowfireworks_img = yellowfireworks_imgs[frame // 5 % len(yellowfireworks_imgs)]  # Controla velocidade com "// 5"
        window.blit(yellowfireworks_img, (600-230, 100))  
        yellowfireworks_img = yellowfireworks_imgs[frame // 5 % len(yellowfireworks_imgs)]  # Controla velocidade com "// 5"
        window.blit(yellowfireworks_img, (600-270, 420))  

        pygame.display.update()
        clock.tick(30)  # 30 FPS

        frame += 1
    
#Função para animar o dado girando (feito 100% pelo ChatGPT)
def animar_dado(window, lista_dados, WIDTH, HEIGHT):
    """Função responsável por rodar o dado

    Args:
        window: recebendo tela do pygame
        lista_dados: lista de dados
        WIDTH: tamanho da tela no eixo x
        HEIGHT: tamanho da tela no eixo y
    """
    for _ in range(10):  #10 frames de "giro"
        n_animado = random.randint(1, 6)
        imagem = lista_dados[n_animado]
        window.blit(fundo, (0, 0)) #Fundo
        window.blit(imagem, ((WIDTH-DADO_WIDTH) // 2, (HEIGHT-DADO_HEIGHT) // 2))
        pygame.display.update()
        pygame.time.delay(70) #Delay entre frames
