def insertion_sort(A, n):
    """Sorts array A of length n using insertion sort algorithm"""
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A

# Test case
if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr, len(arr))
    print("Sorted array:", sorted_arr)

