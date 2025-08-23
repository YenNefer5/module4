
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for number in range(0, n - i - 1):
            if arr[number] > arr[number + 1]:
                arr[number], arr[number + 1] = arr[number + 1],  arr[number]


my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)