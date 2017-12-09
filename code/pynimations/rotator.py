# importing modules for animations
from time import sleep


# class used to display animations
class Animator:
    def __init__(self, label="Loading", interval=100, iteration=5):  # default parameters of the constructor
        self.__label = label
        self.__interval = float(interval)/1000.0   # converting milli-secs to secs
        self.__iteration = iteration
        self.__elements = ["\\", "|", "/", "-"]  # ascii rotating elements
        pass

    # public method to display animations
    def animate(self):
        i = self.__iteration
        while i > 0:  # iterating till iteration != 0
            i -= 1    # decreasing iter by 1
            for element in self.__elements:   # for each element in ascii rotator elements
                print(end="\r")  # moving display cursor to the beginning of line
                print(self.__label, element, end="")   # replacing  end character "\n" with ""
                sleep(self.__interval)  # giving sleep
                pass
            pass
        print("\b ")  # printing new line
        pass

    pass

