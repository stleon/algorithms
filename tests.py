from linear_search import linear_search_1, linear_search_2, linear_search_3
import unittest

class TestLinearSearch(unittest.TestCase):
	
	def setUp(self):
		self.lst = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
	
	def assertFunctions(self, *args, **kwargs):
		for func in args:
			result = func(self.lst, kwargs['str2find'])
			self.assertEqual(result, kwargs['index2find'], 'Problem with %s function' % func.__name__)

	def testMiddle(self):
		self.assertFunctions(linear_search_1, linear_search_2, linear_search_3, str2find='t', index2find=4)

	def testNotIn(self):
		self.assertFunctions(linear_search_1, linear_search_2, linear_search_3, str2find='1', index2find=None)

	def testEnd(self):
		self.assertFunctions(linear_search_1, linear_search_2, linear_search_3, str2find='p', index2find=9)


if __name__ == '__main__':
	unittest.main()