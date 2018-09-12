from python_test_case import PythonTestCase, run_tests
from pylab import *
from contextlib import redirect_stdout
from os import devnull

with open(devnull, "w") as f:
    with redirect_stdout(f):
        # Redirect the stdout in case the student has global print statements
        import attempt

class Tests(PythonTestCase):

	def test_function_defined(self):
		""" Function 'fdash' is defined """
		self.assertMethodDefined(attempt, "fdash", 1)
			
	def test_function_10(self):
		""" Function 'fdash' returns "0.82436" for input "10" """
		self.assertEqual(attempt.fdash(10), 0.82436)
		
	def test_function_zero(self):
		""" Function 'fdash' returns "0" for input "0""""
		self.assertEqual(attempt.fdash(0), 0)
		
	def test_function_neg15(self):
		""" Function 'fdash' returns "-0.35427" for input "-15" """
		self.assertEqual(attempt.fdash(-15), -0.35427)
		
	def test_function_defined2(self):
		""" Function 'onestep' is defined """
		self.assertMethodDefined(attempt, "onestep", 3)
			
	def test_function_111(self):
		""" Function 'onestep' returns "1.05256" for input "1,1,1" """
		self.assertEqual(attempt.pnestep(1,1,1), 1.05256)
		
	def test_function_101805(self):
		""" Function 'onestep' returns "18.41218" for input "10,18,0.5" """
		self.assertEqual(attempt.onestep(10,18,0.5), 18.41218)
		
	def test_function_1042036810(self):
		""" Function 'onestep' returns "212.4265" for input "10.4,203.68,10" """
		self.assertEqual(attempt.onestep(10.4,203.68,10), 212.4265)
		
	def test_function_defined3(self):
		""" Function 'eulers' is defined """
		self.assertMethodDefined(attempt, "eulers", 4)
			
	def test_function_one(self):
		""" Function 'eulers' returns "10.8205" for input "0,10,0.5,10" """
		self.assertEqual(attempt.pnestep(0,10,0.5,10), 10.8205)
		
	def test_function_two(self):
		""" Function 'eulers' returns "13.42957" for input "12,12,0.1,12" """
		self.assertEqual(attempt.onestep(12,12,0.1,12), 13.42957)
		
	def test_function_three(self):
		""" Function 'eulers' returns "287.669" for input "38.2,95.9,0.1,100" """
		self.assertEqual(attempt.onestep(38.2,95.9,0.1,100), 287.669)
				
# Run the unit tests
if __name__ == "__main__":
    run_tests(Tests)
