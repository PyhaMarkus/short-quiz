#!/usr/bin/python

import sys
import time
import signal

# sudo apt-get install python3-pip
# pip3 install termcolor
from termcolor import colored
from termcolor import cprint
# pip3 install colorama
from colorama import init

# pip3 install pyfiglet
from pyfiglet import figlet_format

# Function starts here
def startQuiz():

	# Variables
	adminKillSwitch = "admin" # Input to kill script

	rightAnswer = "linux" # Do not use CAPS!
	prize = "SECRET _ KEY"

	# Loop this
	while True:
		while True:
			userAnswer = input("What's the correct answer?:    ").lower()
			if not userAnswer:
				print(colored("Invalid user input", "red"))
				continue

			else:
				break

		if userAnswer == rightAnswer:
			#print(colored("Well done! Take this:  " + prize + "\nYou will need it later!\n", "green"))
			print(colored("Well done! Take this, you'll need it later:", "green"))
			cprint(figlet_format(prize), "green")
			time.sleep(10)

		elif userAnswer == adminKillSwitch:
			sys.exit() # Killswitch for admins

		else:
			print (colored("Wrong!\n", "red"))

# Function ends here

# Signal handlers for preventing KeyboardInterrupt
# SIGINT translates into a KeyboardInterrupt exception & SIG_IGN ignores the given signal
s = signal.signal(signal.SIGINT, signal.SIG_IGN)
startQuiz() # Call function
signal.signal(signal.SIGINT, s)
