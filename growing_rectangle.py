import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill('black')
pygame.display.update()

class Grow_Rectangle():
    
    def __init__(self,color, pos, dimensions):
        self.color = color
        self.pos = pos
        self.dimensions = dimensions
        self.surface = screen

    def draw(self):
        self.draw.rect = pygame.draw.rect(self.surface,self.color, self.pos, self.dimensions)

    def grow(self,dimensions):
        self.dimensions = self.dimensions+dimensions
        self.draw_rect = pygame.draw.rect(self.surface,self.color, self.pos, self.dimensions)

blue_rect = Grow_Rectangle('light blue',(300,300), (100,50))

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill('black')
            blue_rect.draw() 
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill('black')
            blue_rect.grow((40,40)) 
            pygame.display.update()
