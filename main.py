import numpy as np
import data_gen, implementations, misc

# =============================================================================
#                           Benchmark Functions
# =============================================================================

def mark_random(num_entries):
    data = data_gen.generate_random_data(num_entries)
    print(f"\n==========Random data==========")
    return data
        
def mark_partially_sorted(num_entries):
    data = data_gen.generate_partially_sorted_data(num_entries)
    print(f"\n==========Partially sorted data==========")
    return data

def mark_reverse_sorted(num_entries):
    data = data_gen.generate_reverse_sorted_data(num_entries)
    print(f"\n==========Reverse sorted data==========")
    return data

def mark_sorted(num_entries):
    data = data_gen.generate_sorted_data(num_entries)
    print(f"\n==========Sorted data==========")
    return data

# =============================================================================
#                                    Main
# =============================================================================

def main():
    num_entries = 10000
    num_cycles = 5

    data = mark_reverse_sorted(num_entries)
    print(f"Number of entries: {num_entries}")
    print(f"Number of cycles: {num_cycles}")

    bubble_sort_times = []
    quick_sort_times = []
    selection_sort_times = []

    for _ in range(num_cycles):
        bubble_sort_time = implementations.bubble_sort(data)[1]
        quick_sort_time = implementations.quick_sort(data)[1]
        selection_sort_time = implementations.selection_sort(data)[1]

        bubble_sort_times.append(bubble_sort_time)
        quick_sort_times.append(quick_sort_time)
        selection_sort_times.append(selection_sort_time)

    bubble_sort_mean = np.mean(bubble_sort_times)
    quick_sort_mean = np.mean(quick_sort_times)
    selection_sort_mean = np.mean(selection_sort_times)

    bubble_sort_stddev = np.std(bubble_sort_times)
    quick_sort_stddev = np.std(quick_sort_times)
    selection_sort_stddev = np.std(selection_sort_times)

    print("\n==========Results==========")
    print(f"Bubble Sort: {misc.convert_to_ms(bubble_sort_mean)}ms +/- {misc.convert_to_ms(bubble_sort_stddev)}ms")
    print(f"Quick Sort: {misc.convert_to_ms(quick_sort_mean)}ms +/- {misc.convert_to_ms(quick_sort_stddev)}ms")
    print(f"Selection Sort: {misc.convert_to_ms(selection_sort_mean)}ms +/- {misc.convert_to_ms(selection_sort_stddev)}ms")

main()