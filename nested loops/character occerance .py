# Get input from the user

string_input = input("Enter a string: ")

target_char = input("Enter the character to count: ")

# Initialize variables

count = 0

i = 0

# Loop through the string using a while loop

while i < len(string_input):

    if string_input[i] == target_char:

        count = count + 1

    i = i + 1

# Print the result

print("Number of character occurrences:", count)