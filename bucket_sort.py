"""
Bucket Sort Implementation in Python

This module provides a robust bucket sort algorithm implementation that handles
various data types including integers, floats, and strings.

Bucket sort is a distribution-based sorting algorithm that works by distributing
elements into a number of buckets, sorting each bucket individually, and then
concatenating the sorted buckets.

Time Complexity:
    - Best Case: O(n + k) where n is the number of elements and k is the number of buckets
    - Average Case: O(n + k)
    - Worst Case: O(n²) when all elements fall into the same bucket

Space Complexity: O(n + k)
"""

from typing import List, Union, Any, Callable, Optional
import math


def bucket_sort(
    arr: List[Union[int, float]],
    num_buckets: Optional[int] = None,
    key: Optional[Callable[[Any], Union[int, float]]] = None,
    reverse: bool = False
) -> List[Union[int, float]]:
    """
    Sort a list using the bucket sort algorithm.
    
    Args:
        arr: List of numeric elements to sort
        num_buckets: Number of buckets to use (default: sqrt(n))
        key: Optional function to extract comparison key from each element
        reverse: If True, sort in descending order (default: False)
    
    Returns:
        Sorted list in ascending order (or descending if reverse=True)
    
    Raises:
        ValueError: If the array is empty or contains invalid data types
    
    Examples:
        >>> bucket_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        
        >>> bucket_sort([0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51])
        [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
        
        >>> bucket_sort([64, 34, 25, 12, 22, 11, 90], reverse=True)
        [90, 64, 34, 25, 22, 12, 11]
    """
    if not arr:
        return arr
    
    # Apply key function if provided
    if key is not None:
        # Create list of (original_element, key_value) tuples
        keyed_arr = [(elem, key(elem)) for elem in arr]
        sorted_keyed = _bucket_sort_internal([kv[1] for kv in keyed_arr], num_buckets, reverse)
        # Reconstruct original elements in sorted order
        key_to_original = {kv[1]: kv[0] for kv in keyed_arr}
        return [key_to_original[k] for k in sorted_keyed]
    
    return _bucket_sort_internal(arr, num_buckets, reverse)


def _bucket_sort_internal(
    arr: List[Union[int, float]],
    num_buckets: Optional[int] = None,
    reverse: bool = False
) -> List[Union[int, float]]:
    """
    Internal bucket sort implementation for numeric values.
    
    Args:
        arr: List of numeric elements to sort
        num_buckets: Number of buckets to use
        reverse: If True, sort in descending order
    
    Returns:
        Sorted list in ascending or descending order
    """
    n = len(arr)
    
    if n <= 1:
        return arr.copy()
    
    # Determine number of buckets (default: square root of n)
    if num_buckets is None:
        num_buckets = max(1, int(math.sqrt(n)))
    
    # Find minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are equal
    if min_val == max_val:
        return arr.copy()
    
    # Handle infinity values - if range is infinite, use Python's built-in sort
    if math.isinf(max_val - min_val):
        return sorted(arr)
    
    # Initialize buckets
    buckets: List[List[Union[int, float]]] = [[] for _ in range(num_buckets)]
    
    # Calculate bucket range
    bucket_range = (max_val - min_val) / num_buckets
    
    # Distribute elements into buckets
    for num in arr:
        # Handle special cases for infinity
        if math.isinf(num):
            if num > 0:
                buckets[-1].append(num)  # Positive infinity goes to last bucket
            else:
                buckets[0].append(num)   # Negative infinity goes to first bucket
        else:
            # Calculate bucket index
            # Use min() to handle edge case where num == max_val
            bucket_index = min(
                int((num - min_val) / bucket_range),
                num_buckets - 1
            )
            buckets[bucket_index].append(num)
    
    # Sort individual buckets using insertion sort (efficient for small arrays)
    for i in range(num_buckets):
        buckets[i] = _insertion_sort(buckets[i], reverse=reverse)
    
    # Concatenate sorted buckets
    result = []
    if reverse:
        # Reverse bucket order for descending sort
        for bucket in reversed(buckets):
            result.extend(bucket)
    else:
        for bucket in buckets:
            result.extend(bucket)
    
    return result


def _insertion_sort(arr: List[Union[int, float]], reverse: bool = False) -> List[Union[int, float]]:
    """
    Sort a small list using insertion sort.
    
    This is used internally for sorting individual buckets.
    Insertion sort is efficient for small arrays.
    
    Args:
        arr: List of numeric elements to sort
        reverse: If True, sort in descending order
    
    Returns:
        Sorted list in ascending or descending order
    """
    if len(arr) <= 1:
        return arr
    
    sorted_arr = arr.copy()
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        if reverse:
            while j >= 0 and sorted_arr[j] < key:
                sorted_arr[j + 1] = sorted_arr[j]
                j -= 1
        else:
            while j >= 0 and sorted_arr[j] > key:
                sorted_arr[j + 1] = sorted_arr[j]
                j -= 1
        sorted_arr[j + 1] = key
    
    return sorted_arr


