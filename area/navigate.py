# -*- coding: UTF-8 -*-
from station import Station
from way import Way
class Navigate:
    # set area name. like xi`an  xianyang weinan
    def __init__(self, name):
        self.area = name
        self.stations = {}
    # init stations by file
    def init_route_by_file(self, file):
        pass
    # init stations by way
    def init_route_by_station(self, station, ways):
        if not isinstance(station, Station) or not isinstance(ways, Way):
            raise Exception("Invalid parameter", None)
        self.add_route(station, ways)
        return True

    # 取station.的ways 拼接到stations[station.name].ways后 ? 区域搜索
    def add_route(self, station, ways):
        # name = self.area + '.' + way.src
        if station not in self.stations:
            self.stations[station] = ways
            return
        return
        
    # 只能解析固定格式的文件内容
    def __parse_file(self, f):
        with open(f, 'r') as content_file:
            data = content_file.read()
    
    # 计算相邻节点之间的距离
    # return value:
    #  <= 0 无法联通
    #  > 0 距离
    def __distance_between_adjacent(self, dst, src_way):
        #print src_way.dst.name + '->' + dst.name
        if src_way.dst == dst:
            return src_way.distance
        if src_way.next:
            return self.__distance_between_adjacent(dst, src_way.next)
        return -1
    
    # 计算stations之间的长度
    # 按预定路线行驶  BFS
    # return value:
    #  <= 0 无法联通
    #  > 0 距离
    def distance_stations(self, stations):
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


    # 找出A->B之间路线 限制最大站数
    # def find_ways_by_max_staions(self, src_station, dst_station, max_staions):
    #     ways = self.find_all_ways(src_station, dst_station)
    #     result = 0
    #     if len(ways) == 0:
    #         return -1
    #     for way in ways:
    #         if len(way) - 1 <= max_staions:
    #             result += 1
    #     return result
    # def find_ways_by_max_staions(self, src_station, dst_station, max_staions):
    #     routes = 0
    #     # Check if start and end nodes exists in route table
    #     if src_station not in self.stations or dst_station not in self.stations:
    #         return -1
        

     

    #     src_way = self.route_table[src_station]

    #     while src_way:
    #         distance += stop.distance
    #         # If distance is under max, keep traversing
    #         # even if match is found until distance is > max

    #         if distance <= max_distance:
    #             if stop.destination == town_end:
    #                 routes += 1
    #                 routes += self.find_num_routes_within(stop.destination, town_end, distance, max_distance)
    #                 stop = stop.next_stop
    #                 continue

    #             else:
    #                 routes += self.find_num_routes_within(stop.destination, town_end, distance, max_distance)
    #                 distance -= stop.distance  # Decrement distance as we backtrack


    #         else:
    #             distance -= stop.distance

    #         stop = stop.next_stop


    #     else:
    #         return "NO SUCH ROUTE"

    #     return routes

     # 找出A->B之间路线 限制最大长度
    def find_ways_by_max_distance(self, src_station, dst_station, max_distance):
        ways = self.find_all_ways(src_station, dst_station)
        result = 0
        if len(ways) == 0:
            return -1
        for way in ways:
            if self.distance_stations(way) <= max_distance:
                result += 1
        return result

     # 找出src_station->dst_station之间的所有路线
    def find_all_ways(self, src_station, dst_station):
        if src_station not in self.stations or dst_station not in self.stations:
            return []
        deep = []
        result = []
        list_way = self.__dfs_find_all_ways(src_station, dst_station, deep, result)
        return list_way





    # 找出src_station->dst_station之间的所有路线
    # DFS
    def __dfs_find_all_ways(self, src_station, dst_station, deep, result):
        src_station.visited = True
        src_way = self.stations[src_station]
        
        
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
                self.__dfs_find_all_ways(src_way.dst, dst_station, deep, result)
            # 开始下一条路
            src_way = src_way.next
            #if len(deep) > 0: # 下次循环会重新压入
            deep.pop()
            #print src_way.src.name
        src_station.visited = False
        # if len(deep) > 0:
        #     deep.pop()
        return result








# 打印所有路线
def test_route_table(stations):
    for k, ways in stations.items():
        print k.name
        next_way = ways
        while next_way:
            print '\t' +  next_way.src.name + ' To ' + next_way.dst.name + ',distance:' + str(next_way.distance)
            next_way = next_way.next
    

