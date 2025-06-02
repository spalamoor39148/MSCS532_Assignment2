import random
import time
import tracemalloc
import matplotlib.pyplot as plt

def quick_sort(arr):
    """
    Implementation of the Quick Sort algorithm.
    arr: input list to be sorted
    returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr  # if the array has 0 or 1 element, it's already sorted
    pivot = arr[len(arr) // 2]  # Choose pivot as the middle element
    left = [x for x in arr if x < pivot]  # Elements that are smaller than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot] # Elements that are greater than pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursive calls

def merge_sort(arr):
    """
    Implementation of the Merge Sort algorithm.
    arr: input list to be sorted
    returns a new sorted list.
    """
    if len(arr) <= 1:
        return arr  # if the array has 0 or 1 element, it's already sorted
    mid = len(arr) // 2  # Find the middle index
    left = arr[:mid]  # Left half of array
    right = arr[mid:]  # Right half of array
    left = merge_sort(left)  # Sort the left half recursively
    right = merge_sort(right)  # Sort the right half recursively
    return merge(left, right)  # Merging the sorted halves

def merge(left, right):
    """
    Merges two sorted lists.
    left: The first sorted list.
    right: The second sorted list.
    returns a new merged list.
    """
    merged = []  # Initialize the merged list
    left_idx = 0  # Index for the left list
    right_idx = 0  # Index for the right list
    while left_idx < len(left) and right_idx < len(right):  # While both lists have elements
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])  # Append smaller element to merged
            left_idx += 1  # Move to the next element in left list
        else:
            merged.append(right[right_idx])
            right_idx += 1  # Move to the next element in right list
    merged.extend(left[left_idx:])  # Add any remaining elements from left list
    merged.extend(right[right_idx:])  # Add any remaining elements from right list
    return merged

# --- Generate Test Data ---

def generate_data(size, data_type="random"):
    """
    Generates test data.
    """
    if data_type == "sorted":
        return list(range(size))  # Sorted data
    elif data_type == "reverse":
        return list(range(size, 0, -1))  # Reverse sorted data
    else:  # "random"
        return [random.randint(0, size) for _ in range(size)]  # Random data

def measure_performance(algorithm, data):
    """
    Measures the execution time and memory usage of a given algorithm.
    Returns a tuple containing execution time (seconds) and memory usage (KB).
    """
    tracemalloc.start()  # Start memory tracing
    start_time = time.perf_counter()  # Get start time
    algorithm(data.copy())  # Run algorithm and sort on a copy
    end_time = time.perf_counter()  # Get end time
    _, peak_memory = tracemalloc.get_traced_memory()  # Get peak memory usage
    tracemalloc.stop()  # Stop memory tracing
    execution_time = end_time - start_time  # Calculate execution time
    return execution_time, peak_memory / 1024  # Memory in KB

# Define input list sizes and data types
sizes = [100, 1000, 5000, 10000, 50000]  # Test with different sizes
data_types = ["sorted", "reverse", "random"]  # Test with different data types
results = {}  # Dictionary to store the results

# Loop through different input list sizes and data types
for size in sizes:
    results[size] = {}  # Create a dictionary to hold the results for this size
    for data_type in data_types:
        results[size][data_type] = {}  # Create a dictionary to hold results for this data type
        data = generate_data(size, data_type)  # Generate data

        # Test Quick Sort
        time_quick, memory_quick = measure_performance(quick_sort, data)  # Test Quick Sort
        results[size][data_type]["quick"] = {"time": time_quick, "memory": memory_quick} # Store Quick Sort result

        # Test Merge Sort
        time_merge, memory_merge = measure_performance(merge_sort, data)  # Test Merge Sort
        results[size][data_type]["merge"] = {"time": time_merge, "memory": memory_merge} # Store Merge Sort result


# Print Results
print("Performance Results:")
for size in sizes:
    print(f"Size: {size}")
    for data_type in data_types:
        print(f"  Data Type: {data_type}")
        print(f"    Quick Sort: Time={results[size][data_type]['quick']['time']:.6f}s, Memory={results[size][data_type]['quick']['memory']:.2f} KB")
        print(f"    Merge Sort: Time={results[size][data_type]['merge']['time']:.6f}s, Memory={results[size][data_type]['merge']['memory']:.2f} KB")


# Create plots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))  # Create a 2x3 grid of subplots
axs = axs.flatten()

for i, data_type in enumerate(data_types):
    times_quick = [results[size][data_type]["quick"]["time"] for size in sizes]
    mems_quick = [results[size][data_type]["quick"]["memory"] for size in sizes]
    times_merge = [results[size][data_type]["merge"]["time"] for size in sizes]
    mems_merge = [results[size][data_type]["merge"]["memory"] for size in sizes]

    # Plot time
    axs[i].plot(sizes, times_quick, label="Quick Sort")
    axs[i].plot(sizes, times_merge, label="Merge Sort")
    axs[i].set_title(f"Execution Time ({data_type} data)")
    axs[i].set_xlabel("Input Size")
    axs[i].set_ylabel("Time (seconds)")
    axs[i].legend()
    axs[i].grid(True)

    # Plot memory
    axs[i+3].plot(sizes, mems_quick, label="Quick Sort")
    axs[i+3].plot(sizes, mems_merge, label="Merge Sort")
    axs[i+3].set_title(f"Memory Usage ({data_type} data)")
    axs[i+3].set_xlabel("Input Size")
    axs[i+3].set_ylabel("Memory (KB)")
    axs[i+3].legend()
    axs[i+3].grid(True)

plt.tight_layout()
plt.show()
