from python_test_case import PythonTestCase, run_tests
from unittest.mock import patch, call
import sys
from io import StringIO
from pylab import *

class Tests(PythonTestCase):

    def setUp(self):
        try:
            del sys.modules["attempt"]
        except KeyError:
            pass
			
    def test1(self):
        """"Team B is most popular with input 1000, 500, 4500, 4500."""
        user_input = ["1000","500","4500", "4500"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Team B has the most fans for month 1\nTeam A has the most fans for month 2\nTeam B has the most fans for month 3\nTeam A has the most fans for month 4\nTeam A has the most fans for month 5\nTeam B has the most fans for month 6\nTeam A has the most fans for month 7\nTeam A has the most fans for month 8\nTeam B has the most fans for month 9\nTeam B has the most fans for month 10\nTeam A has the most fans for month 11\nTeam B has the most fans for month 12\nBoth teams are equally popular.")
				
    def test2(self):
        """ Team A is most popular with input 1000, 500, 4500, 4000"""
        user_input = ["1000","500","4500", "4000"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Team A has the most fans for month 1\nTeam A has the most fans for month 2\nTeam B has the most fans for month 3\nTeam A has the most fans for month 4\nTeam A has the most fans for month 5\nTeam A has the most fans for month 6\nTeam A has the most fans for month 7\nTeam A has the most fans for month 8\nTeam B has the most fans for month 9\nTeam A has the most fans for month 10\nTeam A has the most fans for month 11\nTeam B has the most fans for month 12\nTeam A has the most fans for 9 months.")
				             
               
    def test3(self):
        """ Team B is the most popular with input -500, 500, 5000, 5000"""
        user_input = ["-500","500","5000", "5000"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Team B has the most fans for month 1\nTeam B has the most fans for month 2\nTeam A has the most fans for month 3\nTeam A has the most fans for month 4\nBoth teams are equally popular for month 5\nTeam A has the most fans for month 6\nTeam A has the most fans for month 7\nTeam B has the most fans for month 8\nTeam A has the most fans for month 9\nTeam B has the most fans for month 10\nTeam B has the most fans for month 11\nTeam B has the most fans for month 12\nTeam B has the most fans for 6 months.")
    
    
    def test4(self):
        """ Team A is the most popular with input 500, 500, 5000, 5000"""
        user_input = ["500","500","5000", "5000"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Team B has the most fans for month 1\nTeam A has the most fans for month 2\nTeam B has the most fans for month 3\nTeam A has the most fans for month 4\nTeam A has the most fans for month 5\nTeam A has the most fans for month 6\nTeam A has the most fans for month 7\nTeam A has the most fans for month 8\nTeam B has the most fans for month 9\nTeam B has the most fans for month 10\nBoth teams are equally popular for month 11\nTeam B has the most fans for month 12\nTeam A has the most fans for 6 months.")
                
    def test5(self):
        """ Both teams are equally popular with input 0, 0, 10, 10"""
        user_input = ["0","0","10", "10"]
        with patch("builtins.input", side_effect=user_input) as input_call:
            with patch("sys.stdout", new=StringIO()) as output:
                import attempt
                self.assertEqual(output.getvalue().strip(),"Both teams are equally popular for month 1\nBoth teams are equally popular for month 2\nBoth teams are equally popular for month 3\nBoth teams are equally popular for month 4\nBoth teams are equally popular for month 5\nBoth teams are equally popular for month 6\nBoth teams are equally popular for month 7\nBoth teams are equally popular for month 8\nBoth teams are equally popular for month 9\nBoth teams are equally popular for month 10\nBoth teams are equally popular for month 11\nBoth teams are equally popular for month 12\nBoth teams are equally popular.")

   
		
		
# Run the unit tests
if __name__ == "__main__":
        run_tests(Tests)
