import unittest

import pythondil

class TestPolish(unittest.TestCase):
	def test_polish(self):
		self.assertEqual(pythondil.AvtandilProgram.float_polish(self, "0.5"), "0,5")
		self.assertEqual(pythondil.AvtandilProgram.float_polish(self, "15.23"), "15,23")

class TestAssign(unittest.TestCase):
	def test_assign(self):
		self.vars = {}
		self.assertEqual(pythondil.AvtandilProgram.assign_var(self, ("orationem", 3)), 3)
	
class Var(unittest.TestCase):
	def test_var(self):
		self.vars = {"orationem": 3}
		self.assertEqual(pythondil.AvtandilProgram.var(self, "orationem"), 3)	
		
class Summation(unittest.TestCase):
	def test_summation(self):
		self.assertEqual(pythondil.AvtandilProgram.summation(self, 4, 5), "9.0")
		self.assertEqual(pythondil.AvtandilProgram.summation(self, 16, 16), "32.0")

class Division(unittest.TestCase):
	def test_division(self):
		self.assertEqual(pythondil.AvtandilProgram.division(self, 9, 3), "3.0")
		self.assertEqual(pythondil.AvtandilProgram.division(self, 16, '0'), "∅")

class FloatTrue(unittest.TestCase):
	def test_float_true(self):
		self.assertEqual(pythondil.AvtandilProgram.float_true(self, "0,5"), "0.5")
		self.assertEqual(pythondil.AvtandilProgram.float_true(self, "15,23"), "15.23")

if __name__ == '__main__':
	unittest.main()
