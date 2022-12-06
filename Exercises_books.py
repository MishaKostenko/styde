def binary_search(list, item):

    low = 0
    high=len(list)-1

    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 2))


def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key_item
    print("The number of permutations is", count)


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
insertion_sort(library_num)
print("Sorted array:", library_num)