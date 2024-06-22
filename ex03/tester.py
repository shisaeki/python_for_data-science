# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tester.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/21 16:15:45 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/22 14:44:55 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from null_not_found import null_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

null_not_found(Nothing)
null_not_found(Garlic)
null_not_found(Zero)
null_not_found(Empty)
null_not_found(Fake)
print(null_not_found("Brian"))