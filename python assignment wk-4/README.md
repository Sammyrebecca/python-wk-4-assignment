# File Read/Write Utility

This Python script (`file.py`) allows you to read the contents of a text file, convert all text to uppercase, and save the modified content to a new file prefixed with `modified_`.

## Features

- Prompts the user for the name of the file to read.
- Reads and displays the content of the specified file.
- Converts the content to uppercase.
- Writes the modified content to a new file named `modified_<original_filename>`.
- Handles errors such as file not found and permission issues.

## Usage

1. Make sure you have Python installed.
2. Place the script and the file you want to read in the same directory, or provide the full path to the file when prompted.
3. Run the script:

   ```
   python file.py
   ```

4. Enter the filename when prompted.

## Error Handling

- **File Not Found**: Displays an error if the specified file does not exist.
- **Permission Error**: Displays an error if you do not have permission to read the file.
- **Other Errors**: Any unexpected errors are caught and displayed.

## Example

```
Enter the name of the file to read: example.txt
✅ Successfully created 'modified_example.txt' with modified content!
```
