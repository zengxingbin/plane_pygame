#-*- coding:utf-8 -*-
#!E:\My software\python3.6
import pygame
import random
from bullet import Bullet
from random import randint
from enemybullet import EnemyBullet
from supply import Supply
class Enemy(object):
    def __init__(self,screen,blood,x=random.randint(0,423),y=-43):
        self.plane = pygame.image.load("./images/enemy1.png");#46 * 57
        #敌机随机出现的x坐标ֵ
        self.x = x#(0,434)
        self.y = y
        self.screen = screen
        self.blood = blood
        self.bulletList = []
        self.invalidBullet = []
        self.direction = randint(0,1)#0向左移动，1向右移动
        self.time = randint(1,4)#记录敌机左右移动的最大次数的范围
        self.count = 0#记录敌机左右移动了多少次
        self.downX = randint(0,423)#敌机应该向下移动的X坐标的位置为随机的
        #爆炸图片列表
        self.explodeImages = ['./images/enemy1_down4.png','./images/enemy1_down4.png','./images/enemy1_down3.png','./images/enemy1_down2.png','./images/enemy1_down1.png']
        #爆炸计数
        self.explodeCount = 0
        #补给
        self.supply = None 
        #敌机是否存活
        self.isAlive=True
    def display(self,enemy):
        self.screen.blit(self.plane,(self.x,self.y))
        if self.bulletList:
            for bullet in self.bulletList:
                if (bullet.x+5 > enemy.x+25 and bullet.x+5 < enemy.x+77) and (bullet.y+11 > enemy.y and bullet.y+11 < enemy.y+126):
                    enemy.blood -= bullet.strength
                    if enemy.blood <= 0:
                        enemy.isAlive = False
                        break
                    self.invalidBullet.append(bullet)
                elif (bullet.x > enemy.x+25 and bullet.x < enemy.x+77) and (bullet.y+11 > enemy.y and bullet.y+11 < enemy.y+126):
                    enemy.blood -= bullet.strength
                    if enemy.blood <= 0:
                        enemy.isAlive = False
                        break
                elif (bullet.x+5 > enemy.x+25 and bullet.x+5 < enemy.x+77) and (bullet.y > enemy.y and bullet.y < enemy.y+126):
                    enemy.blood -= bullet.strength
                    if enemy.blood <= 0:
                        enemy.isAlive = False
                        break
                elif (bullet.x > enemy.x+25 and bullet.x < enemy.x+77) and (bullet.y > enemy.y and bullet.y < enemy.y+126):
                    enemy.blood -= bullet.strength
                    if enemy.blood <= 0:
                        enemy.isAlive = False
                        break
                    self.invalidBullet.append(bullet)
                    self.invalidBullet.append(bullet)
            for bullet in self.bulletList:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    self.invalidBullet.append(bullet)
                    #self.bulletList.remove(bullet)

            if self.invalidBullet:
                for bullet in self.invalidBullet:
                    if self.bulletList.__contains__(bullet):
                        self.bulletList.remove(bullet)
            #清空失效子弹列表
            self.invalidBullet.clear()    
    def moveLeft(self,step):
        if (self.x - step) >= 0:         
            self.x -= step
        else:
            self.x = 0
    def moveRight(self,step):
        if (self.x + step) <= 434:
            self.x += step
        else:
            self.x = 434
    def moveUP(self,step):
        if(self.y - 10) >= 0:
            self.y -= step
        else:
            self.y = 0
    def moveDown(self,step):       
        if(self.y + step) <= 593:
            self.y += step
        else:
            self.y = 593
    def fire(self):
        #随机产生子弹,避免一直2连续产生子弹，重叠子啊一起
        randomNum = randint(1,100)
        if randomNum == 25 or randomNum == 75: 
            self.bulletList.append(EnemyBullet(self.x+26,self.y+47,self.screen))
    def move(self):
        if self.y < 0:
            self.y += 1
            return
        if self.count == self.time:
            if self.x == self.downX:
                self.y += 1#敌机向下移动的逻辑
                return
        if self.direction == 1:#右移
            self.x += 1
        elif self.direction == 0:#左移
            self.x -= 1
        if self.x > 423:#改变方向为左
            self.x = 423
            self.direction = 0
            self.count += 1
        if self.x < 0:#改变方向为右
            self.x = 0
            self.direction = 1
            self.count += 1
        
    def explode(self):
        self.explodeCount += 1
        if self.explodeCount == 8:
            if len(self.explodeImages) == 0:
                return
            #替换爆炸过程的图片
            if len(self.explodeImages) == 1:
                #随机产生补给
                if random.randint(0,1) == 0 and random.randint(0,1) == 0:
                    self.supply = Supply(self.screen,self.x,self.y,"./images/bullet_supply.png","bullet")
                elif random.randint(0,1) == 1 and random.randint(0,1) == 1: 
                    self.supply = Supply(self.screen,self.x,self.y,"./images/bomb_supply.png","bomb")
            self.plane = pygame.image.load(self.explodeImages.pop());         
            #为替换下一张图片重新计数
            self.explodeCount = 0
        return