# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:31 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:09:31 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age() -> None:
    days: int = int(input("Enter plant age in days: "))
    if (days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
