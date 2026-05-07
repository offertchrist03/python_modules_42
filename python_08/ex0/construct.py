#!/usr/bin/env python3

import sys
import os
import site


def venv_check() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    return False


def venv_info(is_virtual: bool) -> None:
    if not is_virtual:
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        print(f"Environment Path: {sys.prefix}")
        print("")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        print()
        print("Package installation path:")

        try:
            package_paths: list[str] = site.getsitepackages()
            for path in package_paths:
                print(path)
        except Exception:
            print("[ERROR]")


if __name__ == "__main__":
    is_virtual: bool = venv_check()

    print("MATRIX STATUS: ", end="")
    print('You\'re still plugged in'
          if not is_virtual
          else 'Welcome to the construct')

    try:
        python_path: str = (os.popen("which python")).read()
    except Exception:
        python_path = "[ERROR]"
    print(f"Current Python: {python_path}")

    if not is_virtual:
        venv: str = "None detected"
    else:
        try:
            lst_temp = sys.prefix.split("/")
            venv = lst_temp[len(lst_temp) - 1]
        except Exception:
            venv = "[ERROR]"
    print(f"Virtual Environment: {venv}")

    venv_info(is_virtual)
