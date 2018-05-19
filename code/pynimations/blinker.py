from time import sleep
from sys import stdout

class Animator():
	def __init__(self, label="Loading", iterations=3, interval=500):
		self.__label = label
		self.__inter = iterations
		self.__delay = interval / 1000
		pass

	def animate(self):
		show = True
		for _ in range(self.__inter * 2):   # one for show and another for hide
			if show:
				stdout.write("\r")
				stdout.write(self.__label)
				stdout.flush()
				show = False
				pass
			else:
				stdout.write("\r")
				stdout.write(" "*len(self.__label))
				stdout.flush()
				show = True
				pass
			sleep(self.__delay)
			pass
		pass