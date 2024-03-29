def find_largest(numbers):
    # Start with the first number as the largest
    largest = numbers[0]
    
    # Loop through the rest of the numbers
    for num in numbers[1:]:
        # Compare each number with the largest so far
        if num > largest:
            # If the number is greater, update the largest
            largest = num
            
    return largest

def find_smallest(numbers):
    # Start with the first number as the smallest
    smallest = numbers[0]
    
    # Loop through the rest of the numbers
    for num in numbers[1:]:
        # Compare each number with the smallest so far
        if num < smallest:
            # If the number is smaller, update the smallest
            smallest = num
            
    return smallest

numbers = [34, 23, 56, 12, 89, 76, 45, 90, 21, 67]

largest = find_largest(numbers)
print("The largest number is:", largest)

smallest = find_smallest(numbers)
print("The smallest number is:", smallest)
