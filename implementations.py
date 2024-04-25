import time

# =============================================================================
#                           Algorithm Implementations
# =============================================================================

def bubble_sort(data):
    start_time = time.time()

    num_elements = len(data)
    for i in range(num_elements):
        for j in range(0, num_elements-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    end_time = time.time()
    return data, end_time - start_time

def quick_sort(data):
    start_time = time.time()

    def quick_sort_recursive(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

    result = quick_sort_recursive(data)
    end_time = time.time()
    return result, end_time - start_time

def selection_sort(data):
    start_time = time.time()

    num_elements = len(data)
    for i in range(num_elements):
        min_idx = i
        for j in range(i+1, num_elements):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]

    end_time = time.time()
    return data, end_time - start_time