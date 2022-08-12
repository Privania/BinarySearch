import  random
random.seed("Binary Search")

numbers = []

for _ in range(100):
    numbers.append(random.randint(0, 1000))
numbers.sort()

counter = 0


def binary_search (numbers_list, number, left, right):
    global counter
    counter = counter + 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if number == numbers_list[mid]:
        return mid

    elif number < numbers_list[mid]:
        return binary_search(numbers_list, number, left , mid - 1)
    else:
        return binary_search(numbers_list, number, mid+1, right)


print(numbers)
print(binary_search(numbers, 43, 0, len(numbers)-1))
print(counter)