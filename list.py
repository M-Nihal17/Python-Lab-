
numbers = list(map(int, input("Enter elements: ").split()))
print("List:", numbers)

key = int(input("\nEnter element to search: "))

if key in numbers:
    print("Element found at index:", numbers.index(key))
else:
    print("Element not found")

pos = int(input("\nEnter position (index): "))
new_val = int(input("Enter new value: "))

if 0 <= pos < len(numbers):
    numbers[pos] = new_val
    print("Updated List:", numbers)
else:
    print("Invalid position")

even_numbers = [x for x in numbers if x % 2 == 0]
print("\nEven Numbers:", even_numbers)

print("\nLength of list:", len(numbers))
numbers.sort()
print("\nSorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)