import unittest
import solution_1

class TestSolution1(unittest.TestCase):

    def test_case_1_example(self):
        result, _ = solution_1.solve([1,3,4,5,7])
        self.assertEqual(result, [[1,1],[3,5],[7,7]])

    def test_case_2_all_discontinuous(self):
        result, _ = solution_1.solve([1,3,5,7,9,11,13,15])
        self.assertEqual(result, [[1,1],[3,3],[5,5],[7,7],[9,9],[11,11],[13,13],[15,15]])

    def test_case_3_all_continuous(self):
        result, _ = solution_1.solve([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        self.assertEqual(result, [[1,20]])

    def test_case_4_all_mix(self):
        result, _ = solution_1.solve([1,2,3,4,5,8,11,12,13,14,15,18,20,21,25])
        self.assertEqual(result, [[1,5],[8,8],[11,15],[18,18],[20,21],[25,25]])

    def test_edge_case_0_length(self):
        result, _ = solution_1.solve([])
        self.assertEqual(result, [])

    def test_edge_case_1_length(self):
        result, _ = solution_1.solve([20])
        self.assertEqual(result, [[20, 20]])


if __name__ == '__main__':
    unittest.main()