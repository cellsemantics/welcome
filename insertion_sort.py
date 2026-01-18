"""
Insertion Sort Implementation

This module provides an implementation of the insertion sort algorithm,
which is a simple sorting algorithm that builds the final sorted array
one item at a time.

Time Complexity:
- Best Case: O(n) - when array is already sorted
- Average Case: O(n²)
- Worst Case: O(n²) - when array is reverse sorted

Space Complexity: O(1) - sorts in place
"""


def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.
    
    The algorithm works by dividing the array into a sorted and unsorted region.
    Values from the unsorted region are picked and placed at the correct position
    in the sorted region.
    
    Args:
        arr (list): The list to be sorted. Can contain integers or floats.
    
    Returns:
        list: The sorted list in ascending order.
    
    Examples:
        >>> insertion_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        
        >>> insertion_sort([5, 2, 4, 6, 1, 3])
        [1, 2, 3, 4, 5, 6]
        
        >>> insertion_sort([1])
        [1]
        
        >>> insertion_sort([])
        []
    """
    # Make a copy to avoid modifying the original array
    arr = arr.copy()
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key at its correct position
        arr[j + 1] = key
    
    return arr


def insertion_sort_descending(arr):
    """
    Sorts an array in descending order using the insertion sort algorithm.
    
    Args:
        arr (list): The list to be sorted. Can contain integers or floats.
    
    Returns:
        list: The sorted list in descending order.
    
    Examples:
        >>> insertion_sort_descending([64, 34, 25, 12, 22, 11, 90])
        [90, 64, 34, 25, 22, 12, 11]
    """
    # Make a copy to avoid modifying the original array
    arr = arr.copy()
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Move elements of arr[0..i-1] that are less than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place key at its correct position
        arr[j + 1] = key
    
    return arr


def insertion_sort_in_place(arr):
    """
    Sorts an array in place (modifies the original array) using insertion sort.
    
    Args:
        arr (list): The list to be sorted in place.
    
    Returns:
        None: The function modifies the array in place.
    
    Examples:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> insertion_sort_in_place(arr)
        >>> arr
        [11, 12, 22, 25, 34, 64, 90]
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    # Example usage
    print("Insertion Sort Examples\n" + "=" * 50)
    
    # Example 1: Basic sorting
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr1}")
    print(f"Sorted array:   {insertion_sort(arr1)}")
    print()
    
    # Example 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print(f"Already sorted: {arr2}")
    print(f"Result:         {insertion_sort(arr2)}")
    print()
    
    # Example 3: Reverse sorted array
    arr3 = [5, 4, 3, 2, 1]
    print(f"Reverse sorted: {arr3}")
    print(f"Result:         {insertion_sort(arr3)}")
    print()
    
    # Example 4: Array with duplicates
    arr4 = [3, 7, 3, 1, 9, 1, 5]
    print(f"With duplicates: {arr4}")
    print(f"Result:          {insertion_sort(arr4)}")
    print()
    
    # Example 5: Descending order
    arr5 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array:    {arr5}")
    print(f"Descending sorted: {insertion_sort_descending(arr5)}")
    print()
    
    # Example 6: In-place sorting
    arr6 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Before in-place sort: {arr6}")
    insertion_sort_in_place(arr6)
    print(f"After in-place sort:  {arr6}")
