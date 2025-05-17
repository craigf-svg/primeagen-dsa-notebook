def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

    return arr


def swap(arr: list[int], index1: int, index2: int) -> None:
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp
