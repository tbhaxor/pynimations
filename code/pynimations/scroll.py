from __future__ import division
import sys
import time
import termisize as ts

class Animator:     
    def __init__(self, label="Loading", iteration=3, interval=100, length=7):
        self.__lbl = label + " "
        self.__itr = iteration
        self.__ivl = interval/1000.0
        self.__len = length
        if length < 1:
            self.__len =ts.get_cols() - len(label) - 1
        
    def animate(self):
        try:
            for _ in range(self.__itr):
                for x in range(0, self.__len):
                    time.sleep(0.1)
                    msg = "\r{}{}".format(" " * x, self.__lbl)
                    sys.stdout.write(msg)
                    sys.stdout.flush()

                for x in range(self.__len, 0, -1):
                    time.sleep(0.1)
                    msg = "\r{}{}".format(" " * x, self.__lbl)
                    sys.stdout.write(msg)
                    sys.stdout.flush()
        except KeyboardInterrupt:
            pass
        sys.stdout.write("\r"+ " "*ts.get_cols() + "\n")
        pass
    pass
