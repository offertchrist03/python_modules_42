# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:27 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:09:28 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total() -> None:
    harvest_total: int = 0
    harvest_total += int(input("Day 1 harvest: "))
    harvest_total += int(input("Day 2 harvest: "))
    harvest_total += int(input("Day 3 harvest: "))
    print(f"Total harvest: {harvest_total}")
