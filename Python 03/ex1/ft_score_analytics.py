#!/usr/bin/env python3

import sys


def ft_score_analytics() -> None:
    argv: list[str] = sys.argv[1:]
    argv_len: int = len(argv)

    if (argv_len < 1):
        print(
            ("No scores provided. Usage: "
             "python3 ft_score_analytics.py <score1> <score2> ...")
        )
        return

    try:
        scores: list[int] = []
        for arg in argv:
            try:
                n: int = int(arg)
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
            else:
                scores += [n]
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        if len(scores) > 0:
            print(f"Scores processed: {scores}")
            print(f"Total players: {argv_len}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / argv_len}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print(
                ("No scores provided. Usage: "
                 "python3 ft_score_analytics.py <score1> <score2> ...")
            )


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
