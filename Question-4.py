def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return None
file_content = read_file("aqq.txt")
if file_content is not None:
    print("File content:", file_content)


    #OUTPUT:- The file 'aqq.txt' does not exist.
