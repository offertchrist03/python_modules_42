#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/03 13:00:43 by mahendri            #+#    #+#            #
#   Updated: 2026/03/03 13:00:43 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def ft_score_analytics() -> None:
    argv: list[str] = sys.argv[1:]
    argv_len: int = len(argv)

    if (argv_len < 1):
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        scores: list[int] = [0] * argv_len
        i: int = 0
        for arg in argv:
            n: int = int(arg)
            scores[i] = n
            i += 1
    except ValueError:
        print(f"ValueError: '{arg}' is non-numeric value")
    except Exception:
        print(f"Exception Error: {arg}")
    else:
        print(f"Scores processed: {argv}")
        print(f"Total players: {argv_len}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / argv_len}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
