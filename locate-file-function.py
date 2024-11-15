import os
from datetime import datetime, timedelta

import math

def locate_file(cwd=None, min_size=0, max_size=None, days_old=None, include_hidden=False):
    """
    Locate files with size and date filtering, excluding hidden files
    
    Parameters:
    - cwd: Directory to search (default: current directory)
    - min_size: Minimum file size in bytes (default: 0)
    - max_size: Maximum file size in bytes (default: None)
    - days_old: Only include files modified within this many days (default: None)
    - include_hidden: Whether to include hidden files (default: False)
    """
    if cwd is None:
        cwd = os.getcwd()
        
    file_dic = []
    current_time = datetime.now()
    
    for folder, _, files in os.walk(cwd):
        for file in files:
            # Skip hidden files (starting with .)
            if not include_hidden and (file.startswith('.') or '/.' in folder):
                continue
                
            file_path = os.path.join(folder, file)
            
            try:
                # Get file stats
                file_stats = os.stat(file_path)
                file_size = file_stats.st_size
                modified_time = datetime.fromtimestamp(file_stats.st_mtime)
                
                # Check if file meets all criteria
                size_ok = (file_size >= min_size) and (max_size is None or file_size <= max_size)
                date_ok = (days_old is None or 
                          (current_time - modified_time) <= timedelta(days=days_old))
                
                if size_ok and date_ok:
                    file_info = {
                        'File': file_path,
                        'Size': file_size,
                        'Last Modified': modified_time.strftime('%Y-%m-%d %H:%M:%S')
                    }
                    file_dic.append(file_info)
                    
            except (OSError, PermissionError) as e:
                print(f"Error accessing {file_path}: {e}")
                continue
    
    return file_dic

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{math.ceil(size_bytes)} {unit}"
        size_bytes /= 1024
    return f"{math.ceil(size_bytes)} TB"

# Example usage
if __name__ == "__main__":
    try:
        user_input = input("Enter the path: ")
        days_old_input = input("Enter the number of days old (or press Enter to skip): ")
        
        # Convert and validate user input
        days_old = None
        if days_old_input.strip():
            try:
                days_old = int(days_old_input)
                if days_old < 0:
                    raise ValueError("Days must be a positive number")
            except ValueError:
                print("Invalid days input, using no date filter")
                days_old = None
        
        response = locate_file(
            user_input,
            min_size=1024,  # 1KB minimum
            max_size=1024 * 1024 * 100,  # 100MB maximum
            days_old=days_old,
            include_hidden=False
        )
        
        if not response:
            print("No files found matching the criteria")
        else:
            for item in response:
                print(f"\nFile: {item['File']}")
                print(f"Size: {format_size(item['Size'])}")
                print(f"Modified: {item['Last Modified']}")
                
    except Exception as e:
        print(f"Error running the script: {e}")