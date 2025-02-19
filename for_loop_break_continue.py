# Filename: for_loop_break_continue.py

# Step 1: Define a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Iterate over each number using a for loop
for num in numbers:
    
    # Step 3: Skip the number 3 using continue
    if num == 3:
        continue  # Skip the rest of this iteration if num is 3
    
    # Step 4: Exit the loop if the number is 7 using break
    if num == 7:
        break  # Exit the entire loop if num is 7
    
    # Step 5: Print the current number
    print(num)
