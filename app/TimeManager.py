
import time
import json

class TimeManager() :
    def __init__(self) :
        self.mainTime = MyTime(self.__myMktime(time.localtime()))

    def update(self) :
        ltime = time.localtime()
        # local time + 5 hour 30 min ( == 19800 sec)
        # because when 18 h 30 m : dinner time is over
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

    def __repr__(self) :
        return self.__str__() + ' ' + str(self.sec)
        
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

tm = TimeManager()
