# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/21 12:15:26 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/21 12:39:36 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	if type(object) == list:
		print(f"List : {type(object)}")
	elif type(object) == tuple:
		print(f"Tuple : {type(object)}")
	elif type(object) == set:
		print(f"Set : {type(object)}")
	elif type(object) == dict:
		print(f"Dict : {type(object)}")
	elif type(object) == str:
		print(f"{object} is in the kitchen : {type(object)}")
	else:
		print("Type not found")
	return (42)