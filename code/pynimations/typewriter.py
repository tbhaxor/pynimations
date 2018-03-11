# importing required modules
from time import sleep
import sys
import termisize as ts
class Animator:  # class Animator
	# constructor of class with some default parameters
	def __init__(self, label=["[!] Loading",], interval=100, wait_unitl=1000):
		self.__interval = float(interval)/1000.0  # converting milli-secs to secs
		self.__label = label   # getting the label
		self.__wait = float(wait_unitl)/1000.0
		pass

	def animate(self):
		for x in self.__label:
			for y in x:
				sys.stdout.write(y)
				sys.stdout.flush()
				sleep(self.__interval)
				pass
			sleep(self.__wait) # waiting for backspace
			self.__back(len(x))
		sys.stdout.write("\r" + " " * ts.get_cols() + "\n")
		pass

	# ------
	# Priv8 method to print backspace
	# ------
	def __back(self, l):
		for _ in range(l):
			sys.stdout.write("\b \b")
			sys.stdout.flush()
			sleep(self.__interval)

	pass
