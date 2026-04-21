# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:34 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 14:09:34 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    days: int = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
