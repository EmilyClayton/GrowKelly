import pygame
import time
import random
import os
from classKelly import *
from classWeeks import *

pygame.init()
screen = pygame.display.set_mode((600, 800))
 
display_width = 600 
display_height = 800

 
black = (0,0,0)
white = (255,255,255)
blue = (0,0,220)
green = (0,200,0)

bright_blue = (0,0,255)
bright_green = (0,235,0)

 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Grow a KELLY')
clock = pygame.time.Clock()
 
kellyImg = pygame.image.load('/Users/nicolechu/Desktop/flower.png')
kellyImg = pygame.transform.scale(kellyImg, (290, 400))

# some code taken from https://pythonprogramming.net/pygame-python-3-part-1-intro/ and the other pages in the tutorial
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 

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
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("grow a KELLY", largeText)
        TextRect.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(kellyImg,(300,200))

        button("Play!", 70,300,200,80, green,bright_green, game_babyKelly)

        button("Instructions", 70,440,200,80, blue,bright_blue, game_instruct)

        pygame.display.update()
        clock.tick(15)
    
    
def instruct_text(text, y, size):
    
    pygame.draw.circle(gameDisplay, black, [display_width//8,y], 5)
    
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText)
    gameDisplay.blit(TextSurf, ((display_width//6),y-15))
    
    
def game_instruct():
    
    gameIntruct = True
 
    while gameIntruct:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIntruct = False
    
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objects("INSTRUCTIONS", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.draw.line(gameDisplay, black, [50,(display_height/5)], [(display_width-50),(display_height/5)], 5)
        

    
        instruct_text("Answer the questions correctly", (display_height//3), 30)
        instruct_text("Watch Kelly grow!", (display_height//2), 30)
        instruct_text("Don't get them wrong...", (2*display_height//3), 30)
        button("Play!", (display_width//3),(4*display_height/5),200,80, green,bright_green, game_babyKelly)
        
        pygame.display.update()
        clock.tick(15)
        
    

def game_wrong():
    
    gameWrong = True
 
    while gameWrong:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameWrong = False
    
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",90)
        TextSurf, TextRect = text_objects("WRONG ANSWER", largeText)
        TextRect.center = ((display_width/2),(display_height/8))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Go back", (display_width//3),(display_height/2),200,80, green,bright_green, game_babyKelly)
        button("back to start", (display_width//3),(4*display_height/5),200,70, green,bright_green, game_intro)
        
        
        pygame.display.update()
        clock.tick(10)
        
def nextQuestion():
    questionNum += 1

def game_babyKelly():
    
    gamebaby = True

    my_sprite = BabyKelly()
    my_group = pygame.sprite.Group(my_sprite)
    
    while gamebaby:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamebaby = False
        
        gameDisplay.fill(white)
        
        smallText = pygame.font.SysFont("comicsansms",40)
        textSurf, textRect = text_objects("Which is an integer?", smallText)
        textRect.center = ((display_width//2), (display_height//2) )
        gameDisplay.blit(textSurf, textRect)
        
        button("2", 50,(6*display_height/10),(display_width-100),70, blue,bright_blue, game_kidKelly)
        button("5.7", 50,(7*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        button("hello", 50,(8*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        
        button("back to start", (display_width//3),(9*display_height/10),200,70, green,bright_green, game_intro)
        
        my_group.update()
        my_group.draw(screen)
        
        pygame.display.update()
        clock.tick(10)
        
    

def game_kidKelly():
    
    gamekid = True
 
    my_sprite = KidKelly()
    my_group = pygame.sprite.Group(my_sprite)
    
    while gamekid:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gamekid = False
        
        gameDisplay.fill(white)
        
        
        smallText = pygame.font.SysFont("comicsansms",40)
        textSurf, textRect = text_objects("What is the type of True?", smallText)
        textRect.center = ((display_width//2), (display_height//2) )
        gameDisplay.blit(textSurf, textRect)
        
        button("string", 50,(6*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        button("boolean", 50,(7*display_height/10),(display_width-100),70, blue,bright_blue, game_teenKelly)
        button("integer", 50,(8*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        
        button("back to start", (display_width//3),(9*display_height/10),200,70, green,bright_green, game_intro)
        
        my_group.update()
        my_group.draw(screen)
        
        pygame.display.update()
        clock.tick(10)
  

def game_teenKelly():
    
    gameteen = True
    my_sprite = TeenKelly()
    my_group = pygame.sprite.Group(my_sprite)
    
    while gameteen:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameteen = False
        
        gameDisplay.fill(white)
        
        smallText = pygame.font.SysFont("comicsansms",40)
        textSurf, textRect = text_objects("What is 3 % 10?", smallText)
        textRect.center = ((display_width//2), (display_height//2) )
        gameDisplay.blit(textSurf, textRect)
        
        button("idk", 50,(6*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        button("3", 50,(7*display_height/10),(display_width-100),70, blue,bright_blue, game_adultKelly)
        button("7", 50,(8*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        
        button("back to start", (display_width//3),(9*display_height/10),200,70, green,bright_green, game_intro)
        
        my_group.update()
        my_group.draw(screen)
        
        pygame.display.update()
        clock.tick(10)
        


def game_adultKelly():
    
    gameadult = True
     
    my_sprite = AdultKelly()
    my_group = pygame.sprite.Group(my_sprite)
    
    while gameadult:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameadult = False
        
        gameDisplay.fill(white)
        
        
        smallText = pygame.font.SysFont("comicsansms",40)
        textSurf, textRect = text_objects("What does MVC stand for?", smallText)
        textRect.center = ((display_width//2), (display_height-390) )
        gameDisplay.blit(textSurf, textRect)
        
        button("Model, View, Controller", 50,(6*display_height/10),(display_width-100),70, blue,bright_blue, game_profRivers)
        button("42", 50,(7*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        button("Make Vivacious Code", 50,(8*display_height/10),(display_width-100),70, blue,bright_blue, game_wrong)
        
        button("back to start", (display_width//3),(9*display_height/10),200,70, green,bright_green, game_intro)
        
        
        my_group.update()
        my_group.draw(screen)
        
        
        pygame.display.update()
        clock.tick(10)
        

def game_profRivers():
    
    gameprof = True
    my_sprite = ProfessorRivers()
    my_group = pygame.sprite.Group(my_sprite)
    
    while gameprof:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameprof = False
        
        gameDisplay.fill(white)
        
        
        largeText = pygame.font.SysFont("comicsansms",85)
        TextSurf, TextRect = text_objects("you passed 15-112 !", largeText)
        TextRect.center = ((display_width/2),(2*display_height//3))
        gameDisplay.blit(TextSurf, TextRect)
        
        
        button("back to start", (display_width//3),(9*display_height/10),200,70, green,bright_green, game_intro)
        
        my_group.update()
        my_group.draw(screen)
        
        
        pygame.display.update()
        clock.tick(10)
        
        
def main():
    while True:
        
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


        game_intro()
if __name__ == '__main__':
    main() 
    
    