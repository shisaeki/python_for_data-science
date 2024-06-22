# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/22 22:18:02 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/22 22:47:35 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	args = sys.argv

	if len(args) > 2:
		print("AssertionError: More thab 1 argument provided")
		return
	else:
		try:
			number = int(args[1])
		except ValueError:
			print("ValueError: Argument is not a number")
			return

		if number % 2 == 0:
			print("I'm Even")
		else:
			print("I'm Odd")
	return

if __name__ == "__main__":
	main()