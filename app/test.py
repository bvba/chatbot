import time

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

    def __str__(self) :
        return str(self.st[0]) + '.' + str(self.st[1]) + '.' + str(self.st[2])

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

    def __hash__(self) :
        return self.sec
