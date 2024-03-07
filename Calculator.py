
import sys
import pygame
class Calculator:
    def __init__(self):
        self.dimensions = (649/2,880/2)
        pygame.init()
        pygame.display.set_caption('Calculator')
        self.screen = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('Sprites/FullCal.png')
        self.img = pygame.transform.scale(self.img, self.dimensions)
    def run(self):
        while True:
            self.screen.blit(self.img,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

Calculator().run()