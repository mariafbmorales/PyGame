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

#Inicia estruturade dados
game = True

#Loop principal
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #Gera saídas
    window.fill((255, 204, 229)) #Preenche com a cor rosa 

    #Atualiza estado do jogo
    pygame.display.update()

#Finalização
pygame.quit()