# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    null_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/21 12:43:04 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/22 14:46:22 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def null_not_found(object: any) -> int:
	if object == None:
		print(f"Nothing : None {type(object)}")
		return (0)
	elif isinstance(object, float) and object != object:
		print(f"Cheese : nan {type(object)}")
		return (0)
	elif object == 0:
		print(f"Zero : 0 {type(object)}")
		return (0)
	elif object == "":
		print(f"Empty :   {type(object)}")
		return (0)
	elif object == False:
		print(f"Fake : False {type(object)}")
		return (0)
	else:
		print("Type not found")
		return (1)