#-*- coding:utf-8 -*-
#!E:\My software\python3.6
#定义住函数，即程序的入口函数
import pygame
import random
import time
from bullet import Bullet
from myplane import MyPlane
from enemy import Enemy
from pygame.locals import *
def keyControl(heroPlane):
    #获取事件，比如按键等
    for event in pygame.event.get():
            #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
         #判断是否是按下了键
        elif event.type == KEYDOWN:
             #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                heroPlane.moveLeft(10)
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                heroPlane.moveRight(10)
            elif event.key == K_w or event.key == K_UP:
                heroPlane.moveUP(10)
            elif event.key == K_s or event.key == K_DOWN:
                heroPlane.moveDown(10)
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                heroPlane.fire()
                print('space')
def main():
    '''程序的入口'''
    #创建一个窗口
    screen = pygame.display.set_mode((480,650),0,32)
    #创建一个和窗口一样大小的背景图片
    background = pygame.image.load("./images/background.png")
    #创建一个飞机对象
    heroPlane = MyPlane(screen)
    #创建敌机
    enemy = Enemy(screen);
    #敌机爆炸后，剩余子弹列表
    enemyBulletList = None
    #x = 217
    #y = 593
    #将图片放在窗口上，作为背景图片
    while True:
        screen.blit(background,(0,0))
        #显示飞机
        heroPlane.display(enemy)
        if enemy.isAlive:
            #敌机移动
            enemy.move()
            #敌机开火
            enemy.fire()
            #敌军越界删除敌军
            if enemy.y >= 650:
                #创建新敌机
                enemy = Enemy(screen)
        else:
            enemy.explode()
            if  len(enemy.explodeImages)== 0:
                #如果还有子弹，找一个变量来记录子弹列表
                if enemy.bulletList:
                    enemyBulletList = enemy.bulletList
                #敌机爆炸后，创建新敌机
                enemy = Enemy(screen)
        #让敌机爆炸后剩余的子弹继续飞行
        if enemyBulletList != None and enemyBulletList:
            for bullet in enemyBulletList:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    enemyBulletList.remove(bullet)
                    
                        
        #显示敌机
        enemy.display()
        #飞机不停的开火
        #heroPlane.fire()
        #键盘事件控制飞机的移动         
        keyControl(heroPlane)
        pygame.display.update()
        time.sleep(0.01)
if __name__ == "__main__":
    main()    