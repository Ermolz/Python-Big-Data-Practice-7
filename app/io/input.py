import pandas as pd


def input_from_console():
    """
    Reads text input from the console.

    :return: User input as a string
    """
    return input("Enter some text: ")


def read_file_builtin(path):
    """
    Reads text from a file using built-in Python functions.

    :param path: Path to the file
    :return: File content as a string
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def read_file_pandas(path):
    """
    Reads data from a file using the pandas library.

    :param path: Path to the file (e.g., .csv or .xlsx)
    :return: File content as a DataFrame
    """
    return pd.read_csv(path)
