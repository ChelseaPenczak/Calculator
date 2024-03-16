
import sys
import pygame
clock=pygame.time.Clock()
pygame.init()

# class Calculator:
#     #this function is called every time we make a new calculator object
#     def __init__(self): 
        #making the display 
        # self.dimensions = (400,600)
        # pygame.init()
        # pygame.display.set_caption('Calculator')

        # self.screen = pygame.display.set_mode(self.dimensions)
        # self.clock = pygame.time.Clock()
        # self.img = pygame.image.load('Sprites/Cal.png')
        # self.img = pygame.transform.scale(self.img, self.dimensions)

        # #setting up text display 
        # pygame.font.init()
        # font = pygame.font.SysFont('chalkboard se', 30)
        # self.text_surface = font.render(str(999), True, (89,82,75))
    
    # def run(self):
    #     while True:
            #self.screen.blit((255,255,255))
            # self.screen.blit(self.img,(0,0))
            # # for button in self.buttons:
            # #     self.screen.blit(button.img,button.cord)
            # self.screen.blit(pygame.image.load('Sprites/1_trans.png'),(0,10))
            # self.screen.blit(pygame.image.load('Sprites/2_trans.png'),(0,10))
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         sys.exit()
            #display text
            #self.screen.blit(self.text_surface,(280,120))
            #pygame.display.update()
            # self.clock.tick(60)



# Create a surface for the button
button_surface = pygame.Surface((150, 50))

screen = pygame.display.set_mode((400,600))


# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(125, 125, 150, 50)  # Adjust the position as needed

# Start the main loop
while True:
    # Set the frame rate
    clock.tick(60)
    # Get events from the event queue
    for event in pygame.event.get():
    # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            pygame.quit()
            sys.exit()

    # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # Call the on_mouse_button_down() function
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                click_sound = pygame.mixer.Sound('Sprites/click-button-140881.mp3')
                click_sound.play()
                print("Button clicked!")

    # Check if the mouse is over the button. This will create the button hover effect
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (200, 255, 200), (1, 1, 148, 48))
        
    else:
        pygame.draw.rect(button_surface, (230, 255, 230), (1, 1, 148, 48))
        pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

    # Draw the button on the screen
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    # Update the game state
    pygame.display.update()


    # class Button():
    #     def __init__(self, top_rect,pos):
    #         #self.image = pygame.transform.scale(image, (int(width), int(height)))
    #         #self.rect = self.image.get_rect()
    #         print('init button')
    #         self.top_rect = pygame.Rect(pos,(56,56))
    #         self.clock = pygame.time.Clock()
        
    #     def run(self):
    #         while True:
    #             pos = pygame.mouse.get_pos()
    #             top_rect = self.top_rect.copy()
    #             print('string loop')
    #             if top_rect.collidepoint(pos):
    #                 if pygame.mouse.get_pressed()[0]:
    #                     print('hello')
    #             self.clock.tick(60)
#  Calculator().run()