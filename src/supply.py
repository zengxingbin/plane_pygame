#-*- coding:utf-8 -*-
import pygame
class Supply(object):
    def __init__(self,screen,x,y,image,supplyName):
        self.screen = screen
        self.supply = pygame.image.load(image);
        self.x = x
        self.y = y
        self.supplyName = supplyName
        self.isObtained = False
    def display(self):
        self.screen.blit(self.supply,(self.x,self.y))
    def move(self):
        self.y += 1
    def judge(self):
        return self.y > 650    