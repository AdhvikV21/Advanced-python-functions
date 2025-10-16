number_input = input("Enter a number: ")
limit = int(number_input)
odd_numbers_list = [x for x in range(1, limit) if x%2!= 0]
print(f"Odd numbers under {limit}: {odd_numbers_list}")

fruits = ["apple", "banana", "cherry", "date"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(f"Original list of fruits: {fruits}")
print(f"Capitalized list of fruits: {capitalized_fruits}")