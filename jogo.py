from assets import *
from funcoes import *


#Definindo posição e tamanho dos botões da tela principal
ret_verde = pygame.Rect(60, 550, 210, 70) 
ret_vermelho = pygame.Rect(WIDTH-250, 550, 180, 70)

#Inicia estrutura de dados
game = True

ponto_vencer = 100
pontuacao_total1 = 0
pontuacao_total2 = 0
pontuacao_partida = 0
venceu = 0
n = 0
vez = 1
perdeu = False

tela_inicial(window, WIDTH, HEIGHT) #Chamando tela inicial antes do inicio do jogo
tela_instrucoes(window, WIDTH, HEIGHT)  # Chama tela de intruções sobre o jogo

def rolagem(window, lita_dados, WIGTH, HEIGHT, pontuacao_partida):
    animar_dado(window, lista_dados, WIDTH, HEIGHT)
    n = random.randint(1, 6)
    perdeu = False

    if n == 1:
        perdeu_sound.play()
        pontuacao_partida = 0
        perdeu = True
    else:
        pontuacao_partida += n
    
    return n
    return pontuacao_partida
    return perdeu

def fim_vez(vez, pontuacao_partida, pontuacao_total1, pontuacao_total2, ponto_vencer):
    venceu = 0

    if vez == 1:
        pontuacao_total1 += pontuacao_partida
        if pontuacao_total1 >= ponto_vencer:
            ganhou_sound.play()
            venceu = 1
        vez = 2
    else:
        pontuacao_total2 += pontuacao_partida
        if pontuacao_total2 >= ponto_vencer:
            ganhou_sound.play()
            venceu = 2
        vez = 1
    
    pontuacao_partida = 0
    perdeu = False

    return vez
    return pontuacao_partida
    return pontuacao_total1
    return pontuacao_total2
    return venceu
    return perdeu

#Loop principal
while game and venceu == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN: 
            pos = pygame.mouse.get_pos()

            if ret_verde.collidepoint(pos): #Verifica de o usuario apertou o botão verde (girou o dado)
                n, pontuacao_partida, perdeu = rolagem (
                    window,
                    lista_dados,
                    WIDTH,
                    HEIGHT,
                    pontuacao_partida
                )
                
            if ret_vermelho.collidepoint(pos) or perdeu: #Verifica de o usuario apertou o botão vermelho (terminou sua jogada)
                vez, pontuacao_partida, pontuacao_total1, pontuacao_total2, vencedor_rodada, perdeu = fim_vez (
                    vez,
                    pontuacao_partida,
                    pontuacao_total1,
                    pontuacao_total2,
                    ponto_vencer
                )

                if vencedor_rodada != 0:
                    venceu = vencedor_rodada
        
    #Gera saídas
    window.fill((0, 0, 0)) #Preenche com a cor branca
    window.blit(fundo, (0, 0)) #Coloca tela de fundo

    #Gerando imagens dos dados, dependendo que qual for sorteado
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

    #Texto da pontuação total do jogador 1
    total1 = font_pontuacao.render('P1: '"{:03d}".format(pontuacao_total1), True, (244, 244, 244))
    text_rect = total1.get_rect()
    text_rect.midtop = (WIDTH //4, 20)
    window.blit(total1, text_rect)

    #Texto da pontuação total do jogador 2
    total2 = font_pontuacao.render('P2: '"{:03d}".format(pontuacao_total2), True, (244, 244, 244))
    text_rect = total2.get_rect()
    text_rect.midtop = (WIDTH*3//4, 20)
    window.blit(total2, text_rect)

    #Texto da pontuação da partida
    partida = font_pontuacao.render('JOGADA: '"{:03d}".format(pontuacao_partida), True, (244, 244, 244))
    text_rect = partida.get_rect()
    text_rect.midtop = (WIDTH //2, 700)
    window.blit(partida, text_rect)

    #Definindo de qual jogador é a vez
    if vez == 1:
        vez1 = font_vezjogador.render('VEZ DO JOGADOR 1', True, (244, 244, 244))
        text_rect = vez1.get_rect()
        text_rect.midtop = (305, 130)
        window.blit(vez1, text_rect)
    elif vez == 2:
        vez2 = font_vezjogador.render('VEZ DO JOGADOR 2', True, (244, 244, 244))
        text_rect = vez2.get_rect()
        text_rect.midtop = (300, 130)
        window.blit(vez2, text_rect)
    
    #Desenhando botões de rodar e parar
    cor_verde = (0, 255, 0)
    window.blit(botaoverde, (50, 500))
    text_rect.midtop = (157, 578)

    cor_vermelha = (255, 0, 0)
    window.blit(botaovermelho, (WIDTH-280, 500))
    text_rect.midtop = (457, 578)

    #Atualiza estado do jogo
    pygame.display.update()

if venceu != 0:
    tela_final(window, WIDTH, HEIGHT, venceu) #Chamando tela final caso alguem tiver vencido

#Finalização
pygame.quit()