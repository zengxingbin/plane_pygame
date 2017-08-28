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
from itertools import count
from mybullet import MyBullet
from enemy2 import Enemy2
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
                heroPlane.moveLeft(15)
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                heroPlane.moveRight(15)
            elif event.key == K_w or event.key == K_UP:
                heroPlane.moveUP(15)
            elif event.key == K_s or event.key == K_DOWN:
                heroPlane.moveDown(15)
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                heroPlane.fire()
                print('space')
            elif event.key == K_f:
                heroPlane.launchBomb()
                print("launch bomba")
def main():
    '''程序的入口'''
    #创建一个窗口
    screen = pygame.display.set_mode((480,650),0,32)
    #创建一个和窗口一样大小的背景图片
    background = pygame.image.load("./images/background.png")
    #创建一个飞机对象
    heroPlane = MyPlane(screen)
    #计数已经产生多少敌机
    countEnemy = 0
    #创建敌机列表
    enemyList = []
    #失效敌机列表d
    invalidEnemyList = []
    #敌机爆炸后，剩余子弹列表
    enemyBulletList = []
    #敌机补给列表
    supplyList = []
    #x = 217
    #y = 593
    #将图片放在窗口上，作为背景图片
    while True:
        screen.blit(background,(0,0))
        #如果敌机咧列表为空，创建敌机
        if countEnemy <= 5:
            if not enemyList:
                enemyList.append(Enemy(screen,10))
                countEnemy += 1
        elif countEnemy > 5 and countEnemy <= 10:
            if not enemyList:
                enemyList.append(Enemy(screen,20))
                enemyList.append(Enemy(screen,20))
                countEnemy += 1
        elif countEnemy > 10 and countEnemy <= 15:
            if not enemyList:
                enemyList.append(Enemy(screen,30))
                enemyList.append(Enemy(screen,30))
                enemyList.append(Enemy(screen,30))
                countEnemy += 1
        elif countEnemy > 15 and countEnemy <= 20:
            if not enemyList:
                enemyList.append(Enemy2(screen,40,34,-129))
                enemyList.append(Enemy2(screen,40,93,-86))
                enemyList.append(Enemy2(screen,40,152,-43))           
                enemyList.append(Enemy2(screen,40,211,0))
                enemyList.append(Enemy2(screen,40,270,-43))
                enemyList.append(Enemy2(screen,40,329,-86))
                enemyList.append(Enemy2(screen,40,388,-129))    
                countEnemy += 1
        if not heroPlane.isAlive:
            heroPlane.explode()
        #英雄飞机爆炸完毕
        if not heroPlane.explodeImages:
            time.sleep(1)
            print("游戏结束！")
            break 
        #显示飞机
        heroPlane.display(enemyList)
        #显示敌机
        for enemy in enemyList:
            enemy.display(heroPlane)
        #遍历敌机列表
        for enemy in enemyList:
            if enemy.isAlive:
                #敌机移动
                enemy.move()
                #敌机开火
                enemy.fire()
                #敌军越界添加到失效敌机列表
                if enemy.y >= 650:
                    #添加到失效敌机列表
                    invalidEnemyList.append(enemy)
            else:
                enemy.explode();
                if  len(enemy.explodeImages)== 0:
                #如果还有子弹，找一个列表来记录子弹列表
                    if enemy.bulletList:
                        enemyBulletList.append(enemy.bulletList) 
                    #如果敌机爆炸后有补给，添加到补给列表
                    if enemy.supply:
                        supplyList.append(enemy.supply)
                    #添加到失效敌机列表
                    invalidEnemyList.append(enemy)
        #遍历每一架敌机的子弹列表，让敌机爆炸后剩余的子弹继续飞行
        if enemyBulletList:
            for bulletList in enemyBulletList: 
                for bullet in bulletList:
                    bullet.display()
                    bullet.move()
                    if bullet.judge():
                        bulletList.remove(bullet)
                    elif (bullet.x > heroPlane.x+25 and bullet.x < heroPlane.x+77) and (bullet.y > heroPlane.y and bullet.y < heroPlane.y+126):
                        heroPlane.blood -= 10
                        bulletList.remove(bullet)
        # 遍历敌机补给列表           
        if supplyList:
            for supply in supplyList:
                supply.display()
                supply.move()
                #子弹越界
                if supply.judge():
                    supplyList.remove(supply)
                #子弹被吃了
                elif supply.x+58 > heroPlane.x and supply.x+58<=heroPlane.x+102 and supply.y+88 > heroPlane.y and supply.y+88 < heroPlane.y+126:
                    supplyList.remove(supply)
                    if supply.supplyName == "bullet":
                        heroPlane.bulletSupplyNum += 10
                    elif supply.supplyName == "bomb":
                        heroPlane.bombSupplyNum += 10
                elif supply.x > heroPlane.x and supply.x<=heroPlane.x+102 and supply.y+88 > heroPlane.y and supply.y+88 < heroPlane.y+126:
                    supplyList.remove(supply)
                    if supply.supplyName == "bullet":
                        heroPlane.bulletSupplyNum += 10
                    elif supply.supplyName == "bomb":
                        heroPlane.bombSupplyNum += 10
                elif supply.x+58 > heroPlane.x and supply.x+58<=heroPlane.x+102 and supply.y > heroPlane.y and supply.y < heroPlane.y+126:
                    supplyList.remove(supply)
                    if supply.supplyName == "bullet":
                        heroPlane.bulletSupplyNum += 10
                    elif supply.supplyName == "bomb":
                        heroPlane.bombSupplyNum += 10
                elif supply.x > heroPlane.x and supply.x<=heroPlane.x+102 and supply.y > heroPlane.y and supply.y < heroPlane.y+126:
                    supplyList.remove(supply)
                    if supply.supplyName == "bullet":
                        heroPlane.bulletSupplyNum += 10
                    elif supply.supplyName == "bomb":
                        heroPlane.bombSupplyNum += 10
                
        #从 敌机列表中删除失效敌机列表
        if invalidEnemyList:
            for enemy in invalidEnemyList:
                enemyList.remove(enemy)
        #清空失效敌机列表
        invalidEnemyList.clear()
        #飞机不停的开火
        #heroPlane.fire() 
        #键盘事件控制飞机的移动         
        keyControl(heroPlane)
        pygame.display.update()
        time.sleep(0.01)
if __name__ == "__main__":
    main()    