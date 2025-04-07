#QUESTION 1:
def read_and_write_file(input_file, output_file):
    try:
      
        with open(input_file, 'r') as infile:
            data = infile.read()
        
        modified_data = data.upper()

        with open(output_file, 'w') as outfile:
            outfile.write(modified_data)

        print(f"Data successfully written to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
    except IOError:
        print("An error occurred while reading or writing the file.")

input_file = 'input.txt' 
output_file = 'output.txt' 
read_and_write_file(input_file, output_file)

# QUESTION 2:
def user_file_input():
    filename = input("Please enter the filename: ")

    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(f"File content:\n{data}")

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} cannot be read.")


user_file_input()
