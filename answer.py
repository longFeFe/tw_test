# -*- coding: UTF-8 -*-

from area import navigate
from area import way
from area import station
import unittest
import sys
#import getopt


na = None

stationA = station.Station("A")
stationB = station.Station("B")
stationC = station.Station("C")
stationD = station.Station("D")
stationE = station.Station("E")


def init_station_by_ways():
    global na
    wayA = way.Way(stationA, stationB, 5).set_next(way.Way(stationA, stationD, 5).set_next(way.Way(stationA, stationE, 7)))
    wayB = way.Way(stationB, stationC, 4)
    wayC = way.Way(stationC, stationD, 8).set_next(way.Way(stationC, stationE, 2))
    wayD = way.Way(stationD, stationC, 8).set_next(way.Way(stationD, stationE, 6))
    wayE = way.Way(stationE, stationB, 3)
    na = navigate.Navigate("tw")
    na.init_station_by_ways(stationA, wayA)
    na.init_station_by_ways(stationB, wayB)
    na.init_station_by_ways(stationC, wayC)
    na.init_station_by_ways(stationD, wayD)
    na.init_station_by_ways(stationE, wayE)
    return True


def __parse_file(f):
    '''[summary]
        解析固定格式的文件
    Arguments:
        f {[type]} -- [file stream]
    '''
    global na
    line = f.readline()
    while line:
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        items = line.split(':')
        if len(items) <= 0:
            return False
        
        if len(items) == 2:
            if na: # 已经初始化过
                return False
            na = navigate.Navigate(items[0])
            items.pop(0)
        if na == None:
            return False
        str_ways = items[0].split(',')

        # FIXME: data check
        for str_w in str_ways:
            src = station.Station(str_w[0])
            dst = station.Station(str_w[1])
            dist = int(str_w[2])
            na.init_station_by_ways(src, way.Way(src, dst, dist))
        line = f.readline()
    return True


def init_stations_by_file(file):
    '''[summary]
        从文件中初始化stations表
    Arguments:
        file {[type]} -- [filepath]
    
    Returns:
        [type] -- [description]
    '''
    try:
        f = open(file, mode='r')
        ret = __parse_file(f)
        f.close()
        #navigate.test_route_table(na.stations)
        return ret
    except BaseException:
        return False


    




def find_way_by_station_num( src, dst, num):
    ways = na.find_ways_by_max_station_num(src, dst, num + 1)
    result = 0
    for way in ways:
        if len(way) - 1 == num:
            result += 1
    return result



def find_way_by_shortest(src, dst):
    ways = na.find_all_ways(src, dst)
    if len(ways) == 0:
        return -1
    result = ways.pop()

    min_len = na.distance_stations(result)
    for way in ways:
        current_len = na.distance_stations(way)
        if  current_len < min_len:
            min_len = current_len
    return min_len



# questions
def Q1():
    stations = [stationA, stationB, stationC]
    #stations = [stationA, stationC, stationD]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #1: " +  str(ans)
    return ans

def Q2():
    stations = [stationA, stationD]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #2: " +  str(ans)
    return ans

def Q3():
    stations = [stationA, stationD, stationC]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #3: " +  str(ans)
    return ans

def Q4():
    stations = [stationA, stationE, stationB, stationC, stationD]
    ans = na.distance_stations(stations)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #4: " +  str(ans)
    return ans

def Q5():
    stations = [stationA, stationE, stationD]
    ans = na.distance_stations(stations)
    #ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #5: " +  str(ans if ans > 0 else "NO SUCH ROUTE")
    return ans


def Q6():
    ans = len(na.find_ways_by_max_station_num(stationC, stationC, 3 + 1))
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #6: " +  str(ans)
    return ans

def Q7():
    ans = find_way_by_station_num(stationA, stationC, 4)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #7: " +  str(ans)
    return ans

def Q8():
    ans = find_way_by_shortest(stationA, stationC)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #8: " +  str(ans)
    return ans

def Q9():
    ans = find_way_by_shortest(stationB, stationB)
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #9: " +  str(ans)
    return ans

def Q10():
    ans = len(na.find_ways_by_max_distance(stationC, stationC, 30))
    ans = ans if ans > 0 else "NO SUCH ROUTE"
    print "Output #10: " +  str(ans)
    return ans



# 单元测试
class UnitTest(unittest.TestCase):
    def test_Q1(self):
        self.assertEquals(9, Q1())

    def test_Q2(self):
        self.assertEquals(5, Q2())

    def test_Q3(self):
        self.assertEquals(13, Q3())

    def test_Q4(self):
        self.assertEquals(22, Q4())

    def test_Q5(self):
        self.assertEquals(-1, Q5())

    def test_Q6(self):
        self.assertEquals(2, Q6())
    
    def test_Q7(self):
        self.assertEquals(3, Q7())

    def test_Q8(self):
        self.assertEquals(9, Q8())

    def test_Q9(self):
        self.assertEquals(9, Q9())

    def test_QA(self):
        self.assertEquals(7, Q10())



def main(argv):
    if len(argv) == 3:
        if argv[1] == "--file" or argv[1] == "-f":
            return init_stations_by_file(argv[2])
    else:
        return init_station_by_ways()
        #Usage()
if __name__ == "__main__":
    if not main(sys.argv):
        print 'Init Faild'
        exit(0)
    sys.argv = sys.argv[:1]
    unittest.main()
