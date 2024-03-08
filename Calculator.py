
import sys
import pygame

class Calculator:
    def __init__(self):
        self.dimensions = (608,889)
        pygame.init()
        pygame.display.set_caption('Calculator')
        self.screen = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('cal/1.png')
        self.img = pygame.transform.scale(self.img, self.dimensions)
        # self.buttons = []
    
    def run(self):
        while True:
            self.screen.blit(self.img,(0,0))

            # for button in self.buttons:
            #     self.screen.blit(button.img,button.cord)
            self.screen.blit(pygame.image.load('cal/2.png'),(195,683))
            self.screen.blit(pygame.image.load('cal/3.png'),(50,160))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60)

# class Button:
#     def __init__(self, imgPath, cord, value, screen):
#         self.img = pygame.image.load(imgPath)
#         self.img = pygame.transform.scale(self.img, (50,50))
#         self.cord = cord
#         self.value = value 
#         self.screen = screen 
    
    
#     def run(self):
#         while True:
#             self.screen.blit(self.img,self.cord)


calc = Calculator()
calc.run()

# button0 = Button('Sprites/calculator_sprites/0.png', (100,100), 0, calc.screen)
# calc.buttons.append(button0)
# button1 = Button('Sprites/calculator_sprites/1.png', (150,150), 1, calc.screen)
# calc.buttons.append(button1)