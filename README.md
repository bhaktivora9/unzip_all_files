# unzip_all_files
This Python script is designed to unzip files from a specified directory. It searches for ZIP files in the given directory and extracts their contents into respective separate directories.
## Requirements
- Python 3.x
- `zipfile` module (built-in)
- `os` module (built-in)

## Usage
1. Save the `unzip_files.py` script to your desired location.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script by executing the command:
    ```
    python unzip_files.py
    ```
5. Enter the full path to the directory containing the ZIP files when prompted.
6. Press Enter to start the extraction process.
7. The script will create a new directory for each ZIP file and extract its contents into that directory.

## Example
Suppose you have a directory named `zip_files` containing the following files:
- `file1.zip`
- `file2.zip`

Running the script and providing the path to the `zip_files` directory will result in the following directory structure:
