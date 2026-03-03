#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 11:30:39 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 11:30:39 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def check_temperature(temp_str) -> str:
    nbr: str = ""
    if (temp_str.startswith("-")):
        nbr = temp_str[1:]
    else:
        nbr = temp_str
    if (nbr.isdigit()):
        temp: int = int(temp_str)
        if (temp < 0):
            return (f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        elif (temp > 40):
            return (f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        return (f"Temperature {temp_str}°C is perfect for plants!")
    else:
        return (f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    while 1:
        temp_str = input(">> Input temperature: ")
        if (temp_str.lower() == "q" or temp_str.lower() == "quit"):
            break
        print(f"Testing temperature: {temp_str}")
        print(check_temperature(temp_str))
        print("")


if __name__ == "__main__":
    test_temperature_input()
