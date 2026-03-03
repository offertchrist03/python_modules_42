# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 14:09:49 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 16:38:11 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed: str, number: int, size: str) -> None:
    end_paragraph: str = ""
    if (size == "packets"):
        end_paragraph = f"{number} packets available"
    elif (size == "grams"):
        end_paragraph = f"{number} grams total"
    elif (size == "area"):
        end_paragraph = f"cover {number} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed.capitalize()} seeds: {end_paragraph}")
