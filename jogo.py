from assets import *
from funcoes import *


#Definindo posição e tamanho dos botões da tela principal
ret_verde = pygame.Rect(60, 550, 210, 70) 
ret_vermelho = pygame.Rect(WIDTH-250, 550, 180, 70)

#Inicia estrutura de dados
game = True

pontuacao_total1 = 0
pontuacao_total2 = 0
pontuacao_partida = 0
venceu = 0
n = 0
vez = 1
perdeu = False

tela_inicial(window, WIDTH, HEIGHT) #Chamando tela inicial antes do inicio do jogo
tela_instrucoes(window, WIDTH, HEIGHT)  # Chama tela de intruções sobre o jogo

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
                    perdeu_sound.play() #colocando som para tocas quando cai o dado 1
                    pontuacao_partida = 0
                    perdeu = True
                
            if ret_vermelho.collidepoint(pos) or perdeu: #Verifica de o usuario apertou o botão vermelho (terminou sua jogada)
                perdeu = False
                if vez == 1:
                    pontuacao_total1 += pontuacao_partida #Adiciona a pontuação daquela partida na pontuação total do jogador 1
                    if pontuacao_total1 >= 100:
                        ganhou_sound.play()
                        venceu = 1
                    vez = 2
                else:
                    pontuacao_total2 += pontuacao_partida #Adiciona a pontuação daquela partida na pontuação total do jogador 2
                    if pontuacao_total2 >= 100:
                        ganhou_sound.play()
                        venceu = 2
                    vez = 1
                pontuacao_partida = 0
        
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

    #Colocando de qual jogador é a vez
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
    tela_final(window, WIDTH, HEIGHT, venceu)

#Finalização
pygame.quit()