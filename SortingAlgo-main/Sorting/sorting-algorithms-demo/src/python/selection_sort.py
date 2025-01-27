def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(sample_array)
    print("Sorted array:", sorted_array)