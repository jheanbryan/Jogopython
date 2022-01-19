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

relogio = pygame.time.Clock()
pygame.display.set_caption('Snake') #Nome do jogo
fundo = pygame.display.set_mode((largura, altura)) #definindo largura e altura da tela

def cobra(pos_x_cobra, pos_y_cobra):
    pygame.draw.rect(fundo, preto, [pos_x_cobra, pos_y_cobra, tamanho, tamanho]) #desenhar o quadrado (serpente)
    
def maca(pos_x_maca, pos_y_maca):
        pygame.draw.rect(fundo, vermelho, [pos_x_maca, pos_y_maca, tamanho, tamanho]) #desenhar o quadrado (serpente)
    
def jogo():
    #Cobra
    pos_x_cobra = randint(0, (largura - tamanho) /10) *10 #posição x
    pos_y_cobra = randint(0, (altura - tamanho) /10) *10 #posição y
    
    #Maça
    pos_x_maca = randint(0, (largura - tamanho) /10) *10 #posição x
    pos_y_maca = randint(0, (altura - tamanho) /10) *10 #posição y
    
    velocidade_x = 0
    velocidade_y = 0
    sair = True
    while sair:
        for event in pygame.event.get(): #Enquanto acontecer eventos, entra no loop
            if event.type == pygame.QUIT: #Se apertar no [X] que fecha o jogo
                sair = False
            #Eventos para quando andar para qualquer direção
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho: #Se andar pra esquerda
                    velocidade_y = 0
                    velocidade_x = -tamanho   
                if event.key == pygame.K_RIGHT and velocidade_x != tamanho: #Se andar pra direita
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho: #Se andar pra cima
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != tamanho: #Se andar pra baixo
                    velocidade_x = 0
                    velocidade_y = tamanho
                    
            print(event)  #printar no prompt o que ta acontecendo
        fundo.fill(branco) #cor de fundo      
        pos_x_cobra += velocidade_x #andar no eixo x
        pos_y_cobra += velocidade_y #andar no eixo y
        cobra(pos_x_cobra, pos_y_cobra)
        maca(pos_x_maca, pos_y_maca)
        pygame.display.update() #recarregar a janela
        relogio.tick(10)

        #Eventos para caso a serpente chegar na borda da tela
        if pos_x_cobra >= largura:
            pos_x_cobra = 1 #game over
        if pos_x_cobra < 1:
            pos_x_cobra = 639 #game over
        if pos_y_cobra >= altura:
            pos_y_cobra = 1 #game over
        if pos_y_cobra < 1:
            pos_y_cobra = 479 #game over
            
        #pygameif pos_x == x_maca and pos_y == y_maca: #Se a serpente comer a maça
            #print("pegou a maca")
            #desenhar o quadrado (serpente)
        #     tamanho = tamanho + 5 #Serpente ganha tamanho
            
            
    #pygame.quit()
    #quit()
jogo()