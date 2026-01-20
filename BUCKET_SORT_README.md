# Bucket Sort Implementation

A comprehensive, production-ready bucket sort algorithm implementation in Python with support for various data types and use cases.

## Overview

Bucket sort is a distribution-based sorting algorithm that works by distributing elements into a number of buckets, sorting each bucket individually, and then concatenating the sorted buckets. This implementation provides robust handling of integers, floats, strings, and custom objects.

## Algorithm Complexity

| Case | Time Complexity | Space Complexity |
|------|----------------|------------------|
| Best | O(n + k) | O(n + k) |
| Average | O(n + k) | O(n + k) |
| Worst | O(n²) | O(n + k) |

Where:
- `n` = number of elements
- `k` = number of buckets

## Features

- ✅ **Multiple data type support**: integers, floats, strings, and custom objects
- ✅ **Configurable bucket count**: automatic or manual bucket count selection
- ✅ **Negative number handling**: works with both positive and negative numbers
- ✅ **Custom key functions**: sort objects by custom criteria
- ✅ **Case-sensitive/insensitive string sorting**
- ✅ **Ascending and descending order**: reverse parameter for descending sort
- ✅ **In-place sorting**: optional in-place modification for memory efficiency
- ✅ **Comprehensive test suite**: 50+ unit tests covering edge cases
- ✅ **Type hints**: full type annotation support for better IDE integration
- ✅ **Optimized for small arrays**: uses insertion sort for individual buckets

## Installation

Simply copy the `bucket_sort.py` file to your project directory:

```bash
# Clone the repository
git clone https://github.com/cellsemantics/welcome.git
cd welcome

# Or download just the file
wget https://raw.githubusercontent.com/cellsemantics/welcome/main/bucket_sort.py
```

## Usage

### Basic Usage - Sorting Integers

```python
from bucket_sort import bucket_sort

# Sort a list of integers
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### Sorting Floating Point Numbers

```python
from bucket_sort import bucket_sort

# Sort a list of floats
decimals = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_decimals = bucket_sort(decimals)
print(sorted_decimals)  # Output: [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
```

### Sorting with Custom Bucket Count

```python
from bucket_sort import bucket_sort

numbers = [64, 34, 25, 12, 22, 11, 90]

# Use 5 buckets instead of default
sorted_numbers = bucket_sort(numbers, num_buckets=5)
```

### Sorting in Descending Order

```python
from bucket_sort import bucket_sort

numbers = [64, 34, 25, 12, 22, 11, 90]

# Sort in descending order
sorted_desc = bucket_sort(numbers, reverse=True)
print(sorted_desc)  # Output: [90, 64, 34, 25, 22, 12, 11]
```

### In-Place Sorting

```python
from bucket_sort import bucket_sort_in_place

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Before: {numbers}")

# Sort in place (modifies original array)
bucket_sort_in_place(numbers)
print(f"After: {numbers}")  # Output: [11, 12, 22, 25, 34, 64, 90]

# In-place descending sort
bucket_sort_in_place(numbers, reverse=True)
print(f"Reversed: {numbers}")  # Output: [90, 64, 34, 25, 22, 12, 11]
```

### Sorting Strings

```python
from bucket_sort import bucket_sort_strings

# Case-sensitive sorting (default)
fruits = ['banana', 'apple', 'cherry', 'date', 'elderberry']
sorted_fruits = bucket_sort_strings(fruits)
print(sorted_fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Case-insensitive sorting
mixed_case = ['Banana', 'apple', 'Cherry', 'date']
sorted_mixed = bucket_sort_strings(mixed_case, case_sensitive=False)
```

### Sorting Custom Objects

```python
from bucket_sort import bucket_sort_objects

# Sort dictionaries by a specific field
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78},
    {'name': 'Diana', 'grade': 95}
]

sorted_students = bucket_sort_objects(students, key=lambda x: x['grade'])
# Output: Students sorted by grade from lowest to highest

# Sort custom class instances
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person('Alice', 30),
    Person('Bob', 25),
    Person('Charlie', 35)
]

sorted_people = bucket_sort_objects(people, key=lambda p: p.age)
```

### Advanced Usage with Key Functions

```python
from bucket_sort import bucket_sort

