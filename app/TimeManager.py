
from Src import src
import time
import json

class TimeManager() :
    def __init__(self) :
        self.mainTime = MyTime(self.__myMktime(time.localtime()))

    def update(self) :
        ltime = time.localtime()
        # local time = local time + 5 hour 30 min ( == 19800 sec)
        # because 18h 30m : dinner time over
        # (today's dinner time over -> have to update time to next day)
        ltime = time.localtime(int(time.mktime(ltime)) + 19800)

        if list(self.mainTime.st)[:3] != list(ltime)[:3] :
            self.mainTime = MyTime(self.__myMktime(ltime))
            print('tm update')
            return True
        return False

    # calculation day's mktime when time is 00 h 00 m 00 s
    def __myMktime(self, structTime) :
        if type(structTime) != time.struct_time :
            print('TimeManager.py - __myMktime function error')
            structTime = time.localtime()
        st = structTime
        st = list(st)
        st[3:6] = [0, 0, 0] # hour, min, second == 0, 0, 0
        st = time.struct_time(st)
        return int(time.mktime(st))
        

class MyTime() :
    def __init__(self, val = None) :
        # val == time.struct_time or time.mktime(st)
        if type(val) == time.struct_time :
            self.st = val
            self.sec = int(time.mktime(val))
        elif type(val) == int :
            self.sec = val
            self.st = time.localtime(val)
        else :
            self.st = time.localtime(0)
            self.sec = 0 # time.mktime(st)

    def toString(self) :
        return self.__str__() + '(' + src.wday[self.st[6]] + ')'

    def __str__(self) :
        return str(self.st[1]) + '.' + str(self.st[2])

    def __repr__(self) :
        return self.st[0] + self.__str__() + ' ' + str(self.sec)
        
    def __lt__(self, other) :
        return self.sec < other.sec

    def __le__(self, other) :
        return self.sec <= other.sec

    def __eq__(self, other) :
        return self.sec == other.sec

    def __ne__(self, other) :
        return self.sec != other.sec

    def __gt__(self, other) :
        return self.sec > other.sec

    def __ge__(self, other) :
        return self.sec >= other.sec

    def __hash__(self) :
        return self.sec

tm = TimeManager()
