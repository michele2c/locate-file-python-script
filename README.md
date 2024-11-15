# File Locator

A Python script to find and print out files, their size, and the last modification date in a directory based on days old.

## Features

- Search files recursively in a specified directory
- Filter files by:
  - Minimum file size
  - Maximum file size
  - Last modification date
  - Hidden files (optional)
- Human-readable file size output
- Error handling for file access issues

## Requirements

- Python 3.x
- No external dependencies required

## Usage

### Command Line Interface

Run the script directly to use the interactive interface:

```python
python locate-file-function.py
```

You will be prompted to:

Enter the search directory path.

Specify the number of days to filter by (optional)

## Function Parameters

```python
locate_file(cwd=None, min_size=0, max_size=None, days_old=None, include_hidden=False)
```

- cwd: Directory to search (default: current directory)

- min_size: Minimum file size in bytes (default: 0)

- max_size: Maximum file size in bytes (default: None)

- days_old: Only include files modified within this many days (default: None)

- include_hidden: Whether to include hidden files (default: False)

Returns a list of dictionaries containing file information:

- File path

- File size

- Last modification date

## Error Handling

- The script handles:

- Invalid directory paths

- Permission errors

- Invalid date inputs

- File access errors

## Example Output

```text
File: /path/to/file/document.pdf
Size: 2 MB
Modified: 2023-12-01 14:30:45
```
