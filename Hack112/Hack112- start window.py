import pygame
import time
import random
import os
from classKelly.py import *

pygame.init()
 
display_width = 600 
display_height = 800

 
black = (0,0,0)
white = (255,255,255)
blue = (0,0,220)
green = (0,200,0)

bright_blue = (0,0,255)
bright_green = (0,235,0)
 
# block_color = (53,115,255)
 
car_width = 100
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Grow a KELLY')
clock = pygame.time.Clock()
 
kellyImg = pygame.image.load('/Users/nicolechu/Desktop/Stickfigure.png')
 
babyKelly = pygame.image.load('/Users/nicolechu/Desktop/baby1.png')
babyKelly = pygame.transform.scale(babyKelly, (display_width, 300))


# def things_dodged(count):
#     font = pygame.font.SysFont(None, 25)
#     text = font.render("Dodged: "+str(count), True, black)
#     gameDisplay.blit(text,(0,0))
#  
# def things(thingx, thingy, thingw, thingh, color):
#     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
# def car(x,y):
#     gameDisplay.blit(kellyImg,(x,y))
 
 
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
    
 
# def crash():
#     message_display('You Crashed')

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("grow a KELLY", largeText)
        TextRect.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(kellyImg,(350,290))

        button("GO!", 100,300,200,80, green,bright_green, game_kidKelly)
        button("Instructions", 100,440,200,80, blue,bright_blue, game_instruct)

        pygame.display.update()
        clock.tick(15)
    
    
def instruct_text(text, y, size):
    
    pygame.draw.circle(gameDisplay, black, [display_width//8,y], 5)
    
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    gameDisplay.blit(TextSurf, ((display_width//6),y-15))
    
    
def questions():
    pass
    
    
def game_instruct():
    instruct = True
 
    while instruct:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objects("INSTRUCTIONS", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.draw.line(gameDisplay, black, [50,(display_height/5)], [(display_width-50),(display_height/5)], 5)
    
        
        instruct_text("Choose a Week to study from", (display_height//3), 30)
        instruct_text("Answer the questions correctly", (display_height//2), 30)
        instruct_text("Watch Kelly grow!", (2*display_height//3), 30)
        button("Play!", (display_width//3),(4*display_height/5),200,80, green,bright_green, game_kidKelly)
        
        pygame.display.update()
        clock.tick(15)
        
       
       
        
def game_kidKelly():
    
    gameKid = True
 
    while gameKid:
        gameDisplay.fill(white)
        gameDisplay.blit(babyKelly,(0,0))
        
        pygame.draw.line(gameDisplay, black, [50,(display_height/2)], [(display_width-50),(display_height/2)], 5)
        
        
        
        pygame.display.update()
        clock.tick(10)
    
    
# def game_loop():
#     x = 450
#     y = 250
#  
#     x_change = 0
#     y_change = 0
#  
#     thing_startx = random.randrange(0, display_width)
#     thing_starty = -600
#     thing_speed = 4
#     thing_width = 100
#     thing_height = 100
#  
#     thingCount = 1
#  
#     dodged = 0
#  
#     gameExit = False
#  
#     while not gameExit:
#  
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#  
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change = -5
#                 if event.key == pygame.K_RIGHT:
#                     x_change = 5
#                 if event.key == pygame.K_UP:
#                     y_change = -5
#                 if event.key == pygame.K_DOWN:
#                     y_change = 5
#                     
# 
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0
#                 if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
#                     y_change = 0  
# 
#         x += x_change
#         y += y_change
#         gameDisplay.fill(white)
#  
#         things(thing_startx, thing_starty, thing_width, thing_height, block_color)
#  
#  
#         thing_starty += thing_speed
#         car(x,y)
#         things_dodged(dodged)
#  
#         if x > display_width - car_width or x < 0:
#             crash()
#  
#         if thing_starty > display_height:
#             thing_starty = 0 - thing_height
#             thing_startx = random.randrange(0,display_width)
#             dodged += 1
#             thing_speed += 1
#             thing_width += (dodged * 1.2)
#  
#         if y < thing_starty+thing_height:
#             print('y crossover')
#  
#             if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
#                 print('x crossover')
#                 crash()
#         
#         pygame.display.update()
#         clock.tick(60)
# 
#     


game_intro()
game_instruct()
game_kidKelly()
pygame.quit()
quit()