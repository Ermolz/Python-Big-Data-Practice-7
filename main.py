from app.io.input import input_from_console, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file


def main():
    # 1. Get input from the console
    user_input = input_from_console()
    print_to_console(user_input)
    write_to_file("output_console.txt", user_input)

    # 2. Read from file using built-in methods
    builtin_text = read_file_builtin("data/sample.txt")
    print_to_console(builtin_text)
    write_to_file("output_builtin.txt", builtin_text)

    # 3. Read from file using pandas
    pandas_data = read_file_pandas("data/sample.csv")
    print_to_console(str(pandas_data))
    write_to_file("output_pandas.txt", str(pandas_data))

if __name__ == "__main__":
    main()