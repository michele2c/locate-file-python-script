# File Locator

A Python utility for finding files in a directory based on size and modification date criteria.

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

### As a Module

```python
from locate_file_function import locate_file, format_size

# Find files modified in the last 7 days, between 1KB and 100MB
files = locate_file(
    cwd="/path/to/search",
    min_size=1024,          # 1KB
    max_size=104857600,     # 100MB
    days_old=7,
    include_hidden=False
)

for file in files:
    print(f"File: {file['File']}")
    print(f"Size: {format_size(file['Size'])}")
    print(f"Modified: {file['Last Modified']}")

