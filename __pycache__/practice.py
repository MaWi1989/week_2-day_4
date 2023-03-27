# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

a = [1, 3, 5 ,6 ,8 ,3]
b = [1, 4, 6, 8, 4]

def subtracted_list(arr1, arr2):
    """Subtract list b from list a, return a new list only with items that do not exist in list a."""
    new_arr = []
    for num in arr1:
        if num not in arr2:
            new_arr.append(num)
    return new_arr

print(subtracted_list(a,b))
        


# Find Even numbers
# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.

# Example:
input= [2, 7, 10, 11, 12]
output= [2, 10, 12]

def even_nums(arr):
    """Return a list of even numbers."""
    evens = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(even_nums(input))



# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print 'Fizz' instead of the number
# If the number is divisible 5, print 'Buzz' instead of the number
# If the number is divisible by both 3 and 5, print 'FizzBuzz' instead of the number
# Otherwise, simply print the number

def fizz_buzz(arr):
    for num in arr:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz(range(1,16))    
