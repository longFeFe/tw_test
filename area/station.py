# -*- coding: UTF-8 -*-

# 定义车站 也就是 图的定点
# 十字链表法 
from way import Way
class Station:
    def __init__(self, name):
        self.name = name
        #self.ways = None
        self.visited = False
    # 重写hask 做key用. 避免way和station耦合
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        if isinstance(other, Station):
            return self.name == other.name
        return False
    
    # def add_way(self, ways):
    #     print ways
    #     if ways.src.name != self.name:
    #         print '[Invalid parameter] way!'
    #         return False
    #     #FIXME: 检查重复的路线
    #     self.ways = ways
    #     return True