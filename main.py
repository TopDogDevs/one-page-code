import os


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
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
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
