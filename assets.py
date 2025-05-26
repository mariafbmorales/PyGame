#Importa e inicia pacotes
import pygame 
import random
import os
import time

pygame.init() 
pygame.mixer.init() #Inicializando o uso de sons

#Gera tela principal
WIDTH = 600
HEIGHT = 750
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('No 1, rodou')

#Adicionando os sons
perdeu_sound = pygame.mixer.Sound('assets/sounds/losetrumpet.mp3')
ganhou_sound = pygame.mixer.Sound('assets/sounds/Victory.wav')

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

botaoverde = pygame.image.load('assets/img/startsemfundo-removebg-preview.png').convert_alpha() 
botaoverde = pygame.transform.scale(botaoverde, (230, 200))
botaovermelho = pygame.image.load('assets/img/pararsemfundo-removebg-preview.png').convert_alpha() 
botaovermelho = pygame.transform.scale(botaovermelho, (230, 200))

fundo = pygame.image.load('assets/img/teladefundo.png').convert() #Imagem de fundo gerada pelo ChatGPT
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))

background_inicio = pygame.image.load('assets/img/fundoinicial.png').convert()
background_inicio = pygame.transform.scale(background_inicio, (WIDTH, HEIGHT))

logo = pygame.image.load('assets/img/logo.png').convert_alpha()
logo = pygame.transform.scale(logo, (475, HEIGHT/1.6))

botaoinicio = pygame.image.load('assets/img/Botão_inicio.png-removebg-preview.png').convert_alpha()
botaoinicio_img_small = pygame.transform.scale(botaoinicio, (250, 250))

#Definindo fonte e tamanho das letras que aparecem na de intruções
font_instrucoes = pygame.font.Font('assets/font/PressStart2P.ttf', 10)

botao_continuar = pygame.image.load('assets/img/botaocontinuar.png').convert_alpha()
botao_continuar = pygame.transform.scale(botao_continuar, (260, 95))

#Imagem do botao de sair
botao_sair = pygame.image.load('assets/img/botaosair-removebg-preview.png').convert_alpha()
botao_sair = pygame.transform.scale(botao_sair, (250, 120))

fundo_instrucoes = pygame.image.load('assets/img/fundoinstruções.png').convert_alpha()
fundo_instrucoes = pygame.transform.scale(fundo_instrucoes, (WIDTH, HEIGHT+40))