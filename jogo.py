#Importa e inicia pacotes
import pygame 
import random
pygame.init() 

#Gera tela principal
WIDTH = 600
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('No 1, rodou')

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