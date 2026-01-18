"""
Unit tests for insertion sort implementation
"""

import unittest
from insertion_sort import insertion_sort, insertion_sort_descending, insertion_sort_in_place


class TestInsertionSort(unittest.TestCase):
    """Test cases for the insertion_sort function"""
    
    def test_basic_sorting(self):
        """Test basic sorting of unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_already_sorted(self):
        """Test sorting an already sorted array"""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array (worst case)"""
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_single_element(self):
        """Test sorting an array with a single element"""
        arr = [42]
        expected = [42]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_empty_array(self):
        """Test sorting an empty array"""
        arr = []
        expected = []
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_duplicates(self):
        """Test sorting an array with duplicate elements"""
        arr = [3, 7, 3, 1, 9, 1, 5]
        expected = [1, 1, 3, 3, 5, 7, 9]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_two_elements(self):
        """Test sorting an array with two elements"""
        arr = [2, 1]
        expected = [1, 2]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_all_same_elements(self):
        """Test sorting an array where all elements are the same"""
        arr = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers"""
        arr = [3, -1, 4, -5, 2, 0]
        expected = [-5, -1, 0, 2, 3, 4]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_floats(self):
        """Test sorting an array with floating point numbers"""
        arr = [3.5, 1.2, 4.8, 2.1, 0.5]
        expected = [0.5, 1.2, 2.1, 3.5, 4.8]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_original_array_unchanged(self):
        """Test that the original array is not modified"""
        arr = [3, 1, 4, 1, 5]
        original = arr.copy()
        insertion_sort(arr)
        self.assertEqual(arr, original)


class TestInsertionSortDescending(unittest.TestCase):
    """Test cases for the insertion_sort_descending function"""
    
    def test_descending_basic(self):
        """Test basic descending sort"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [90, 64, 34, 25, 22, 12, 11]
        self.assertEqual(insertion_sort_descending(arr), expected)
    
    def test_descending_already_sorted(self):
        """Test descending sort on already descending array"""
        arr = [5, 4, 3, 2, 1]
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort_descending(arr), expected)
    
    def test_descending_with_duplicates(self):
        """Test descending sort with duplicates"""
        arr = [3, 7, 3, 1, 9, 1, 5]
        expected = [9, 7, 5, 3, 3, 1, 1]
        self.assertEqual(insertion_sort_descending(arr), expected)


class TestInsertionSortInPlace(unittest.TestCase):
    """Test cases for the insertion_sort_in_place function"""
    
    def test_in_place_basic(self):
        """Test in-place sorting modifies the original array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, expected)
    
    def test_in_place_returns_none(self):
        """Test that in-place sort returns None"""
        arr = [3, 1, 4, 1, 5]
        result = insertion_sort_in_place(arr)
        self.assertIsNone(result)
    
    def test_in_place_empty(self):
        """Test in-place sorting of empty array"""
        arr = []
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [])
    
    def test_in_place_single(self):
        """Test in-place sorting of single element"""
        arr = [42]
        insertion_sort_in_place(arr)
        self.assertEqual(arr, [42])


if __name__ == "__main__":
    unittest.main()
