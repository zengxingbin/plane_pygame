#-*- coding:utf-8 -*-
#!E:\My software\python3.6
from enemy import Enemy
from random import randint
from enemybullet import EnemyBullet
class Enemy2(Enemy):
    def move(self):
        self.y += 1
    def fire(self):
        #随机产生子弹,避免一直2连续产生子弹，重叠子啊一起
        randomNum = randint(1,100)
        if randomNum == 25: 
            self.bulletList.append(EnemyBullet(self.x+26,self.y+47,self.screen))