digit_name = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

phone_number = input()

# Each number entered is like this '0', '1', 2' etc.,
# Each can be iterated over (as we prove, in the print statement, by looping over each
# And printing the word for them each time
# So an example entry would be read by the program as: '0' '4' '4' '9' '8' '9'

for digit in phone_number:
    # Print the digit_name from the list
    print(digit_name[int(digit)])  # Using the digit entered as the list index

