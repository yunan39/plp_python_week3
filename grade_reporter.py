scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

for score in scores:
    # Add to total score for later average calculation
    total_score += score
    
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Print each score with its grade
    print(f"Score: {score} - Grade: {grade}")
    
    # Count passes (50 or more) and fails (below 50)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# Calculate the average and round to one decimal place
average_score = round(total_score / len(scores), 1)

# Print final summary statistics
print("\n--- Summary ---")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average: {average_score}")