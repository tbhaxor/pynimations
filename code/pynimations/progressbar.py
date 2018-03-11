# importing required modules
from pbars import ProgressBar
from time import sleep
import sys
import termisize as ts
class Animator:  # class Animator
    # constructor of class with some default parameters
    def __init__(self, label="Loading", interval=100, length=30, style="pip"):
        self.__interval = float(interval)/1000.0  # converting milli-secs to secs
        self.__pbar = ProgressBar(label, length, 100, style)   # making an instance of ProgressBar
        pass

    def animate(self):
        for x in range(100):   # loop to progress the bar
            self.__pbar.Progress(x+1)
            sleep(self.__interval)  # delay interval
            pass
        sys.stdout.write("\r" + " " * ts.get_cols() + "\n")
        pass
    pass
