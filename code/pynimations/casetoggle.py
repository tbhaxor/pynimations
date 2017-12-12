# importing all modules
from time import sleep


# class for CaseToggle Animation
class Animator:
    # ----------
    #  Class Parametrised Constructor for private data members
    # ----------
    def __init__(self, label="Loading", interval=100, iteration=5):
        self.__label = label
        self.__interval = float(interval) / 1000.0  # Converting milli-sec to sec
        self.__iteration = iteration
        self.__len = len(self.__label)
        pass

    # --------------
    # Public method to display the animation on the terminal
    # --------------
    def animate(self):
        for k in range(self.__iteration):  # iteration loop
            for i in range(self.__len):  # main trigger loop
                if not self.__label[i].isalpha(): continue  # if the current element is not alphabet, skip it
                print(end="\r")  # reverse the whole line for overwriting the new one
                for j in range(self.__len):   # inner loop
                    if j == i: # if the
                        print(self.__toggleCase(self.__label[j]), end="")  # if trigger loop number and inner loop matches then toggle case
                    else:
                        print(self.__label[j], end="")  # else print the character as it is
                sleep(self.__interval)  # delay for process
        pass

    # -------------
    # Private Method to toggle Letter casing
    # -------------
    def __toggleCase(self, letter):
        return "".join(map(str.swapcase, letter))

    pass
