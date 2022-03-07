import pygame

#create display window
SCREEN_HEIGHT = 450
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((1000, 600))

#button class
class Button():
    def __init__(self, x, y, image, scale):
        self.animado = []
        self.animado = image
        self.image = self.animado[0]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return

    def click(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        self.image = pygame.transform.scale(self.animado[0],
                                            (int(self.width * self.scale),
                                             int(self.height * self.scale)))
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(self.animado[1],
                                                (int(self.width * self.scale),
                                                 int(self.height * self.scale)))
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
        res = self.clicked
        self.clicked = False
        return res




BG = pygame.image.load('images/background.jpg').convert_alpha()
BG = pygame.transform.scale(BG,
                            (int(BG.get_width() * 0.8),
                             int(BG.get_height() * 0.8)))
pygame.display.set_caption('menu')

#load button images
track_img = []
track_img.append(pygame.image.load('images/joystick_ed.png').convert_alpha())
track_img.append(pygame.image.load('images/joystick_ed2.png').convert_alpha())
way_img = []
way_img.append(pygame.image.load('images/waypoints.png').convert_alpha())
way_img.append(pygame.image.load('images/waypoints2.png').convert_alpha())
menu_img = []
menu_img.append(pygame.image.load('images/menu_ed.png').convert_alpha())
menu_img.append(pygame.image.load('images/menu_ed.png').convert_alpha())
instru_img = []
instru_img.append(pygame.image.load('images/instru.png').convert_alpha())
instru_img.append(pygame.image.load('images/instru.png').convert_alpha())

#create button instances
track_button = Button(100, 150, track_img, 0.2)
way_button = Button(500, 150, way_img, 0.2)
menu_button = Button(800, 530, menu_img, 0.05)
instru_button = Button(250, 180, instru_img, 1)

clock_menu = pygame.time.Clock()


res = 0
def menu():
    global res, screen
    if res != 0:
        res = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while res == 0:
        clock_menu.tick(20)
        screen.blit(BG, (0, 0))
        track_button.draw()
        way_button.draw()
        if track_button.click():
            res = 2
            screen = pygame.display.set_mode((1000, 600))
        if way_button.click():
            res = 1
            screen = pygame.display.set_mode((1000, 600))
        pygame.display.update()
        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                pygame.quit()
    return res

