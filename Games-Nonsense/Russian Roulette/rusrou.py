#!/usr/bin/python3
#Licensed under the WTFPL

#A simple Russian Roulette game

import random 

in_ch = 1
land_ch = random.randint(1,7)

if in_ch == land_ch: 
	print('BANG!... Hey, who put a blank in here?')

else: 
	print('Click')
	print('Safe this time')
