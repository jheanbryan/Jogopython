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
font = pygame.font.SysFont(None, 25)

#Texto
def texto(msg, cor):
    texto_um = font.render(msg, True, cor)
    fundo.blit(texto_um, [(largura/2) -40, altura/2]) 
    
def cobra(cobraxy):
    for xy in cobraxy:
        pygame.draw.rect(fundo, branco, [xy[0], xy[1], tamanho, tamanho]) #desenhar o quadrado (serpente)
    
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
    cobraxy = []
    comprimento_cobra = 1
  
        
    sair = True
    fim_de_jogo = False
    while sair:
        while fim_de_jogo:
            fundo.fill(branco)   
            texto('Game Over. Pressione r para continuar', vermelho)
            pygame.display.update()             
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
                if event.key == pygame.K_r:
                    jogo()
                
                    
            print(event)  #printar no prompt o que ta acontecendo
        fundo.fill(preto) #cor de fundo      
        pos_x_cobra += velocidade_x #andar no eixo x
        pos_y_cobra += velocidade_y #andar no eixo y
        cobra_inicio = []
        cobra_inicio.append(pos_x_cobra)
        cobra_inicio.append(pos_y_cobra)
        cobraxy.append(cobra_inicio)
        
        if len(cobraxy) > comprimento_cobra:
            del cobraxy[0]
            
        cobra(cobraxy)
        maca(pos_x_maca, pos_y_maca)
        pygame.display.update() #recarregar a janela
        relogio.tick(15)
        
        if pos_x_cobra == pos_x_maca and pos_y_cobra == pos_y_maca: #Se a serpente comer a maça
            print("pegou a maca")
            comprimento_cobra+=10
            #Maça
            pos_x_maca = randint(0, (largura - tamanho) /10) *10 #posição x
            pos_y_maca = randint(0, (altura - tamanho) /10) *10 #posição y
            
         #Eventos para caso a serpente chegar na borda da tela
        if pos_x_cobra >= largura:
            print('game over')
            fim_de_jogo = True 
        if pos_x_cobra < 1:
            print('game over')
            fim_de_jogo = True
        if pos_y_cobra >= altura:
            print('game over')
            fim_de_jogo = True
        if pos_y_cobra < 1:
            print('game over')
            fim_de_jogo = True
            
        #Caso a cobra se morder
        if any(Bloco == cobra_inicio for Bloco in cobraxy[:-1]):
            print('game over')
            fim_de_jogo = True
        
              
            
            
    #pygame.quit()
    #quit()

jogo()