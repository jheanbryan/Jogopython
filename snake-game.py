import pygame
from random import randint

branco = (255,255,255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

try: 
    pygame.init()
except:
    print('Deu algo de errado.')
    
largura = 640
altura = 480
tamanho = 10
pos_x = randint(0, (largura - tamanho) /10) *10
pos_y = randint(0, (altura - tamanho) /10) *10
x_maca = randint(0, (largura - tamanho) /10) *10
y_maca = randint(0, (altura - tamanho) /10) *10
velocidade_x = 0
velocidade_y = 0
relogio = pygame.time.Clock()
pygame.display.set_caption('Snake') #Nome do jogo
fundo = pygame.display.set_mode((largura, altura)) #definindo largura e altura da tela

sair = True
while sair:
    for event in pygame.event.get(): #Enquanto acontecer eventos, entra no loop
        if event.type == pygame.QUIT: #Se apertar no [X] que fecha o jogo
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #Se andar pra esquerda
                velocidade_y = 0
                velocidade_x = -tamanho
                
            if event.key == pygame.K_RIGHT: #Se andar pra direita
                velocidade_y = 0
                velocidade_x = tamanho
                
            if event.key == pygame.K_UP: #Se andar pra cima
                velocidade_x = 0
                velocidade_y = -tamanho
                
            if event.key == pygame.K_DOWN: #Se andar pra baixo
                velocidade_x = 0
                velocidade_y = tamanho
                
        print(event)  #printar no prompt o que ta acontecendo
    fundo.fill(branco) #cor de fundo
    serpente = pygame.draw.rect(fundo, azul, [pos_x, pos_y, tamanho, tamanho]) #desenhar o quadrado (serpente)
    maca = pygame.draw.circle(fundo, vermelho, (x_maca, y_maca), 5, 5) #desenhar o circulo (maçã)
    
    pos_x += velocidade_x #andar no eixo x
    pos_y += velocidade_y #andar no eixo y
    pygame.display.update() #recarregar a janela
    relogio.tick(10)
    #pygame.draw.circle(fundo, azul, [pos_x, pos_y, tamanho, tamanho])
    
    if pos_x == x_maca and pos_y == y_maca: #Se a serpente comer a maça
        print("pegou a maca")
        tamanho = tamanho + 5 #Serpente ganha tamanho
    
        
        
#pygame.quit()
#quit()