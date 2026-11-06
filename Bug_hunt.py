count = 1
total = 0

# BUG: Missing colon at the end of the while loop statement. Added ':' to fix syntax.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Tried to concatenate a string and an integer directly. Wrapped total in str().
# BUG: The loop condition only went up to count < 5 (stopping at 4). Changed to <= 5 to include 5.
print("Sum of 1 to 5 is: " + str(total))