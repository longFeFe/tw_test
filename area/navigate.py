# -*- coding: UTF-8 -*-
from station import Station
from way import Way
class Navigate:
    # set area name. like xi`an  xianyang weinan
    def __init__(self, name):
        self.area = name
        self.stations = {}
    
    # init stations by way
    def init_station_by_ways(self, station, ways):
        '''[summary]
            初始化station表
        Arguments:
            station {[type]} -- [description]
            ways {} -- [description]
        
        Raises:
            Exception -- [description]
        
        Returns:
            [type] -- [description]
        '''
        # print ways.src.name + ' to ' + ways.dst.name
        if not isinstance(station, Station) or not isinstance(ways, Way):
            raise Exception("Invalid parameter", None)
        self.__add_route(station, ways)
        return True


    # 取station.的ways 拼接到stations[station.name].ways后 ? 区域搜索
    def __add_route(self, station, ways):
        # name = self.area + '.' + way.src
        if station not in self.stations:
            self.stations[station] = ways
            return
        current_ways = self.stations[station]
        while current_ways.next:
            current_ways = current_ways.next
        current_ways.set_next(ways)


    
    def distance_stations(self, stations):
        '''[summary]
            计算制定路线的距离
            bug: 站点之间必须相邻
        Arguments:
            stations {[]} -- [description]
        
        Returns:
            [type] -- int
            -1 无法联通
        '''

        distance = 0
        index = 0
        for station in stations:
            if len(stations) - 1 <= index:
                return distance # Find done
            index += 1

            if station not in self.stations: 
                return -1
            if stations[index] not in self.stations: 
                return -1
            
            src_way = self.stations[station]

            distance_between = self.__distance_between_adjacent(stations[index], src_way)
            if distance_between > 0:
                distance += distance_between
            else:
                return -1
            
        return distance


    def find_ways_by_max_distance(self, src_station, dst_station, max_distance):
        '''[summary]
            最大距离限制查找所有路径
        Arguments:
            src_station {[type]} -- [起点]
            dst_station {[type]} -- [终点]
            current_distance {[type]} -- []
            max_distance {[type]} -- [最大距离]
            deep {[type]} -- [description]
        
        Returns:
            [type] -- [[],[]]
        '''

        deep = []
        if src_station in self.stations and dst_station in self.stations:
            result = self.__dfs_find_all_ways_by_max_distance(src_station, dst_station, 0, max_distance, deep)
            # for r in result:
            #     for w in r:
            #         print w.name
            #     print '====='
            return result
        return []

    def find_ways_by_max_station_num(self, src_station, dst_station, max_num):
        '''[summary]
            最大站点数限制查找所有路径
        Arguments:
            src_station {[type]} -- [起点]
            dst_station {[type]} -- [终点]
            max_num {[type]} -- [路径中最大站点数 包含起点终点]
            deep {[type]} -- []
        
        Returns:
            [type] -- [[],[]]
        '''

        deep = []
        if src_station in self.stations and dst_station in self.stations:
            result = self.__dfs_find_all_ways_by_max_staion_num(src_station, dst_station, max_num, deep)
            # for r in result:
            #     for w in r:
            #         print w.name
            #     print '====='
            return result
        return []


    def find_all_ways(self, src_station, dst_station):
        '''[summary]
            找出src_station->dst_station之间的所有路线
            路径中不会有重复站点  如C->D->E->C->D->C路线不会被统计
        Arguments:
            src_station {[type]} -- [起点]
            dst_station {[type]} -- [终点]
        
        Returns:
            [type] -- [[],[]]
        '''

        if src_station not in self.stations or dst_station not in self.stations:
            return []
        deep = []
        list_way = self.__dfs_find_all_ways_stand(src_station, dst_station, deep)
        # for w in list_way:
        #     for s in w:
        #         print s.name
        #     print '======'

        return list_way



    def __distance_between_adjacent(self, dst, src_way):
        '''[summary]
            计算节点距离
        Arguments:
            dst {[type]} -- [description]
            src_way {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        '''

        if src_way.dst == dst:
            return src_way.distance
        if src_way.next:
            return self.__distance_between_adjacent(dst, src_way.next)
        return -1





    # 找出src_station->dst_station之间的所有路线
    # 标准DFS
    def __dfs_find_all_ways_stand(self, src_station, dst_station, deep):
        '''[summary]
            标准DFS方法遍历A->B所有路径
        Arguments:
            src_station {[type]} -- [起点]
            dst_station {[type]} -- [终点]
            deep {[type]} -- [description]
        
        Returns:
            [type] -- [[],[]]]
        '''

        src_station.visited = True
        src_way = self.stations[src_station]
        result = []
        
        while src_way:
            deep.append(src_way.src)
            if src_way.dst == dst_station:
                # print "src_way.src:" + src_way.src.name
                # print "src_way.dst:" + src_way.dst.name
                src_way = src_way.next
                l = deep[:]
                l.append(dst_station)
                # for w in l:
                #     print w.name
                # print '\t'
                result.append(l)
                deep.pop()
                continue
                
            if not src_way.dst.visited:
                ways = self.__dfs_find_all_ways_stand(src_way.dst, dst_station, deep)
                result += ways
            # 开始下一条路
            src_way = src_way.next
            deep.pop()
            #print src_way.src.name
        src_station.visited = False
        return result



    def __dfs_find_all_ways_by_max_distance(self, src_station, dst_station, current_distance, max_distance, deep):
        '''[summary]
            最大距离限制查找所有路径
        Arguments:
            src_station {[type]} -- [起点]
            dst_station {[type]} -- [终点]
            current_distance {[type]} -- []
            max_distance {[type]} -- [最大距离]
            deep {[type]} -- [description]
        
        Returns:
            [type] -- [[],[]]
        '''

        src_way = self.stations[src_station]
        result = []
        deep.append(src_way.src)
        while src_way:
            
            
            current_distance += src_way.distance
            if current_distance <= max_distance:
                if src_way.dst == dst_station:
                    
                    l = deep[:]
                    l.append(dst_station)
                    result.append(l)
                    # 此src的 出度 找到 dst 再继续沿用此出度路径 深度遍历
                    ways = self.__dfs_find_all_ways_by_max_distance(src_way.dst, dst_station, current_distance, max_distance, deep)
                    result += ways
                    # 下一条出度
                    src_way = src_way.next
                    continue
            
                ways = self.__dfs_find_all_ways_by_max_distance(src_way.dst, dst_station, current_distance, max_distance, deep)
                result += ways
            
            # 超出限制 
            # 此出度无法到达目的地 需要减去此出度的长度
            current_distance -= src_way.distance
            # 开始下一条路
            src_way = src_way.next
        # 此站的所有出度已遍历完毕 需要pop出此站
        deep.pop()
        return result
    

    def __dfs_find_all_ways_by_max_staion_num(self, src_station, dst_station, max_num, deep):
        '''[summary]
            最大站点数限制查找所有路径
        Arguments:
            src_station {[type]} -- [起点]
            dst_station {[type]} -- [终点]
            max_num {[type]} -- [路径中最大站点数 包含起点终点]
            deep {[type]} -- []
        
        Returns:
            [type] -- [[],[]]
        '''
        src_way = self.stations[src_station]
        result = []
        deep.append(src_way.src)
        while src_way:
            # + dst
            if len(deep) + 1 <= max_num:
                if src_way.dst == dst_station:
                    l = deep[:]
                    l.append(dst_station)
                    result.append(l)
                    # 此src的 出度 找到 dst 再继续沿用此出度路径 深度遍历
                    ways = self.__dfs_find_all_ways_by_max_staion_num(src_way.dst, dst_station, max_num, deep)
                    result += ways
                    # 下一条出度
                    src_way = src_way.next
                    continue
            
                ways = self.__dfs_find_all_ways_by_max_staion_num(src_way.dst, dst_station, max_num, deep)
                result += ways
            # 开始下一条路
            src_way = src_way.next
        # 此站的所有出度已遍历完毕 需要pop出此站
        deep.pop()
        return result








# 打印所有路线
def test_route_table(stations):
    for k, ways in stations.items():
        print k.name
        next_way = ways
        while next_way:
            print '\t' +  next_way.src.name + ' To ' + next_way.dst.name + ',distance:' + str(next_way.distance)
            next_way = next_way.next
    

