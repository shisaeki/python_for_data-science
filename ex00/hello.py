# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/21 12:15:14 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/21 12:15:16 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list  = ["Hello", "tata!"]
ft_tuple = ("Hello", "Japan!")
ft_set   = {"Hello", "Tokyo!"}
ft_dict  = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"
ft_dict["Hello"] = "42Tokyo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)