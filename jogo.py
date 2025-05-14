#Importa e inicia pacotes
import pygame 
import random
pygame.init() 

#Gera tela principal
WIDTH = 600
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('No 1, rodou')

#Inicia assets
DADO_WIDTH = 100
DADO_HEIGHT = 100
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

#Inicia estrutura de dados
game = True

pontuacao_total1 = 0
pontuacao_total2 = 0
pontuacao_partida = 0
venceu = 0
perdeu = False
vez = 1
n = 0
#Loop principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYUP: #Verifica se o usuario apertou keyup (girou o dado)
            if event.key == pygame.K_UP:
                n = random.randint(1, 6)
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
            if event.key == pygame.K_DOWN or perdeu:
                perdeu = False
                if vez == 1:
                    pontuacao_total1 += pontuacao_partida #Adiciona a pontuação daquela partida na pontuação total
                    if pontuacao_total1 >= 100:
                        venceu = 1
                    vez = 2
                else:
                    pontuacao_total2 += pontuacao_partida #Adiciona a pontuação daquela partida na pontuação total
                    if pontuacao_total2 >= 100:
                        venceu = 2
                    vez = 1
                pontuacao_partida = 0
                print("Pont total 1:",pontuacao_total1)
                print("Pont total 2:",pontuacao_total2)
                print("Vez do jogador ",vez)

        
    #Gera saídas
    window.fill((255, 204, 229)) #Preenche com a cor rosa

    #Gerando imagens dos dados
    if n == 1:
        window.blit(dado1_img_small, (300, 375))
    elif n == 2:
        window.blit(dado2_img_small, (300, 375))
    elif n ==3:
        window.blit(dado3_img_small, (300, 375))
    elif n == 4:
        window.blit(dado4_img_small, (300, 375))
    elif n == 5:
        window.blit(dado5_img_small, (300, 375))
    elif n == 6:
        window.blit(dado6_img_small, (300, 375))
    #Gerando o texto 
    font = pygame.font.SysFont('georgia', 25)
    total1 = font.render('TOTAL 1: ', True, (244, 244, 244))
    text_rect = total1.get_rect()
    text_rect.midtop = (WIDTH //5, 15)
    
    window.blit(total1, text_rect)

    #Atualiza estado do jogo
    pygame.display.update()

#Finalização
pygame.quit()