#Creates a new list with only even numbers
numbers = list(map(int, input("Enter numbers separated by a space.: ").split ()))

even_numbers = [num for num in numbers if num % 2 == 0]

print("New list:", even_numbers)
