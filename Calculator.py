
import sys
import pygame

class Calculator:
    def __init__(self):
        self.dimensions = (400,600)
        pygame.init()
        pygame.display.set_caption('Calculator')
        self.screen = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('Sprites/Calculator_sprites/Calculator.png')
        self.img = pygame.transform.scale(self.img, self.dimensions)
        # self.buttons = []
    
    def run(self):
        while True:
            self.screen.blit(self.img,(0,0))

            # for button in self.buttons:
            #     self.screen.blit(button.img,button.cord)
            self.screen.blit(pygame.image.load('Sprites/Calculator_sprites/1_trans.png'),(0,10))
            self.screen.blit(pygame.image.load('Sprites/Calculator_sprites/2_trans.png'),(0,10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)
Calculator().run()