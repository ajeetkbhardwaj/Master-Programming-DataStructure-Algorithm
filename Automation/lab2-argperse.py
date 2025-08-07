"""
argperse: Parser for command-line options, arguments and subcommands
It's used to write user-friendly command-line interfaces.
what arguments it requires, and argparse will figure out how to parse those out of sys.argv. 
It automatically generates help and usage messages and also figure out issue errors when users give the program invalid arguments

To list files in a directory:

python file_manager.py list /path/to/directory
To read a file:

python file_manager.py read /path/to/file
To write to a file:

python file_manager.py write /path/to/file "This is some content"
To delete a file after reading:

python file_manager.py read /path/to/file --delete
For verbose output (e.g., for listing files):

python file_manager.py list /path/to/directory --verbose

"""

import argparse
import os

# Function to list files in a directory
def list_files(directory, verbose=False):
    try:
        files = os.listdir(directory)
        if verbose:
            print(f"Listing files in {directory}:")
            for file in files:
                print(f" - {file}")
        else:
            print("\n".join(files))
    except FileNotFoundError:
        print(f"Error: The directory {directory} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access {directory}.")

# Function to read a file
def read_file(file):
    try:
        with open(file, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: The file {file} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read {file}.")

# Function to write to a file
def write_file(file, content):
    try:
        with open(file, 'w') as f:
            f.write(content)
        print(f"Content written to {file}.")
    except PermissionError:
        print(f"Error: Permission denied to write to {file}.")

# Function to delete a file
def delete_file(file):
    try:
        os.remove(file)
        print(f"File {file} deleted.")
    except FileNotFoundError:
        print(f"Error: The file {file} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to delete {file}.")

# Main function that parses arguments
def main():
    parser = argparse.ArgumentParser(description="File management tool")
    
    # Adding positional argument for the file/directory
    parser.add_argument("target", help="File or directory to operate on")
    
    # Adding optional arguments
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-d", "--delete", action="store_true", help="Delete the file after reading")
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command")
    
    # Subcommand to list files
    list_parser = subparsers.add_parser("list", help="List files in the directory")
    list_parser.add_argument("directory", help="Directory to list files from")
    
    # Subcommand to read a file
    read_parser = subparsers.add_parser("read", help="Read the content of a file")
    
    # Subcommand to write to a file
    write_parser = subparsers.add_parser("write", help="Write content to a file")
    write_parser.add_argument("content", help="Content to write to the file")
    
    # Subcommand to delete a file
    delete_parser = subparsers.add_parser("delete", help="Delete a file")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Handle commands
    if args.command == "list":
        list_files(args.directory, verbose=args.verbose)
    elif args.command == "read":
        read_file(args.target)
        if args.delete:
            delete_file(args.target)
    elif args.command == "write":
        write_file(args.target, args.content)
    elif args.command == "delete":
        delete_file(args.target)

# Run the main function
if __name__ == "__main__":
    main()
