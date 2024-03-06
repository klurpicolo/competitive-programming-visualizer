import unittest
from solution_3_tabulation import get_longest_common_substring, solve

class TestSolution3(unittest.TestCase):

    def test_case_1_example(self):
        result, _ = get_longest_common_substring("ababbacdee", "haababadeedc")
        self.assertEqual(result, "abab")

    def test_case_2_simple(self):
        result, _ = get_longest_common_substring("a", "a")
        self.assertEqual(result, "a")

    def test_case_3_no_common(self):
        result, _ = get_longest_common_substring("qwert", "zxcvb")
        self.assertEqual(result, "")

    def test_case_4_edge_empty(self):
        result, _ = get_longest_common_substring("", "")
        self.assertEqual(result, "")

    def test_case_5_example(self):
        result, _ = get_longest_common_substring("abcdefgxyz123", "xyz789abcdef")
        self.assertEqual(result, "abcdef")

    def test_case_6_example(self):
        result, _ = get_longest_common_substring("The adventurous cat explored the mysterious cave.", "A curious cat ventured into the dark cave for exploration.")
        self.assertEqual(result, "ous cat ")

    def test_case_7_example(self):
        result, _ = get_longest_common_substring("Sunflowers bloomed in the radiant sunlight.", "Radiant sunlight illuminated the field of blooming sunflowers.")
        self.assertEqual(result, "adiant sunlight")

    def test_case_8_example_solve(self):
        input_data = [
            (1, "ababbacdee", "haababadeedc"),
            (2, "Thisisadocumentcontainingpatienthistory", "Theletteringinthisstoryisquite unique"),
            (3, "abcdefgxyz123", "xyz789abcdef"),
            (4, "The adventurous cat explored the mysterious cave.", "A curious cat ventured into the dark cave for exploration."),
            (5, "Sunflowers bloomed in the radiant sunlight.", "Radiant sunlight illuminated the field of blooming sunflowers."),
            (6, "Gentle waves lapped against the sandy shore.", "The shore echoed with the soothing sounds of lapping waves.")
        ]
        result = solve(input_data)
        expected = [
            (1, 'abab'), 
            (2, 'nthis'), 
            (3, 'abcdef'), 
            (4, 'ous cat '), 
            (5, 'adiant sunlight'), 
            (6, ' waves')
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()