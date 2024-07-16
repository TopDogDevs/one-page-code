import os

def should_exclude(path):
    # List of directories and files to exclude
    exclude_dirs = [
        'node_modules',
        '.git',
        '__pycache__',
        'venv',
        'env',
        'build',
        'dist',
        '.vscode',
        '.idea',
        'logs'
    ]
    exclude_files = [
        '.env',
        '.gitignore',
        '.DS_Store',
        'Thumbs.db',
        'package-lock.json',
        'data.json'
    ]
    
    # Check if the path contains any of the excluded directories
    if any(excluded_dir in path.split(os.sep) for excluded_dir in exclude_dirs):
        return True
    
    # Check if the file is in the exclude list
    if os.path.basename(path) in exclude_files:
        return True
    
    return False

def get_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def main():
    # Step 1: Ask for the folder path
    folder_path = input("Enter the folder path: ").strip()

    # Step 2: Ask for file extensions to include
    extensions = input("Enter file extensions to include (comma-separated, e.g., .txt,.py,.md): ").strip()
    extensions = [ext.strip() for ext in extensions.split(',')]

    # Step 3: Create content file
    output_file = "combined_content.txt"

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(folder_path):
            # Remove excluded directories
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
            
            for file in files:
                file_path = os.path.join(root, file)
                if should_exclude(file_path):
                    continue
                
                if any(file.endswith(ext) for ext in extensions):
                    relative_path = os.path.relpath(file_path, folder_path)

                    outfile.write(f"File: {relative_path}\n")
                    outfile.write("=" * 50 + "\n")

                    try:
                        content = get_file_content(file_path)
                        outfile.write(content)
                    except Exception as e:
                        outfile.write(f"Error reading file: {str(e)}\n")

                    outfile.write("\n" + "=" * 50 + "\n\n")

    print(f"Combined content has been written to {output_file}")

if __name__ == "__main__":
    main()
