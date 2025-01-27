# File Locator Script

This Python script scans a specified directory input by the user (or the current working directory by default) and lists all files within it and its subdirectories (ignoring hidden files). It outputs each file's path and size.

## Features

- **Recursive Directory Traversal**: The script explores the specified directory and all its subdirectories.
- **File Filtering**: Hidden files (starting with `.`) are ignored.
- **Output Format**: The script generates a list of dictionaries containing:
  - `File`: The full path to the file.
  - `Size`: The size of the file in B, KB, MB, GB, TB.

## Requirements

- Python 3.x

## How to Use

1. **Clone or Download**: Save the script to your local machine.
2. **Run the Script**: Open a terminal or command prompt, navigate to the script's location, and run it using Python:

   ```bash
   python locate-file-script.py

3. **Prompt**: You will be prompted to enter the search directory path. If any path provided, the current working directory will be scaned by default.

## Function Parameters

```python
locate_file(cwd=None)
```

- cwd: Directory to search (default: current directory)

## Example Output

```text
{
    "File": "/path/to/file1.txt",
    "Size": "1.00 KB"
}
{
    "File": "/path/to/file2.png",
    "Size": "2.34 MB"
}
```
