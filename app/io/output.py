def print_to_console(text):
    """
    Prints the given text to the console.

    :param text: The text to be printed
    """
    print(text)


def write_to_file(path, text):
    """
    Writes the given text to a file using built-in Python features.

    :param path: Path to the file
    :param text: The text to be written
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)
