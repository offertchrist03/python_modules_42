# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:42 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:09:42 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def recursion(i: int, limit: int) -> None:
    if (i < limit):
        print(f"Day {i + 1}")
        return recursion(i + 1, limit)
    print("Harvest time!")
    return


def ft_count_harvest_recursive() -> None:
    i: int = 0
    harvest_day: int = int(input("Days until harvest: "))
    recursion(i, harvest_day)
