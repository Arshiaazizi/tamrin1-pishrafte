class Clock(object):
    def __init__(self, hour=12, minute=0, second=0, milTime=False):
        super(Clock,self).__init__()
        self.hour    = hour
        self.minute  = minute
        self.second  = second
        self.milTime = milTime  # 24-hour clock?

    @property
    def hour(self):
        return self._hour if self.milTime else ((self._hour-1) % 12)+1

    @hour.setter
    def hour(self, hour):
        self._hour = hour % 24

    @property
    def minute(self):
        return self._minute

    @minute.setter        
    def minute(self, minute):
        self._minute = minute % 60

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        self._second = second % 60

    @property
    def time(self):
        return self.hour, self.minute, self.second

    @time.setter
    def time(self, t):
        self.hour, self.minute, self.second = t

    def __str__(self):
        if self.milTime:
            return "{hr:02}:{min:02}:{sec:02}".format(hr=self.hour, min=self.minute, sec=self.second)
        else:
            ap = ("AM", "PM")[self._hour >= 12]
            return "{hr:>2}:{min:02}:{sec:02} {ap}".format(hr=self.hour, min=self.minute, sec=self.second, ap=ap)
