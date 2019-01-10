# -*- coding: UTF-8 -*-

# 定义某个车站的驶出路线 也就是 出度 
# 十字链表法 

class Way:
    def __init__(self, src_station, dst_station, distance):
        self.src = src_station
        self.dst = dst_station
        self.distance = distance
        self.next = None
    def set_next(self, way):
        self.next = way
        return self
    
