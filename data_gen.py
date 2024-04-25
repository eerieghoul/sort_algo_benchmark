import random 

# =============================================================================
#                               Data Generation
# =============================================================================

def generate_random_data(num_entries):
    return [random.randint(0, num_entries) for _ in range(num_entries)]

def generate_partially_sorted_data(num_entries):
    data = list(range(num_entries))
    random.shuffle(data)
    return data

def generate_reverse_sorted_data(num_entries):
    return list(range(num_entries, 0, -1))

def generate_sorted_data(num_entries):
    return list(range(num_entries))