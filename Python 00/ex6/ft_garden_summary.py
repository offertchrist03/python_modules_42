# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:45 by mahendri            #+#    #+#            #
#   Updated: 2026/03/10 10:45:21 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_summary() -> None:
    garden_name: str = input("Enter garden name: ")
    plants_nbr: str = input("Enter number of plants: ")
    print(f"Garden: {garden_name}")
    print(f"Plants: {plants_nbr}")
    print("Status: Growing well!")
