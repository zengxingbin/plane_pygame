#-*- coding:utf-8 -*-
#!E:\My software\python3.6
import pygame
import random
from mybullet import MyBullet
from bomb import Bomb
class MyPlane(object):
    def __init__(self,screen):
        self.plane = pygame.image.load("./images/me2.png");#46 * 57
        #飞机起始的随机坐标值
        self.x = random.randint(0,378)#(0,434)
        self.y = random.randint(350,524)#(325,593)
        self.screen = screen
        self.isAlive = True#是否存活
        self.bulletList = []#子弹列表
        self.invalidBullet = []#失效子弹列表
        #爆炸计数
        self.explodeCount = 0
        #爆炸图片列表
        self.explodeImages = ['./images/me_destroy_4.png','./images/me_destroy_4.png','./images/me_destroy_3.png','./images/me_destroy_2.png','./images/me_destroy_1.png']
        #子弹补给列表
        self.bulletSupplyList = []
        self.bulletSupplyNum=0
        #炸弹补给列表
        self.bombSupplyList=[]
        self.bombSupplyNum = 0
        self.blood = 100
    def display(self,enemyList):
        self.screen.blit(self.plane,(self.x,self.y))
        if self.bulletSupplyList:
            #遍历子弹列表，判断子弹是否击中敌机
            for bullet in self.bulletSupplyList:
                for enemy in enemyList:
                    if (bullet.x+5 > enemy.x and bullet.x+5 < enemy.x+57) and (bullet.y+11 > enemy.y and bullet.y+11 < enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
                    elif (bullet.x > enemy.x and bullet.x < enemy.x+57) and (bullet.y+11 > enemy.y and bullet.y+11 < enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
                    elif (bullet.x+5 > enemy.x and bullet.x+5 < enemy.x+57) and (bullet.y> enemy.y and bullet.y< enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
                    elif (bullet.x > enemy.x and bullet.x < enemy.x+57) and (bullet.y > enemy.y and bullet.y < enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
            for bullet in self.bulletSupplyList:
                bullet.display()
                #子弹往上移动
                bullet.move()
                if bullet.judge():
                    self.invalidBullet.append(bullet)   
        if self.bulletList:
            #遍历子弹列表，判断子弹是否击中敌机
            for bullet in self.bulletList:
                for enemy in enemyList:
                    if (bullet.x+5 > enemy.x and bullet.x+5 < enemy.x+57) and (bullet.y+11 > enemy.y and bullet.y+11 < enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
                        
                    elif (bullet.x > enemy.x and bullet.x < enemy.x+57) and (bullet.y+11 > enemy.y and bullet.y+11 < enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
                        
                    elif (bullet.x+5 > enemy.x and bullet.x+5 < enemy.x+57) and (bullet.y> enemy.y and bullet.y< enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
                    elif (bullet.x > enemy.x and bullet.x < enemy.x+57) and (bullet.y > enemy.y and bullet.y < enemy.y+43):
                        if(enemy.blood > 0):
                            enemy.blood -= bullet.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bullet)
            for bullet in self.bulletList:
                bullet.display()
                #子弹往上移动
                bullet.move()
                #判断子弹是否越界，越界的时候，将子弹从列表中删除
                '''注意不要在遍历列表的时候同时删除元素，会有坑，会漏删，但此
                display方法是循环调用的，列表也是每次从头到尾循环遍历删除的因此
                                                        最后肯定能把所有越界的子弹删除，最好的办法是定义个列表把要删的子弹存起来
                                                         然后再遍历删除'''
                if bullet.judge():
                    self.invalidBullet.append(bullet)
                    #self.bulletList.remove(bullet)
        if self.bombSupplyList:
            for bomb in self.bombSupplyList:
                for enemy in enemyList:
                    if (bomb.x+63 > enemy.x and bomb.x+63 < enemy.x+57) and (bomb.y+57 > enemy.y and bomb.y+57 < enemy.y+43):
                        if enemy.blood > 0:
                            enemy.blood -= bomb.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bomb)
                    elif (bomb.x > enemy.x and bomb.x < enemy.x+57) and (bomb.y+57 > enemy.y and bomb.y+57 < enemy.y+43):
                        if enemy.blood > 0:
                            enemy.blood -= bomb.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bomb)  
                    elif (bomb.x+63 > enemy.x and bomb.x+63 < enemy.x+57) and (bomb.y > enemy.y and bomb.y < enemy.y+43):
                        if enemy.blood > 0:
                            enemy.blood -= bomb.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bomb)
                    if (bomb.x > enemy.x and bomb.x < enemy.x+57) and (bomb.y > enemy.y and bomb.y < enemy.y+43):
                        if enemy.blood > 0:
                            enemy.blood -= bomb.strength
                        if enemy.blood <= 0:
                            enemy.isAlive = False
                        self.invalidBullet.append(bomb)     
                for bomb in self.bombSupplyList:
                    bomb.display()
                    bomb.move()
                    if bomb.judge():
                        self.invalidBullet.append(bomb)
        if self.invalidBullet:
            for bullet in self.invalidBullet:
                if self.bulletList.__contains__(bullet):
                    self.bulletList.remove(bullet)
                elif self.bulletSupplyList.__contains__(bullet):
                    self.bulletSupplyList.remove(bullet)
                elif self.bombSupplyList.__contains__(bullet):
                    self.bombSupplyList.remove(bullet)
        #清空已删除的失效子弹列表
        self.invalidBullet.clear()    
                
    def moveLeft(self,step):
        if (self.x - step) >= 0:         
            self.x -= step
        else:
            self.x = 0
    def moveRight(self,step):
        if (self.x + step) <= 378:
            self.x += step
        else:
            self.x = 378
    def moveUP(self,step):
        if(self.y - 10) >= 0:
            self.y -= step
        else:
            self.y = 0
    def moveDown(self,step):       
        if(self.y + step) <= 524:
            self.y += step
        else:
            self.y = 524
    def fire(self):
        if self.bulletSupplyNum <= 0:
            self.bulletList.append(MyBullet((self.x + 51),self.y,self.screen,"./images/bullet1.png",10))
        else:
            self.bulletSupplyList.append(MyBullet((self.x + 51),self.y,self.screen,"./images/bullet2.png",20))
            self.bulletSupplyNum -= 1
    def launchBomb(self):
        if self.bombSupplyNum > 0:
            self.bombSupplyList.append(Bomb((self.x + 20),self.y+30,self.screen,"./images/bomb.png",50))
            self.bombSupplyNum -= 1
    def explode(self):
        self.explodeCount += 1
        if self.explodeCount == 8:
            if len(self.explodeImages) == 0:
                return
            #替换爆炸过程的图片
            self.plane = pygame.image.load(self.explodeImages.pop());         
            #为替换下一张图片重新计数
            self.explodeCount = 0
        return    
                                                                    
                    
    