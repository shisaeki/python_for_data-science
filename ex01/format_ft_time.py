# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shinsaeki <shinsaeki@student.42.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/21 12:15:22 by shinsaeki         #+#    #+#              #
#    Updated: 2024/06/21 12:15:24 by shinsaeki        ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime

elapsed_time = time.time()
current_time = datetime.now()
print(f"Seconds since January 1, 1970: {elapsed_time:,.4f} or {elapsed_time:.2e} in scientific notation")
print(f"{current_time.strftime('%b %d %Y')}")
