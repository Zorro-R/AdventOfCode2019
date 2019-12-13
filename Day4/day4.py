password_range = range(183564, 657474 + 1)  # Puzzle input

# Assume all passwords fit the criteria
passwords = [num for num in password_range]

#passwords = [123789]
#passwords = [111111, 223450, 123789]
not_passwords = []  # list of passwords that do not fit criteria
for num in passwords:

    # Two adjacent digits must be the same
    # Assume the number does not have equal adjacent digits
    equal_adjacent_digits = False
    for i in range(len(str(num)) - 1):
        # Stored as string in order to be able to index
        adjacent_digits = str(num)[i:i+2]
        if adjacent_digits[0] == adjacent_digits[1]:
            equal_adjacent_digits = True
            break
    # If no adjacent digits are equal add password to list of incorrect passwords
    if not equal_adjacent_digits:
        not_passwords.append(num)
        continue  # Move on to check next number

    # Digits must be in increasing order
    # Assume digits are in increasing order
    digits_in_increasing_order = True
    for i in range(len(str(num)) - 1):
        current_digit = str(num)[i]
        trailing_digits = str(num)[i+1:]

        # If trailing digit is greater than current digit
        for trailing_digit in trailing_digits:
            if trailing_digit < current_digit:
                digits_in_increasing_order = False
                break

        # Break out of for loop if it is already known that any of the digits are not in increasing order
        if not digits_in_increasing_order:
            break

    # Add password to list of incorrect passwords if digits are not in increasing order
    if not digits_in_increasing_order:
        not_passwords.append(num)

potential_passwords = [x for x in passwords if x not in not_passwords]
print(len(potential_passwords))  # Solution to part 1

#potential_passwords = [112233, 123444, 111122]
new_not_passwords = []
# Solution for part 2
for password in potential_passwords:
    list_of_adjacent_equals = []
    for i in range(len(str(password)) - 1):
        # Stored as string in order to be able to index
        adjacent_digits = str(password)[i:i+2]
        if adjacent_digits[0] == adjacent_digits[1]:
            list_of_adjacent_equals.append(
                (adjacent_digits[0], adjacent_digits[1]))

    print(list_of_adjacent_equals)
    # if there are repeated adjacent digits and one "double" occurs only once
    if len(set(list_of_adjacent_equals)) < len(list_of_adjacent_equals) and not 1 in [list_of_adjacent_equals.count(x) for x in set(list_of_adjacent_equals)]:
        new_not_passwords.append(password)

# Solution to part 2
print(len([password for password in potential_passwords if password not in new_not_passwords]))