# Sort tuples by the second element
data = [(1, 100), (2, 50), (3, 75), (4, 25)]
sorted_data = bucket_sort_objects(data, key=lambda x: x[1])
# Output: [(4, 25), (2, 50), (3, 75), (1, 100)]
```

## API Reference

### `bucket_sort(arr, num_buckets=None, key=None, reverse=False)`

Sort a list of numeric values using bucket sort.

**Parameters:**
- `arr` (List[Union[int, float]]): List of numeric elements to sort
- `num_buckets` (Optional[int]): Number of buckets to use (default: √n)
- `key` (Optional[Callable]): Function to extract comparison key from each element
- `reverse` (bool): If True, sort in descending order (default: False)

**Returns:**
- `List[Union[int, float]]`: Sorted list in ascending or descending order

**Raises:**
- `ValueError`: If the array contains invalid data types

---

### `bucket_sort_strings(arr, num_buckets=None, case_sensitive=True, reverse=False)`

Sort a list of strings using bucket sort.

**Parameters:**
- `arr` (List[str]): List of strings to sort
- `num_buckets` (Optional[int]): Number of buckets to use (default: 26)
- `case_sensitive` (bool): Whether to perform case-sensitive sorting (default: True)
- `reverse` (bool): If True, sort in descending order (default: False)

**Returns:**
- `List[str]`: Sorted list of strings

---

### `bucket_sort_objects(arr, key, num_buckets=None, reverse=False)`

Sort a list of objects using bucket sort with a custom key function.

**Parameters:**
- `arr` (List[Any]): List of objects to sort
- `key` (Callable[[Any], Union[int, float]]): Function to extract numeric sort key
- `num_buckets` (Optional[int]): Number of buckets to use (default: √n)
- `reverse` (bool): If True, sort in descending order (default: False)

**Returns:**
- `List[Any]`: Sorted list of objects

---

### `bucket_sort_in_place(arr, num_buckets=None, reverse=False)`

Sort a list in place using bucket sort (modifies the original array).

**Parameters:**
- `arr` (List[Union[int, float]]): List of numeric elements to sort in place
- `num_buckets` (Optional[int]): Number of buckets to use (default: √n)
- `reverse` (bool): If True, sort in descending order (default: False)

**Returns:**
- `None`: The function modifies the array in place

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python test_bucket_sort.py

# Run with verbose output
python -m pytest test_bucket_sort.py -v

# Run specific test class
python -m unittest test_bucket_sort.TestBucketSort
```

The test suite includes:
- ✅ 50+ unit tests
- ✅ Edge case testing (empty arrays, single elements, duplicates)
- ✅ Performance testing with large datasets
- ✅ Negative number handling
- ✅ Float precision tests
- ✅ String sorting tests
- ✅ Object sorting tests

## Performance Characteristics

### When to Use Bucket Sort

Bucket sort is most efficient when:
- Elements are uniformly distributed across a range
- You know the approximate range of input values
- Working with floating-point numbers in a known range
- Need linear time complexity on average

### When NOT to Use Bucket Sort

Consider other algorithms when:
- Elements are highly clustered (all in one bucket)
- Range of values is unknown or very large
- Memory is limited (bucket sort requires O(n+k) space)
- You need guaranteed O(n log n) worst-case performance

### Comparison with Other Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n+k) | Yes* |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

*Stability depends on the sorting algorithm used for individual buckets

## Implementation Details

### Bucket Distribution Strategy

The implementation uses a uniform distribution strategy:

```
bucket_index = floor((element - min_value) / bucket_range)
```

Where:
- `bucket_range = (max_value - min_value) / num_buckets`

### Individual Bucket Sorting

Each bucket is sorted using insertion sort, which is:
- Efficient for small arrays (typical bucket size)
- Simple and has low overhead
- Stable (preserves relative order)

### Default Bucket Count

By default, the number of buckets is set to √n:
- Balances distribution overhead with sorting overhead
- Works well for uniformly distributed data
- Can be overridden for specific use cases

## Examples

### Example 1: Financial Data

```python
from bucket_sort import bucket_sort

# Sort stock prices
prices = [45.32, 67.89, 23.45, 89.12, 34.56, 78.90, 56.78]
sorted_prices = bucket_sort(prices)
print(f"Sorted prices: {sorted_prices}")
```

### Example 2: Grade Processing

```python
from bucket_sort import bucket_sort_objects

# Sort students by exam scores
exam_results = [
    {'student': 'Alice', 'score': 87.5},
    {'student': 'Bob', 'score': 92.3},
    {'student': 'Charlie', 'score': 78.9},
    {'student': 'Diana', 'score': 95.1}
]

sorted_results = bucket_sort_objects(exam_results, key=lambda x: x['score'])

for result in sorted_results:
    print(f"{result['student']}: {result['score']}")
```

### Example 3: Large Dataset

```python
from bucket_sort import bucket_sort
import random

# Sort 10,000 random numbers
random.seed(42)
large_dataset = [random.random() * 1000 for _ in range(10000)]

# Use more buckets for better distribution
sorted_data = bucket_sort(large_dataset, num_buckets=100)
```

## Troubleshooting

### Issue: Slow performance on clustered data

**Solution:** Increase the number of buckets or use a different sorting algorithm.

```python
# If data is clustered, try increasing buckets
sorted_data = bucket_sort(data, num_buckets=len(data) // 10)
```

### Issue: Memory errors with very large datasets

**Solution:** Reduce the number of buckets or process data in chunks.

```python
# Use fewer buckets to reduce memory usage
sorted_data = bucket_sort(large_data, num_buckets=10)
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This implementation is part of the cellsemantics/welcome repository and is provided under the MIT License.

## References

- [Bucket Sort - Wikipedia](https://en.wikipedia.org/wiki/Bucket_sort)
- [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/books/introduction-algorithms)
- [Sorting Algorithm Comparison](https://www.bigocheatsheet.com/)

## Support

For issues, questions, or contributions:
- Open an issue on [GitHub](https://github.com/cellsemantics/welcome/issues)
- Reach out to maintainers via GitHub discussions

---

**Last Updated:** January 2026  
**Version:** 1.0.0  
**Python Version:** 3.7+
