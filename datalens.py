# datalens.py - Core Array & Collection Analytics Engine

def reverse_array(arr):
    """Reverses the order of an array/list."""
    # Using slicing or a two-pointer approach
    return arr[::-1]

def count_element(arr, target):
    """Counts the occurrences of a specific element in the array."""
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count

def find_maximum(arr):
    """Finds the maximum number in a set/list without using max()."""
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def remove_duplicates_ordered(arr):
    """Removes duplicates from an ordered array while maintaining order."""
    if not arr:
        return []
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result

def partition_array(arr, pivot):
    """Partitions an array into elements less than pivot and elements greater/equal."""
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x >= pivot]
    return {"left_partition": left, "right_partition": right}

def kth_smallest(arr, k):
    """Finds the K-th smallest element by sorting the array."""
    sorted_arr = sorted(arr)
    if k > 0 and k <= len(sorted_arr):
        return sorted_arr[k - 1]
    return "Invalid K index"

def time_tradeoff_demo():
    """Demonstrates time tradeoff between List search (O(n)) and Set search (O(1))."""
    import time
    
    # Create a large list and a large set
    large_list = list(range(1000000))
    large_set = set(range(1000000))
    target = 999999
    
    # Measure list lookup time
    start_time = time.time()
    _ = target in large_list
    list_time = time.time() - start_time
    
    # Measure set lookup time
    start_time = time.time()
    _ = target in large_set
    set_time = time.time() - start_time
    
    return {
        "list_lookup_time": f"{list_time:.6f} seconds",
        "set_lookup_time": f"{set_time:.6f} seconds"
    }
