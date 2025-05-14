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
DADO_WIDTH = 70
DADO_HEIGHT = 70
dado1_img = pygame.image.load('assets/img/dado1.jpeg').convert_alpha()
dado1_img_small = pygame.transform.scale(dado1_img, (DADO_WIDTH, DADO_HEIGHT))
dado2_img = pygame.image.load('assets/img/dado2.jpeg').convert_alpha()
dado2_img_small = pygame.transform.scale(dado2_img, (DADO_WIDTH, DADO_HEIGHT))
dado3_img = pygame.image.load('assets/img/dado3.jpeg').convert_alpha()
dado3_img_small = pygame.transform.scale(dado3_img, (DADO_WIDTH, DADO_HEIGHT))
dado4_img = pygame.image.load('assets/img/dado4.jpeg').convert_alpha()
dado4_img_small = pygame.transform.scale(dado4_img, (DADO_WIDTH, DADO_HEIGHT))
dado5_img = pygame.image.load('assets/img/dado5.jpeg').convert_alpha()
dado5_img_small = pygame.transform.scale(dado5_img, (DADO_WIDTH, DADO_HEIGHT))
dado6_img = pygame.image.load('assets/img/dado6.jpeg').convert_alpha()
dado6_img_small = pygame.transform.scale(dado6_img, (DADO_WIDTH, DADO_HEIGHT))
lista_dados = [0,dado1_img_small, dado2_img_small, dado3_img_small, dado4_img_small, dado5_img_small, dado6_img_small]

#Inicia estrutura de dados
game = True

pontuacao_total = 0

#Loop principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        #Verifica se o usuario apertou o espaço (girou o dado)
        pontuacao_partida = 0
        if event.type == pygame.KEYUP:
            n = random.randint(1, 6)
            dado_sorteado = lista_dados[n]
            if dado_sorteado == 2:
                pontuacao_partida += 2
            elif dado_sorteado == 3:
                pontuacao_partida += 3
            elif dado_sorteado == 4:
                pontuacao_partida += 4
            elif dado_sorteado == 5:
                pontuacao_partida += 5
            elif dado_sorteado == 6:
                pontuacao_partida += 6
            elif dado_sorteado == 1:
                pontuacao_partida = 0

        pontuacao_total += pontuacao_partida #Adicioa a pontuação daquela partida na pontuação total
                
    #Gera saídas
    window.fill((255, 204, 229)) #Preenche com a cor rosa 

    #Atualiza estado do jogo
    pygame.display.update()

#Finalização
pygame.quit()