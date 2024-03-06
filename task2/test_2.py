import unittest
import solution_2

class TestSolution1(unittest.TestCase):

    def test_case_1_example(self):
        result, _ = solution_2.solve([4, 2, 1, 0, 5, 4, 1, 0, 2, 1, 0, 1])
        self.assertEqual(result, 13)

    def test_case_2_simple(self):
        result, _ = solution_2.solve([1,0,1])
        self.assertEqual(result, 1)

    def test_case_3_simple(self):
        result, _ = solution_2.solve([5,0,2])
        self.assertEqual(result, 2)

    def test_case_4_increase_left_to_right(self):
        result, _ = solution_2.solve([0,1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(result, 0)

    def test_case_5_increase_right_to_left(self):
        result, _ = solution_2.solve([10,9,8,7,6,5,4,3,2,1,0])
        self.assertEqual(result, 0)

    def test_case_6_all_equal(self):
        result, _ = solution_2.solve([1,1,1,1,1])
        self.assertEqual(result, 0)

    def test_case_7_middle_ruins(self):
        result, _ = solution_2.solve([5,0,20,0,10])
        self.assertEqual(result, 15)

    def test_case_8(self):
        result, _ = solution_2.solve([1,0,3,0,5,0,3,0,1])
        self.assertEqual(result, 8)

    def test_case_9(self):
        result, _ = solution_2.solve([0,1,0,2,1,0,1,3,2,1,2,1])
        self.assertEqual(result, 6)
    
    def test_case_10(self):
        result, _ = solution_2.solve([4,2,0,3,2,5])
        self.assertEqual(result, 9)

    def test_case_11_edge_0_length(self):
        result, _ = solution_2.solve([])
        self.assertEqual(result, 0)

    def test_case_12_edge_1_length(self):
        result, _ = solution_2.solve([30])
        self.assertEqual(result, 0)

    def test_case_13_edge_lenght(self):
        result, _ = solution_2.solve([999, 111])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()