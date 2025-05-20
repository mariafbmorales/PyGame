#Importa e inicia pacotes
import pygame 
import random

pygame.init() 
pygame.mixer.init() #Inicializando o uso de sons

#Gera tela principal
WIDTH = 600
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('No 1, rodou')


#Tela inicial do jogo (feito 50% pelo ChatGPT)
def tela_inicial(window, WIDTH, HEIGHT):
    inicio = True

    fundo1 = pygame.image.load('assets/img/teladefundo.png').convert_alpha()
    fundo = pygame.image.load('assets/img/imageminicial.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT/1.25))
    
    inicio = pygame.image.load('assets/img/Botão_inicio.png-removebg-preview.png').convert_alpha()
    inicio_img_small = pygame.transform.scale(inicio, (250, 250))

    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                inicio = False

        window.blit(fundo1, (0,0))
        window.blit(fundo, (0, 30))
        window.blit(inicio_img_small, ((175, 510)))
        pygame.display.update()

#Tela final do jogo (feito 50% pelo ChatGPT)
def tela_final(window, WIDTH, HEIGHT, jogador_vencedor):
    fundo = pygame.image.load('assets/img/teladefundo.png').convert_alpha()
    fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
    
    font_tit = pygame.font.Font('assets/font/PressStart2P.ttf', 25)
    titulo_texto = f'Jogador {jogador_vencedor} ganhou!'
    titulo = font_tit.render(titulo_texto, True, (255, 255, 255))
    botao_jn = pygame.image.load('assets/img/jogardnv-removebg-preview.png').convert_alpha()
    botao_jn = pygame.transform.scale(botao_jn, (250, 110))
    botao_sair = pygame.image.load('assets/img/botaosair-removebg-preview.png').convert_alpha()
    botao_sair = pygame.transform.scale(botao_sair, (250, 110))

    fim = True
    while fim:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                fim = False

        window.blit(fundo, (0, 0))
        window.blit(titulo, ((WIDTH - titulo.get_width()) // 2, 250))
        window.blit(botao_jn, (40, 510))
        window.blit(botao_sair, (320, 510))
        pygame.display.update()


#Inicia assets
fundo = pygame.image.load('assets/img/teladefundo.png').convert() #Imagem de fundo gerada pelo ChatGPT
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

botaoverde = pygame.image.load('assets/img/botaoverde.png').convert_alpha() 
botaoverde = pygame.transform.scale(botaoverde, (210, 75))
botaovermelho = pygame.image.load('assets/img/botaovermelho.png').convert_alpha() 
botaovermelho = pygame.transform.scale(botaovermelho, (210, 75))

DADO_WIDTH = 125
DADO_HEIGHT = 125
dado1_img = pygame.image.load('assets/img/dado1-removebg-preview.png').convert_alpha()
dado1_img_small = pygame.transform.scale(dado1_img, (DADO_WIDTH, DADO_HEIGHT))
dado2_img = pygame.image.load('assets/img/dado2-removebg-preview.png').convert_alpha()
dado2_img_small = pygame.transform.scale(dado2_img, (DADO_WIDTH, DADO_HEIGHT))
dado3_img = pygame.image.load('assets/img/dado3-removebg-preview.png').convert_alpha()
dado3_img_small = pygame.transform.scale(dado3_img, (DADO_WIDTH, DADO_HEIGHT))
dado4_img = pygame.image.load('assets/img/dado4-removebg-preview.png').convert_alpha()
dado4_img_small = pygame.transform.scale(dado4_img, (DADO_WIDTH, DADO_HEIGHT))
dado5_img = pygame.image.load('assets/img/dado5-removebg-preview.png').convert_alpha()
dado5_img_small = pygame.transform.scale(dado5_img, (DADO_WIDTH, DADO_HEIGHT))
dado6_img = pygame.image.load('assets/img/dado6-removebg-preview.png').convert_alpha()
dado6_img_small = pygame.transform.scale(dado6_img, (DADO_WIDTH, DADO_HEIGHT))
lista_dados = [0,dado1_img_small, dado2_img_small, dado3_img_small, dado4_img_small, dado5_img_small, dado6_img_small]


#Função para animar o dado girando (feito 100% pelo ChatGPT)
def animar_dado(window, lista_dados, WIDTH, HEIGHT):
    for _ in range(10):  #10 frames de "giro"
        n_animado = random.randint(1, 6)
        imagem = lista_dados[n_animado]
        window.blit(fundo, (0, 0)) #Fundo
        window.blit(imagem, ((WIDTH-DADO_WIDTH) // 2, (HEIGHT-DADO_HEIGHT) // 2))
        pygame.display.update()
        pygame.time.delay(70) #Delay entre frames


#Inicia estrutura de dados
game = True

ret_verde = pygame.Rect(50, 550, 200, 70)
ret_vermelho = pygame.Rect(350, 550, 200, 70)

pontuacao_total1 = 0
pontuacao_total2 = 0
pontuacao_partida = 0
venceu = 0
n = 0
vez = 1
perdeu = False

tela_inicial(window, WIDTH, HEIGHT) #Chamando tela inicial antes do inicio do jogo

#Loop principal
while game and venceu == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()
            if ret_verde.collidepoint(pos): #Verifica de o usuario apertou o botão verde (girou o dado)
                animar_dado(window, lista_dados, WIDTH, HEIGHT) #Animação do dado girando
                n = random.randint(1, 6) #Sorteia o dado
                print(n)
                dado_sorteado = lista_dados[n]

                if n == 2:
                    pontuacao_partida += 2
                elif n == 3:
                    pontuacao_partida += 3
                elif n == 4:
                    pontuacao_partida += 4
                elif n == 5:
                    pontuacao_partida += 5
                elif n == 6:
                    pontuacao_partida += 6
                elif n == 1:
                    pontuacao_partida = 0
                    perdeu = True
                print("Pontuacao partida", pontuacao_partida)
                
            if ret_vermelho.collidepoint(pos) or perdeu: #Verifica de o usuario apertou o botão vermelho (terminou sua jogada)
                perdeu = False
                if vez == 1:
                    pontuacao_total1 += pontuacao_partida #Adiciona a pontuação daquela partida na pontuação total do jogador 1
                    if pontuacao_total1 >= 10:
                        venceu = 1
                        print("1 venceu")
                    vez = 2
                else:
                    pontuacao_total2 += pontuacao_partida #Adiciona a pontuação daquela partida na pontuação total do jogador 2
                    if pontuacao_total2 >= 10:
                        venceu = 2
                        print("2 venceu")
                    vez = 1
                pontuacao_partida = 0
                print("Pont total 1:",pontuacao_total1)
                print("Pont total 2:",pontuacao_total2)
                print("Vez do jogador ",vez)

        
    #Gera saídas
    window.fill((0, 0, 0)) #Preenche com a cor branca
    window.blit(fundo, (0, 0))

    #Gerando imagens dos dados
    if n == 1:
        window.blit(dado1_img_small, ((WIDTH-DADO_WIDTH)//2, (HEIGHT-DADO_HEIGHT)//2))
    elif n == 2:
        window.blit(dado2_img_small, ((WIDTH-DADO_WIDTH)//2, (HEIGHT-DADO_HEIGHT)//2))
    elif n ==3:
        window.blit(dado3_img_small, ((WIDTH-DADO_WIDTH)//2, (HEIGHT-DADO_HEIGHT)//2))
    elif n == 4:
        window.blit(dado4_img_small, ((WIDTH-DADO_WIDTH)//2, (HEIGHT-DADO_HEIGHT)//2))
    elif n == 5:
        window.blit(dado5_img_small, ((WIDTH-DADO_WIDTH)//2, (HEIGHT-DADO_HEIGHT)//2))
    elif n == 6:
        window.blit(dado6_img_small, ((WIDTH-DADO_WIDTH)//2, (HEIGHT-DADO_HEIGHT)//2))

    #Gerando o texto 
    font = pygame.font.Font('assets/font/PressStart2P.ttf', 15)

    #Texto da pontuação total do jogador 1
    total1 = font.render('P1: '"{:03d}".format(pontuacao_total1), True, (244, 244, 244))
    text_rect = total1.get_rect()
    text_rect.midtop = (WIDTH //4, 20)
    window.blit(total1, text_rect)

    #Texto da pontuação total do jogador 2
    total2 = font.render('P2: '"{:03d}".format(pontuacao_total2), True, (244, 244, 244))
    text_rect = total2.get_rect()
    text_rect.midtop = (WIDTH*3//4, 20)
    window.blit(total2, text_rect)

    #Texto da pontuação da partida
    partida = font.render('JOGADA: '"{:03d}".format(pontuacao_partida), True, (244, 244, 244))
    text_rect = partida.get_rect()
    text_rect.midtop = (WIDTH //2, 700)
    window.blit(partida, text_rect)

    #Colocando de qual jogador é a vez
    if vez == 1:
        vez1 = font.render('VEZ DO JOGADOR 1', True, (244, 244, 244))
        text_rect = vez1.get_rect()
        text_rect.midtop = (290, 100)
        window.blit(vez1, text_rect)
    elif vez == 2:
        vez2 = font.render('VEZ DO JOGADOR 2', True, (244, 244, 244))
        text_rect = vez2.get_rect()
        text_rect.midtop = (290, 100)
        window.blit(vez2, text_rect)
    
    #Desenhando botões
    cor_verde = (0, 255, 0)
    window.blit(botaoverde, (50, 550))
    font = pygame.font.Font('assets/font/PressStart2P.ttf', 22)
    rodar = font.render('RODAR', True, (244, 244, 244))
    text_rect = rodar.get_rect()
    text_rect.midtop = (157, 578)
    window.blit(rodar, text_rect)

    cor_vermelha = (255, 0, 0)
    window.blit(botaovermelho, (350, 550))
    font = pygame.font.Font('assets/font/PressStart2P.ttf', 22)
    parar = font.render('PARAR', True, (244, 244, 244))
    text_rect = parar.get_rect()
    text_rect.midtop = (457, 578)
    window.blit(parar, text_rect)

    #Atualiza estado do jogo
    pygame.display.update()
if venceu != 0:
    tela_final(window, WIDTH, HEIGHT, venceu)

#Finalização
pygame.quit()