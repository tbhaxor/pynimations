from __future__ import print_function
from time import sleep


class Animator:
    def __init__(self, label="Loading", interval=100, iteration=5):
        self.__label = label
        self.__interval = float(interval)/1000.0
        self.__iteration = iteration
        self.__elements = ["\\", "|", "/", "-"]
        pass

    def animate(self):
        while self.__iteration > 0:
            self.__iteration -= 1
            for element in self.__elements:
                print(end="\r")
                print(self.__label, element, end="")
                sleep(self.__interval)
                pass
            pass
        pass

    pass

a = Animator()
a.animate()
