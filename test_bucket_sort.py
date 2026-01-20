"""
Unit tests for bucket sort implementation.

This module contains comprehensive tests for all bucket sort functions
including edge cases, performance tests, and validation.
"""

import unittest
import random
from bucket_sort import (
    bucket_sort,
    bucket_sort_strings,
    bucket_sort_objects,
    _insertion_sort
)


class TestBucketSort(unittest.TestCase):
    """Test cases for the main bucket_sort function."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(bucket_sort([]), [])
    
    def test_single_element(self):
        """Test sorting a single element array."""
        self.assertEqual(bucket_sort([42]), [42])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(bucket_sort(arr), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(bucket_sort(arr), [1, 2, 3, 4, 5])
    
    def test_random_integers(self):
        """Test sorting random integers."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bucket_sort(arr), expected)
    
    def test_duplicate_elements(self):
        """Test sorting array with duplicate elements."""
        arr = [5, 2, 8, 2, 9, 1, 5, 5]
        expected = [1, 2, 2, 5, 5, 5, 8, 9]
        self.assertEqual(bucket_sort(arr), expected)
    
    def test_all_same_elements(self):
        """Test sorting array where all elements are the same."""
        arr = [7, 7, 7, 7, 7]
        self.assertEqual(bucket_sort(arr), [7, 7, 7, 7, 7])
    
    def test_float_values(self):
        """Test sorting floating point numbers."""
        arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
        expected = [0.23, 0.25, 0.32, 0.42, 0.47, 0.51, 0.52]
        result = bucket_sort(arr)
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=10)
    
    def test_negative_numbers(self):
        """Test sorting array with negative numbers."""
        arr = [-5, 3, -1, 7, -9, 2]
        expected = [-9, -5, -1, 2, 3, 7]
        self.assertEqual(bucket_sort(arr), expected)
    
    def test_mixed_positive_negative(self):
        """Test sorting array with mixed positive and negative numbers."""
        arr = [10, -5, 0, 15, -10, 5]
        expected = [-10, -5, 0, 5, 10, 15]
        self.assertEqual(bucket_sort(arr), expected)
    
    def test_large_range(self):
        """Test sorting array with large value range."""
        arr = [1, 1000000, 500000, 1, 999999]
        expected = [1, 1, 500000, 999999, 1000000]
        self.assertEqual(bucket_sort(arr), expected)
    
    def test_custom_bucket_count(self):
        """Test bucket sort with custom bucket count."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bucket_sort(arr, num_buckets=5), expected)
        self.assertEqual(bucket_sort(arr, num_buckets=10), expected)
        self.assertEqual(bucket_sort(arr, num_buckets=3), expected)
    
    def test_single_bucket(self):
        """Test bucket sort with only one bucket."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bucket_sort(arr, num_buckets=1), expected)
    
    def test_original_array_unchanged(self):
        """Test that the original array is not modified."""
        arr = [5, 2, 8, 1, 9]
        original = arr.copy()
        bucket_sort(arr)
        self.assertEqual(arr, original)
    
    def test_large_array(self):
        """Test sorting a large array."""
        random.seed(42)
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        sorted_arr = bucket_sort(arr)
        expected = sorted(arr)
        self.assertEqual(sorted_arr, expected)
    
    def test_very_small_floats(self):
        """Test sorting very small floating point differences."""
        arr = [0.001, 0.002, 0.0005, 0.0015, 0.0025]
        expected = [0.0005, 0.001, 0.0015, 0.002, 0.0025]
        result = bucket_sort(arr)
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=10)


