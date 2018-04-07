import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class BabyKelly(pygame.sprite.Sprite):
    def __init__(self):
        super(BabyKelly, self).__init__()
        self.images = []
        numKelly = 12
        for number in range(1,numKelly):
            img = load_image('baby%s.png' %str(number))
            img = pygame.transform.scale(img, (500, 300))
            self.images.append(img)
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 20, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        pygame.time.delay(90)
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
    def levelUp():
        self.kelly = KidKelly()
        
class KidKelly(pygame.sprite.Sprite):
    def __init__(self):
        self.heath = 15
        
        super(KidKelly, self).__init__()
        self.images = []
        numKelly = 13
        for number in range(1,numKelly):
            img = load_image('kid%s.png' %str(number))
            img = pygame.transform.scale(img, (230, 300))
            self.images.append(img)
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(180, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        pygame.time.delay(90)
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
    def levelUp():
        self.kelly = TeenKelly()
        
class TeenKelly(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 10
        super(TeenKelly, self).__init__()
        self.images = []
        numKelly = 14
        for number in range(1,numKelly):
            img = load_image('teen%s.png' %str(number))
            img = pygame.transform.scale(img, (620, 380))
            self.images.append(img)
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        pygame.time.delay(90)
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
    def levelUp():
        self.kelly = AdultKelly()
    
class AdultKelly(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 5
        
        super(AdultKelly, self).__init__()
        self.images = []
        numKelly = 14
        for number in range(1,numKelly):
            img = load_image('adult%s.png' %str(number))
            img = pygame.transform.scale(img, (350, 300))
            self.images.append(img)
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(120, 0, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        pygame.time.delay(90)
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
    def levelUp():
        self.kelly = ProfessorRivers()
    
class ProfessorRivers(pygame.sprite.Sprite):
    def __init__(self):
        super(ProfessorRivers, self).__init__()
        self.images = []
        numKelly = 7
        for number in range(1,numKelly):
            img = load_image('professor%s.png' %str(number))
            img = pygame.transform.scale(img, (600, 400))
            self.images.append(img)
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        pygame.time.delay(90)
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]