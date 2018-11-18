from unittest import TestCase, main

from structure import Infinity, NegativeInfinity


class InfinityTest(TestCase):
	def test_gt(self):
		inf = Infinity()
		self.assertGreater(inf, 0)
		self.assertGreater(inf, dict())
		self.assertGreater(inf, list())
		self.assertGreater(inf, tuple())
		self.assertGreater(inf, str())
		self.assertGreater(inf, float())

	def test_ge(self):
		inf = Infinity()
		self.assertGreaterEqual(inf, 0)
		self.assertGreaterEqual(inf, dict())
		self.assertGreaterEqual(inf, list())
		self.assertGreaterEqual(inf, tuple())
		self.assertGreaterEqual(inf, str())
		self.assertGreaterEqual(inf, float())

	def test_lt(self):
		inf = Infinity()
		self.assertFalse(inf < 0)
		self.assertFalse(inf < dict())
		self.assertFalse(inf < list())
		self.assertFalse(inf < tuple())
		self.assertFalse(inf < str())
		self.assertFalse(inf < float())

	def test_le(self):
		inf = Infinity()
		self.assertFalse(inf <= 0)
		self.assertFalse(inf <= dict())
		self.assertFalse(inf <= list())
		self.assertFalse(inf <= tuple())
		self.assertFalse(inf <= str())
		self.assertFalse(inf <= float())

	def test_eq(self):
		inf = Infinity()
		self.assertFalse(inf == 0)
		self.assertFalse(inf == dict())
		self.assertFalse(inf == list())
		self.assertFalse(inf == tuple())
		self.assertFalse(inf == str())
		self.assertFalse(inf == float())

	def test_ne(self):
		inf = Infinity()
		self.assertTrue(inf != 0)
		self.assertTrue(inf != dict())
		self.assertTrue(inf != list())
		self.assertTrue(inf != tuple())
		self.assertTrue(inf != str())
		self.assertTrue(inf != int())


class NegativeInfinityTest(TestCase):
	def test_lt(self):
		inf = NegativeInfinity()
		self.assertLess(inf, 0)
		self.assertLess(inf, dict())
		self.assertLess(inf, list())
		self.assertLess(inf, tuple())
		self.assertLess(inf, str())
		self.assertLess(inf, float())

	def test_le(self):
		inf = NegativeInfinity()
		self.assertLessEqual(inf, 0)
		self.assertLessEqual(inf, dict())
		self.assertLessEqual(inf, list())
		self.assertLessEqual(inf, tuple())
		self.assertLessEqual(inf, str())
		self.assertLessEqual(inf, float())

	def test_gt(self):
		inf = NegativeInfinity()
		self.assertFalse(inf > 0)
		self.assertFalse(inf > dict())
		self.assertFalse(inf > list())
		self.assertFalse(inf > tuple())
		self.assertFalse(inf > str())
		self.assertFalse(inf > float())

	def test_ge(self):
		inf = NegativeInfinity()
		self.assertFalse(inf >= 0)
		self.assertFalse(inf >= dict())
		self.assertFalse(inf >= list())
		self.assertFalse(inf >= tuple())
		self.assertFalse(inf >= str())
		self.assertFalse(inf >= float())

	def test_eq(self):
		inf = NegativeInfinity()
		self.assertFalse(inf == 0)
		self.assertFalse(inf == dict())
		self.assertFalse(inf == list())
		self.assertFalse(inf == tuple())
		self.assertFalse(inf == str())
		self.assertFalse(inf == float())

	def test_ne(self):
		inf = NegativeInfinity()
		self.assertTrue(inf != 0)
		self.assertTrue(inf != dict())
		self.assertTrue(inf != list())
		self.assertTrue(inf != tuple())
		self.assertTrue(inf != str())
		self.assertTrue(inf != float())


if __name__ == "__main__":
	main()
