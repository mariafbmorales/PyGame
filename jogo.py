#Importa e inicia pacotes
import pygame 
pygame.init() 

#Gera tela principal
window = pygame.display.set_mode((600, 750))
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