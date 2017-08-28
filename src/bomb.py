#-*- coding:utf-8 -*-
#!E:My software\python3.6
from mybullet import MyBullet
class Bomb(MyBullet):
    def judge(self):
        return self.y + 57 < 0