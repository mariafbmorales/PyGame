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