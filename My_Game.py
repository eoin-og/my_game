import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

car_width = 73
car_height = 82

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
class thing:
    def __init__(self, x, y, x_speed, y_speed, width, height, color):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.width = width
        self.height = height
        self.color = color

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def bounce(self):
        if self.x < 0 or self.x+self.width > display_width:
            self.x_speed = self.x_speed*-1
        if self.y<0 or self.y+self.height > display_height:
            self.y_speed = self.y_speed*-1

class car:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0
        self.image = image
        self.height = pygame.Surface.get_height(image)
        self.width = pygame.Surface.get_width(image)

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def hit_wall(self):
        if self.x > display_width - self.width or self.x < 0 or self.y > display_height - self.height or self.y < 0:
            crash()

def score_display(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def draw_things(things):
    for thing in things:
        pygame.draw.rect(gameDisplay, thing.color, [thing.x, thing.y, thing.width, thing.height])

def display_car(car):
    gameDisplay.blit(carImg,(car.x,car.y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def collision_test(my_car,things):
    for thing in things:
        if thing.x+thing.width > my_car.x and thing.x < my_car.x+my_car.width:
            if thing.y+thing.height > my_car.y and thing.y < my_car.y+my_car.height:
                print('yyy')
                return True
        

def crash():
    message_display('You Crashed')
    
def game_loop():
    #create objects
    my_car = car((display_width * 0.45),(display_height * 0.8), pygame.image.load('racecar.png'))
    thingy = thing(0,0,4,4,40,40,black)
    things = [thingy]

    #set-up counter
    ticks = 0
    thingCount = 1

    gameExit = False
    while not gameExit:

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    my_car.x_speed = -5
                if event.key == pygame.K_RIGHT:
                    my_car.x_speed =  5
                if event.key == pygame.K_UP:
                    my_car.y_speed = - 5
                if event.key == pygame.K_DOWN:
                    my_car.y_speed = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    my_car.x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    my_car.y_speed = 0
                    

        gameDisplay.fill(white)

        #display
        draw_things(things)
        score_display(len(things))

        #move cars
        my_car.move()
        my_car.hit_wall()
        display_car(my_car)

        #display boxes
        for thingo in things:
            thingo.move()
            thingo.bounce()

        #test for crash
        if(collision_test(my_car, things)):
            crash()
        
        pygame.display.update()
        clock.tick(60)
        ticks+=1

game_loop()
pygame.quit()
quit()
