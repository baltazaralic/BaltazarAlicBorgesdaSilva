import pygame
from pygame.locals import *
from fisica import *
from interface import *
import numpy as np


pygame.init()
screen = pygame.display.set_mode((1000, 600)) #define o tamanho da tela
pygame.display.set_caption('Drone') #define o nome do programa
pygame.display.get_window_size()
background = pygame.image.load(f'images/kanoha_BG_ed.jpg') #armazena a imagem de fundo
background = pygame.transform.scale(background, (int(background.get_width() * 1.1), int(background.get_height() * 1.1)))
FPS = 100
comandar = 0

# controle dos recursos na tela
menu_open = 1
instru_open = 1

#inicializa as variaveis de movimento do drone
esquerda = False
direita = False
cima = False
baixo = False
dt = 1/FPS
#transformação de metros para pixels
rx = 1000/7

#controle de tempo do jogo
clock = pygame.time.Clock()


class Drone(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        #variaveis de posição
        self.x = x
        self.y = y
        self.scale = scale
        self.angle = 0
        self.pos = []
        #variaveis de animação
        self.flip = 0
        self.passo = 1
        self.animado = []
        self.animado.append(pygame.image.load(f'images/drone.png').convert_alpha())
        self.animado.append(pygame.image.load(f'images/drone1.png').convert_alpha())
        self.animado.append(pygame.image.load(f'images/drone2.png').convert_alpha())
        img = self.animado[0]
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        #variaveis de posição da imagem
        self.rect = img.get_rect()
        self.center = (x, y)
        self.size = self.image.get_size()


    def update(self):
        #troca as imagens do drone para a animação das hélices
        self.flip += self.passo
        if self.flip >= len(self.animado)-1 or self.flip == 0:
            self.passo *= -1
        self.image = self.animado[int(self.flip)]
        self.image = pygame.transform.scale(self.image,
                                            (int(self.image.get_width() * self.scale),
                                             int(self.image.get_height() * self.scale)))
        #rotação do drone na tela
        self.image = pygame.transform.rotate(self.image, self.angle)
        # transformação para fazer o drone girar em relação ao centro
        size = self.image.get_size()
        self.rect.x = self.x - (size[0] - self.size[0])/2
        self.rect.y = self.y - (size[1] - self.size[1])/2


    def move(self, esquerda, direita, cima, baixo, comandar):

        self.pos, angle = movimenta(esquerda, direita, cima, baixo, comandar)
        self.angle = angle * 180 / np.pi

        #Transformação linear da posição
        self.x = rx*self.pos[0]        #############################
        self.y = rx*self.pos[1] - 30        ########################

    def draw(self):
        screen.blit(self.image, self.rect)


drone = Drone(0, 500, 0.3)

i = 0
def drone_f():
    global i, comandar, cima, baixo, esquerda, direita, menu_open

    #atualização do drone na tela
    #modificação da frequencia de apresentação na tela
    i += 1
    if i >= 3:
        drone.update()
        drone.draw()
        menu_button.draw()
        if menu_button.click():
            menu_open = 1
        pygame.display.update()
        pygame.display.flip()
        i = 0



    #coletar dados dos perifericos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        #controlador de posição pelo teclado

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                esquerda = True
            if event.key == pygame.K_d:
                direita = True
            if event.key == pygame.K_w:
                cima = True
            if event.key == pygame.K_s:
                baixo = True
            if comandar and not menu_open:
                if event.key == pygame.K_SPACE:
                    gravar(True)
                if event.key == pygame.K_r:
                    gravar(False)



            # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                esquerda = False
            if event.key == pygame.K_d:
                direita = False
            if event.key == pygame.K_w:
                cima = False
            if event.key == pygame.K_s:
                baixo = False

    drone.move(esquerda, direita, cima, baixo, comandar)

#interface grafica
def instru_f():
    global i, instru_open

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            instru_open = 0

    #atualização do drone na tela
    i += 1
    if i >= 3:
        instru_button.draw()
        pygame.display.update()
        pygame.display.flip()
        i = 0
        if pygame.mouse.get_pressed()[0]:
            instru_open = 0




while True:
    #taxa de clock
    clock.tick(FPS)

    if menu_open:
        menu_res = menu()
        if menu_res != 0:
            menu_open = 0
            comandar = menu_res - 1
            if comandar:
                pygame.time.wait(500)
                instru_open = 1

    else:

        # atualiza o background na tela
        screen.blit(background, (0, 0))

        if comandar and instru_open:
            instru_f()  #abre as intruções
        else:
            drone_f()   #mostra o drone na tela
