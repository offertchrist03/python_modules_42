#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: str = "r",
        new_content: str = "") -> tuple[bool, str]:
    res: bool = False
    content: str = ""
    try:
        if action not in ("r", "w"):
            raise Exception("Error: Action must be 'r' or 'w'")

        if action == "r":
            with open(filename, "r") as file:
                content = file.read()

        elif action == "w":
            with open(filename, "w") as file:
                _ = file.write(new_content)
                content = "Content successfully written to file"
        res = True
    except Exception as err:
        content = str(err)
    return (res, content)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    test: tuple[bool, str] = secure_archive('/not/existing/file')
    print(test)

    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    test = secure_archive('/etc/shadow')
    print(test)

    print()
    print("Using 'secure_archive' to read from a regular file:")
    test = secure_archive('your_text.txt')
    print(test)

    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive('new.txt', 'w', test[1]))
