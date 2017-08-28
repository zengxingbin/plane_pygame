#-*- coding:utf-8 -*-
#!E:\My software\python3.6
import pygame
from bullet import Bullet
class EnemyBullet(Bullet):
    '''�ӵ���'''
    def __init__(self,x,y,screen):
        self.bullet = pygame.image.load("./images/bullet1.png");#5 * 11
        self.x = x
        self.y = y
        self.strength = 10
        self.screen = screen
    def setBullet(self,bullet):
        self.bullet = bullet
    def getBullet(self):
        return self.bullet
    def setX(self,x):
        self.x = x
    def getX(self):
        return self.x
    def setY(self,y):
        self.y = y
    def getY(self):
        return self.y
    def setStrength(self,strength):
        self.strength = strength
    def getStrength(self):
        return self.strength
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))
    def move(self):
        self.y += 3
    def judge(self):
        return self.y > 650