class TestBucketSortStrings(unittest.TestCase):
    """Test cases for bucket_sort_strings function."""
    
    def test_empty_string_array(self):
        """Test sorting an empty string array."""
        self.assertEqual(bucket_sort_strings([]), [])
    
    def test_single_string(self):
        """Test sorting a single string."""
        self.assertEqual(bucket_sort_strings(['hello']), ['hello'])
    
    def test_alphabetic_strings(self):
        """Test sorting alphabetic strings."""
        arr = ['banana', 'apple', 'cherry', 'date']
        expected = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(bucket_sort_strings(arr), expected)
    
    def test_case_sensitive(self):
        """Test case-sensitive string sorting."""
        arr = ['Banana', 'apple', 'Cherry', 'date']
        result = bucket_sort_strings(arr, case_sensitive=True)
        # Should maintain case sensitivity
        self.assertEqual(len(result), 4)
    
    def test_case_insensitive(self):
        """Test case-insensitive string sorting."""
        arr = ['Banana', 'apple', 'Cherry', 'date']
        result = bucket_sort_strings(arr, case_sensitive=False)
        # All strings should be present
        self.assertEqual(len(result), 4)
        self.assertIn('apple', result)
        self.assertIn('Banana', result)
    
    def test_duplicate_strings(self):
        """Test sorting strings with duplicates."""
        arr = ['apple', 'banana', 'apple', 'cherry', 'banana']
        result = bucket_sort_strings(arr)
        expected = ['apple', 'apple', 'banana', 'banana', 'cherry']
        self.assertEqual(result, expected)
    
    def test_custom_bucket_count_strings(self):
        """Test string sorting with custom bucket count."""
        arr = ['banana', 'apple', 'cherry', 'date']
        expected = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(bucket_sort_strings(arr, num_buckets=10), expected)
    
    def test_single_character_strings(self):
        """Test sorting single character strings."""
        arr = ['z', 'a', 'm', 'b', 'y']
        expected = ['a', 'b', 'm', 'y', 'z']
        self.assertEqual(bucket_sort_strings(arr), expected)
    
    def test_empty_strings_in_array(self):
        """Test sorting with empty strings in the array."""
        arr = ['apple', '', 'banana', '']
        result = bucket_sort_strings(arr)
        self.assertEqual(len(result), 4)
        self.assertIn('', result)


class TestBucketSortObjects(unittest.TestCase):
    """Test cases for bucket_sort_objects function."""
    
    def test_empty_object_array(self):
        """Test sorting an empty object array."""
        self.assertEqual(bucket_sort_objects([], key=lambda x: x), [])
    
    def test_dictionary_objects(self):
        """Test sorting dictionary objects by a key."""
        students = [
            {'name': 'Alice', 'grade': 85},
            {'name': 'Bob', 'grade': 92},
            {'name': 'Charlie', 'grade': 78},
            {'name': 'Diana', 'grade': 95}
        ]
        sorted_students = bucket_sort_objects(students, key=lambda x: x['grade'])
        expected_grades = [78, 85, 92, 95]
        actual_grades = [s['grade'] for s in sorted_students]
        self.assertEqual(actual_grades, expected_grades)
    
    def test_custom_objects(self):
        """Test sorting custom objects."""
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            
            def __eq__(self, other):
                return self.name == other.name and self.age == other.age
        
        people = [
            Person('Alice', 30),
            Person('Bob', 25),
            Person('Charlie', 35),
            Person('Diana', 28)
        ]
        sorted_people = bucket_sort_objects(people, key=lambda p: p.age)
        expected_ages = [25, 28, 30, 35]
        actual_ages = [p.age for p in sorted_people]
        self.assertEqual(actual_ages, expected_ages)
    
    def test_tuple_objects(self):
        """Test sorting tuples by a specific element."""
        data = [(1, 100), (2, 50), (3, 75), (4, 25)]
        sorted_data = bucket_sort_objects(data, key=lambda x: x[1])
        expected = [(4, 25), (2, 50), (3, 75), (1, 100)]
        self.assertEqual(sorted_data, expected)
    
    def test_negative_key_values(self):
        """Test sorting objects with negative key values."""
        data = [{'id': 1, 'value': -5}, {'id': 2, 'value': 3}, {'id': 3, 'value': -10}]
        sorted_data = bucket_sort_objects(data, key=lambda x: x['value'])
        expected_values = [-10, -5, 3]
        actual_values = [d['value'] for d in sorted_data]
        self.assertEqual(actual_values, expected_values)
    
    def test_float_key_values(self):
        """Test sorting objects with float key values."""
        data = [
            {'name': 'A', 'score': 85.5},
            {'name': 'B', 'score': 92.3},
            {'name': 'C', 'score': 78.9}
        ]
        sorted_data = bucket_sort_objects(data, key=lambda x: x['score'])
        expected_scores = [78.9, 85.5, 92.3]
        actual_scores = [d['score'] for d in sorted_data]
        self.assertEqual(actual_scores, expected_scores)


