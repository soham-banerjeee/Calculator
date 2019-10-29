
import unittest,csv
from calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        #self.assertIsInstance(calculator, Calculator())

    def test_addition(self):
        calculator=Calculator()
        test_data_row_list = list()
        csv_reader = csv.reader(open("./src/add.csv", 'r'), delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            test_data_row_list.append(row)
        for row in test_data_row_list:
            x = int(row[0])
            y = int(row[1])
            z = int(row[2])
            r = calculator.add(x, y)
            self.assertEqual(r, z)





if __name__ == '__main__':
        unittest.main()
 

