#!/usr/bin/python

import sys
import time
import signal

# sudo apt-get install python3-pip
# pip3 install termcolor
from termcolor import colored

# Function starts here
def startQuiz():
	while True:
		while True:
			try:
				question = int(input('Mikä on oikea numerosarja?:	'))

			except ValueError:
				print(colored("That's not a valid option!\n","red"))
				continue
			else:
				break

		if question == 1:
			print(colored("Well done! Take this code: 1234\nYou will need it later!\n", "green"))
			time.sleep(10)

		elif question == 9999: # Killswitch value for admins
			sys.exit()

		else:
			print (colored("Wrong!\n", "red"))

# Function ends here

# Signal handlers for preventing KeyboardInterrupt
# SIGINT translates into a KeyboardInterrupt exception & SIG_IGN ignores the given signal
s = signal.signal(signal.SIGINT, signal.SIG_IGN)
startQuiz() # Call function
signal.signal(signal.SIGINT, s)
