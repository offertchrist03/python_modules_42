#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 17:10:42 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 17:10:42 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_command_quest() -> None:
    total_len: int = len(sys.argv)
    program_name: str = sys.argv[0]
    argv: list[str] = sys.argv[1:]
    argv_len: int = len(argv)

    if (argv_len < 1):
        print("No arguments provided!")
    print(f"Program name: {program_name}")

    if (argv_len > 0):
        print(f"Arguments received: {argv_len}")
        i: int = 0
        for arg in argv:
            i += 1
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {total_len}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
