# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:39 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:09:39 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative() -> None:
    i: int = 0
    harvest_day: int = int(input("Days until harvest: "))
    for i in range(harvest_day):
        print(f"Day {i + 1}")
        i += 1
    print("Harvest time!")
