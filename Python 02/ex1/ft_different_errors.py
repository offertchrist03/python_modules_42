#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mahendri <mahendri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/02 11:30:26 by mahendri            #+#    #+#            #
#   Updated: 2026/03/02 11:30:26 by mahendri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations() -> None:
    number: float = 0
    string: str = "abc"
    dic: dict[str, str] = {"name": "koto"}

    print("Testing ValueError...")
    try:
        number = int(string)
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    except Exception:
        print("Error")

    print("")
    print("Testing ZeroDivisionError...")
    try:
        number = 125 / number
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    except Exception:
        print("Error")

    print("")
    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt", "r")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    except Exception:
        print("Error")

    print("")
    print("Testing KeyError...")
    try:
        string = dic["_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    except Exception:
        print("Error")

    print("")
    print("Testing multiple errors together...")
    try:
        number = int(string)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    except Exception:
        print("Error")
    print("All error types tested successfully!")


def test_garden_operations() -> None:
    print("=== Garden Error Types Demo ===")
    print("")

    garden_operations()


if __name__ == "__main__":
    test_garden_operations()