class TestInsertionSort(unittest.TestCase):
    """Test cases for the internal insertion sort function."""
    
    def test_insertion_sort_empty(self):
        """Test insertion sort with empty array."""
        self.assertEqual(_insertion_sort([]), [])
    
    def test_insertion_sort_single(self):
        """Test insertion sort with single element."""
        self.assertEqual(_insertion_sort([42]), [42])
    
    def test_insertion_sort_sorted(self):
        """Test insertion sort with already sorted array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(_insertion_sort(arr), [1, 2, 3, 4, 5])
    
    def test_insertion_sort_reverse(self):
        """Test insertion sort with reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(_insertion_sort(arr), [1, 2, 3, 4, 5])
    
    def test_insertion_sort_random(self):
        """Test insertion sort with random array."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(_insertion_sort(arr), expected)
    
    def test_insertion_sort_duplicates(self):
        """Test insertion sort with duplicates."""
        arr = [5, 2, 8, 2, 9, 1, 5, 5]
        expected = [1, 2, 2, 5, 5, 5, 8, 9]
        self.assertEqual(_insertion_sort(arr), expected)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and special scenarios."""
    
    def test_infinity_values(self):
        """Test sorting with infinity values."""
        arr = [1, float('inf'), -float('inf'), 0, 5]
        result = bucket_sort(arr)
        self.assertEqual(result[0], -float('inf'))
        self.assertEqual(result[-1], float('inf'))
    
    def test_very_large_array(self):
        """Test sorting a very large array."""
        random.seed(123)
        arr = [random.random() * 1000 for _ in range(10000)]
        result = bucket_sort(arr)
        expected = sorted(arr)
        self.assertEqual(len(result), len(expected))
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=10)
    
    def test_stability_preservation(self):
        """Test if relative order is preserved for equal elements."""
        # Using objects to track original order
        data = [
            {'id': 1, 'value': 5},
            {'id': 2, 'value': 3},
            {'id': 3, 'value': 5},
            {'id': 4, 'value': 3}
        ]
        sorted_data = bucket_sort_objects(data, key=lambda x: x['value'])
        # Elements with same value should maintain relative order
        value_3_ids = [d['id'] for d in sorted_data if d['value'] == 3]
        value_5_ids = [d['id'] for d in sorted_data if d['value'] == 5]
        self.assertEqual(len(value_3_ids), 2)
        self.assertEqual(len(value_5_ids), 2)


class TestPerformance(unittest.TestCase):
    """Performance-related tests."""
    
    def test_optimal_bucket_count(self):
        """Test that default bucket count provides reasonable performance."""
        random.seed(456)
        arr = [random.randint(1, 10000) for _ in range(1000)]
        
        # Test with default buckets
        result_default = bucket_sort(arr)
        
        # Test with different bucket counts
        result_few = bucket_sort(arr, num_buckets=5)
        result_many = bucket_sort(arr, num_buckets=100)
        
        # All should produce same sorted result
        expected = sorted(arr)
        self.assertEqual(result_default, expected)
        self.assertEqual(result_few, expected)
        self.assertEqual(result_many, expected)
    
    def test_worst_case_scenario(self):
        """Test worst case where all elements fall in one bucket."""
        # All elements in narrow range
        arr = [1.0 + i * 0.000001 for i in range(100)]
        random.shuffle(arr)
        result = bucket_sort(arr, num_buckets=10)
        expected = sorted(arr)
        for i in range(len(result)):
            self.assertAlmostEqual(result[i], expected[i], places=10)


def run_tests():
    """Run all tests and display results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestBucketSort))
    suite.addTests(loader.loadTestsFromTestCase(TestBucketSortStrings))
    suite.addTests(loader.loadTestsFromTestCase(TestBucketSortObjects))
    suite.addTests(loader.loadTestsFromTestCase(TestInsertionSort))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestPerformance))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return success status
    return result.wasSuccessful()


if __name__ == '__main__':
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)