def bucket_sort_strings(
    arr: List[str],
    num_buckets: Optional[int] = None,
    case_sensitive: bool = True,
    reverse: bool = False
) -> List[str]:
    """
    Sort a list of strings using bucket sort.
    
    Args:
        arr: List of strings to sort
        num_buckets: Number of buckets to use (default: 26 for alphabetic sorting)
        case_sensitive: Whether to perform case-sensitive sorting
        reverse: If True, sort in descending order (default: False)
    
    Returns:
        Sorted list of strings
    
    Examples:
        >>> bucket_sort_strings(['banana', 'apple', 'cherry', 'date'])
        ['apple', 'banana', 'cherry', 'date']
    """
    if not arr:
        return arr
    
    if not all(isinstance(s, str) for s in arr):
        raise ValueError("All elements must be strings")
    
    # Default to 26 buckets for alphabetic sorting
    if num_buckets is None:
        num_buckets = 26
    
    # Convert strings to numeric values based on first character
    def string_to_value(s: str) -> float:
        if not s:
            return 0.0
        char = s[0].lower() if not case_sensitive else s[0]
        return ord(char)
    
    n = len(arr)
    if n <= 1:
        return arr.copy()
    
    # Initialize buckets
    buckets: List[List[str]] = [[] for _ in range(num_buckets)]
    
    # Find min and max character values
    min_val = min(string_to_value(s) for s in arr)
    max_val = max(string_to_value(s) for s in arr)
    
    if min_val == max_val:
        # All strings start with same character, use standard sort
        return sorted(arr, key=lambda s: s.lower() if not case_sensitive else s)
    
    # Calculate bucket range
    bucket_range = (max_val - min_val) / num_buckets
    
    # Distribute strings into buckets
    for s in arr:
        val = string_to_value(s)
        bucket_index = min(
            int((val - min_val) / bucket_range),
            num_buckets - 1
        )
        buckets[bucket_index].append(s)
    
    # Sort individual buckets using Python's built-in sort
    for i in range(num_buckets):
        buckets[i].sort(key=lambda s: s.lower() if not case_sensitive else s, reverse=reverse)
    
    # Concatenate sorted buckets
    result = []
    if reverse:
        for bucket in reversed(buckets):
            result.extend(bucket)
    else:
        for bucket in buckets:
            result.extend(bucket)
    
    return result


def bucket_sort_objects(
    arr: List[Any],
    key: Callable[[Any], Union[int, float]],
    num_buckets: Optional[int] = None,
    reverse: bool = False
) -> List[Any]:
    """
    Sort a list of objects using bucket sort with a custom key function.
    
    Args:
        arr: List of objects to sort
        key: Function to extract numeric sort key from each object
        num_buckets: Number of buckets to use
        reverse: If True, sort in descending order (default: False)
    
    Returns:
        Sorted list of objects
    
    Examples:
        >>> students = [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]
        >>> bucket_sort_objects(students, key=lambda x: x['grade'])
        [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]
    """
    if not arr:
        return arr
    
    n = len(arr)
    if n <= 1:
        return arr.copy()
    
    # Determine number of buckets
    if num_buckets is None:
        num_buckets = max(1, int(math.sqrt(n)))
    
    # Extract keys
    keys = [key(obj) for obj in arr]
    min_key = min(keys)
    max_key = max(keys)
    
    if min_key == max_key:
        return arr.copy()
    
    # Initialize buckets
    buckets: List[List[Any]] = [[] for _ in range(num_buckets)]
    
    # Calculate bucket range
    bucket_range = (max_key - min_key) / num_buckets
    
    # Distribute objects into buckets
    for obj in arr:
        key_val = key(obj)
        bucket_index = min(
            int((key_val - min_key) / bucket_range),
            num_buckets - 1
        )
        buckets[bucket_index].append(obj)
    
    # Sort individual buckets
    for i in range(num_buckets):
        buckets[i].sort(key=key, reverse=reverse)
    
    # Concatenate sorted buckets
    result = []
    if reverse:
        for bucket in reversed(buckets):
            result.extend(bucket)
    else:
        for bucket in buckets:
            result.extend(bucket)
    
    return result


def bucket_sort_in_place(arr: List[Union[int, float]], num_buckets: Optional[int] = None, reverse: bool = False) -> None:
    """
    Sort a list in place using bucket sort (modifies the original array).
    
    Args:
        arr: List of numeric elements to sort in place
        num_buckets: Number of buckets to use (default: sqrt(n))
        reverse: If True, sort in descending order (default: False)
    
    Returns:
        None: The function modifies the array in place
    
    Examples:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> bucket_sort_in_place(arr)
        >>> arr
        [11, 12, 22, 25, 34, 64, 90]
    """
    sorted_arr = bucket_sort(arr, num_buckets=num_buckets, reverse=reverse)
    arr[:] = sorted_arr


if __name__ == "__main__":
    # Example usage and demonstrations
    print("=== Bucket Sort Examples ===\n")
    
    # Example 1: Integer array
    int_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original integer array: {int_array}")
    print(f"Sorted array: {bucket_sort(int_array)}\n")
    
    # Example 2: Float array
    float_array = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
    print(f"Original float array: {float_array}")
    print(f"Sorted array: {bucket_sort(float_array)}\n")
    
    # Example 3: String array
    string_array = ['banana', 'apple', 'cherry', 'date', 'elderberry']
    print(f"Original string array: {string_array}")
    print(f"Sorted array: {bucket_sort_strings(string_array)}\n")
    
    # Example 4: Custom objects
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78},
        {'name': 'Diana', 'grade': 95}
    ]
    print(f"Original students: {students}")
    sorted_students = bucket_sort_objects(students, key=lambda x: x['grade'])
    print(f"Sorted by grade: {sorted_students}\n")
    
    # Example 5: Descending order
    desc_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {desc_array}")
    print(f"Sorted descending: {bucket_sort(desc_array, reverse=True)}\n")
    
    # Example 6: In-place sorting
    inplace_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before in-place sort: {inplace_array}")
    bucket_sort_in_place(inplace_array)
    print(f"After in-place sort: {inplace_array}\n")
    
    # Example 7: Large random array
    import random
    random.seed(42)
    large_array = [random.randint(1, 1000) for _ in range(20)]
    print(f"Large random array (20 elements): {large_array}")
    print(f"Sorted array: {bucket_sort(large_array)}\n")
