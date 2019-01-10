# -*- coding: UTF-8 -*-

from area import navigate
from area import way
from area import station

na = None
    
stationA = station.Station("A")
stationB = station.Station("B")
stationC = station.Station("C")
stationD = station.Station("D")
stationE = station.Station("E")

wayA = way.Way(stationA, stationB, 5).set_next(way.Way(stationA, stationD, 5).set_next(way.Way(stationA, stationE, 7)))
wayB = way.Way(stationB, stationC, 4)
wayC = way.Way(stationC, stationD, 8).set_next(way.Way(stationC, stationE, 2))
wayD = way.Way(stationD, stationC, 8).set_next(way.Way(stationD, stationE, 6))
wayE = way.Way(stationE, stationB, 3)
na = navigate.Navigate("tw")
na.init_route_by_station(stationA, wayA)
na.init_route_by_station(stationB, wayB)
na.init_route_by_station(stationC, wayC)
na.init_route_by_station(stationD, wayD)
na.init_route_by_station(stationE, wayE)

# class Answer:
#     def __init__(self):
#         pass
def find_way_by_station_num( src, dst, num):
    
    ways = na.find_all_ways(src, dst)
    #print len(ways)
    result = 0
    for way in ways:
        #print len(way)
        for w in way:
            print w.name
        print '\t'
        if len(way) - 1 == num:
            result += 1
    return result
def find_way_by_shortest(src, dst):
    ways = na.find_all_ways(src, dst)
    if len(ways) == 0:
        return -1
    result = ways.pop()
    # for w in result:
    #     print w.name
    # print '\t'

    min_len = na.distance_stations(result)
    for way in ways:
        # for w in way:
        #     print w.name
        # print '\t'
        current_len = na.distance_stations(way)
        if  current_len < min_len:
            min_len = current_len
    return min_len



def Q1():
    stations = [stationA, stationB, stationC]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #1: " +  str(ans)

def Q2():
    stations = [stationA, stationD]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #2: " +  str(ans)

def Q3():
    stations = [stationA, stationD, stationC]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #3: " +  str(ans)

def Q4():
    stations = [stationA, stationE, stationB, stationC, stationD]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #4: " +  str(ans)

def Q5():
    stations = [stationA, stationE, stationD]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #5: " +  str(ans)

def Q6():
    ans = na.find_ways_by_max_staions(stationC, stationC, 3)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #6: " +  str(ans)
def Q7():
    ans = find_way_by_station_num(stationA, stationC, 4)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #7: " +  str(ans)
def Q8():
    ans = find_way_by_shortest(stationA, stationC)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #8: " +  str(ans)
def Q9():
    ans = find_way_by_shortest(stationB, stationB)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #9: " +  str(ans)
def Q10():
    ans = na.find_ways_by_max_distance(stationC, stationC, 30 - 1)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #10: " +  str(ans)



if __name__ == "__main__":
    pass
    
