# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/28 20:14:25 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/29 12:28:39 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

NESTED_MORSE = {
	" " : "/ ",
	"A" : ".- ",
	"B" : "-... ",
	"C" : "-.-. ",
	"D" : "-.. ",
	"E" : ". ",
	"F" : "..-. ",
	"G" : "--. ",
	"H" : ".... ",
	"I" : ".. ",
	"J" : ".--- ",
	"K" : "-.- ",
	"L" : ".-.. ",
	"M" : "-- ",
	"N" : "-. ",
	"O" : "--- ",
	"P" : ".--. ",
	"Q" : "--.- ",
	"R" : ".-. ",
	"S" : "... ",
	"T" : "- ",
	"U" : "..- ",
	"V" : "...- ",
	"W" : ".-- ",
	"X" : "-..- ",
	"Y" : "-.-- ",
	"Z" : "--.. ",
	"0" : "----- ",
	"1" : ".---- ",
	"2" : "..--- ",
	"3" : "...-- ",
	"4" : "....- ",
	"5" : "..... ",
	"6" : "-.... ",
	"7" : "--... ",
	"8" : "---.. ",
	"9" : "----. "
}

def	main():
	args = sys.argv[1:]
	if len(args) != 1:
		print("AssertionError: Invalid number of arguments")
		return
	characters = args[0]
	morse = ""

	for c in characters:
		if c.upper() in NESTED_MORSE.keys():
			morse += NESTED_MORSE[c.upper()]
		else:
			print("AssertionError: Invalid character")
			return
	print(morse)

if __name__ == "__main__":
	main()
