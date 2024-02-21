# uNameGen

uNameGen is a Python tool for generating usernames from a list of names provided in a text file. It also offers the option to save the generated usernames along with their corresponding CamelCase names and full names into another text file.

## Usage

1. **Clone the Repository**: Clone the uNameGen repository to your local machine.

    ```bash
    git clone https://github.com/username/uNameGen.git
    ```

2. **Navigate to the Directory**: Navigate to the uNameGen directory.

    ```bash
    cd uNameGen
    ```

3. **Run the Script**: Execute the script `script.py` providing the path of the text file containing the names using the `-n` or `--file_name` flag. Optionally, you can specify the output file name using the `-o` or `--output_file` flag. You can also enable verbose mode to display the generated names in the console using the `-v` or `--verbose` flag.

    ```bash
    python script.py -n names.txt -o output.txt -v
    ```

    - `-n`, `--file_name`: Path of the text file containing the names.
    - `-o`, `--output_file`: Output file name (default: wordlist.txt).
    - `-v`, `--verbose`: Display generated names in console (optional).

4. **Check Output**: Check the specified output file to find the generated usernames along with their CamelCase equivalents and full names.

## Example

Suppose you have a text file named `names.txt` containing the following names:
  John Doe
  Alice Smith
  ```bash
  python script.py -n names.txt -o output.txt -v
  ```
Will generate the usernames and display them in the console (if verbose mode is enabled), and save them to output.txt.
