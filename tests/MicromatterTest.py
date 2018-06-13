import unittest
import pathlib
import sys

# importing parseCsvShimadzu  
sys.path.append('../')
import Micromatter

# test data
file_path='data/calibration/micromatter.csv'
file_content = pathlib.Path(file_path).read_text()

class MicromatterTest(unittest.TestCase):

    def test_34662(self):
        Na = Micromatter.getMasses(file_content,34662)[11]
        Cl = Micromatter.getMasses(file_content,34662)[17]
        total = Micromatter.getMasses(file_content,34662)['total']

        self.assertEqual(Na,19.5899428492)
        self.assertEqual(Cl,30.2100571508)
        self.assertEqual(total,49.8)

if __name__ == '__main__':
    unittest.main()
  
