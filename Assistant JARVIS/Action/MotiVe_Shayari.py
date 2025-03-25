# connect.py

def read_file(file_path):
    """Reads and returns the content of the file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(file_path, content):
    """Writes content to the file, overwriting any existing content."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def append_to_file(file_path, content):
    """Appends content to the file."""
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)

def main():
    file_path = 'J:\\Assistant JARVIS\\DATA\\Motivate_shayari.txt'
    
    try:
        # Reading from the file
        content = read_file(file_path)
        print("Current content of the file:")
        print(content)
        
        # Writing new content to the file
        new_content = "This is the new content to write to the file."
        write_to_file(file_path, new_content)
        print("\nNew content written to the file.")
        
        # Appending additional content to the file
        additional_content = "\nThis is additional content appended to the file."
        append_to_file(file_path, additional_content)
        print("\nAdditional content appended to the file.")
        
        # Reading again to see the updated content
        updated_content = read_file(file_path)
        print("\nUpdated content of the file:")
        print(updated_content)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
