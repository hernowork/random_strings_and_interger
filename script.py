import random
import string

def generate_random_string(length=5):
    # Define the characters to choose from (letters and digits)
    characters = string.ascii_letters + string.digits
    # Randomly select characters from the defined set
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def write_multiple_lines_to_file(filename, num_lines):
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            random_string = generate_random_string()
            file.write(random_string + '\n')  # Write each string on a new line

# Specify the number of lines and the filename
num_lines = 10000
filename = 'random_strings.txt'

# Write 1000 random strings to the file
write_multiple_lines_to_file(filename, num_lines)

print(f"{num_lines} random strings have been written to '{filename}'.")