from linear_search import linear_search_1, linear_search_2, linear_search_3
from binary_search import binary_search
from selection_sort import selection_sort
import unittest


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.lst = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']

    def assertFunctions(self, *args, **kwargs):
        for func in args:
            result = func(self.lst, kwargs['str2find'])
            self.assertEqual(result, kwargs['index2find'],
                             'Problem with %s function' % func.__name__)

    def testMiddle(self):
        self.assertFunctions(
            linear_search_1,
            linear_search_2,
            linear_search_3,
            str2find='t',
            index2find=4)

    def testNotIn(self):
        self.assertFunctions(
            linear_search_1,
            linear_search_2,
            linear_search_3,
            str2find='1',
            index2find=None)

    def testEnd(self):
        self.assertFunctions(
            linear_search_1,
            linear_search_2,
            linear_search_3,
            str2find='p',
            index2find=9)


class TestBinarySearch(unittest.TestCase):
    def testDuplicateElements(self):
        '''
		Точно не знаю, должна ли функция возвращать результат 0 или 1. В данный ситуации вернет 1, 
		но можно дописать в коде условие, чтобы проверяло, не является ли элемент слева таким же и тд. 
		И тогда вернуть крайний левый похожий элемент.
		'''
        self.assertEqual(
            binary_search([1, 1, 2, 2, 3, 3, 4], 1), 1,
            'Problem with duplicate elements')

    def testListLen(self):
        self.assertEqual(binary_search([], 1), None, 'Problem with empty list')
        self.assertEqual(
            binary_search([5], 5), 0, 'Problem with one element in list')
        self.assertEqual(
            binary_search([5, 6], 6), 1, 'Problem with 2 elements in list')

    def testFirstLastElements(self):
        self.assertEqual(
            binary_search([0, 1, 2, 3, 4, 5], 0), 0,
            'Problem with first element in the list')
        self.assertEqual(
            binary_search([0, 1, 2, 3, 4, 5], 5), 5,
            'Problem with last element in the list')

    def testNotIn(self):
        self.assertEqual(binary_search([1, 2], 3), None, 'Element not in list')


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        self.lst = [100, 10, 1000, 1]
        self.lst_sorted = [1, 10, 100, 1000]

    def testResult(self):
        self.assertEqual(
            selection_sort(self.lst), self.lst_sorted, 'Problem with sorting')

    def testSortedResult(self):
        self.assertEqual(
            selection_sort(self.lst_sorted), self.lst_sorted,
            'Problem with sorting')


if __name__ == '__main__':
    unittest.main()
