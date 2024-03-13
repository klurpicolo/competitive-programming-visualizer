# 2. Given an elevation map of ruins represented in the form of an array of positive
# numbers, where the width of each bar is 1. Create an approach to calculate the
# amount of sand that would get trapped in the ruins in a sandstorm.
# Example:
# Input: [4,2,1,0,5,4,1,0,2,1,0,1]
# Output: 13


from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class State:
    input: List[int]
    left_pnt: int
    max_left_height: int
    right_pnt: int
    max_right_height: int
    sand: int
    state_type: str


# Time complexity: O(n)
# Space complexity: 1
def solve(input: List[int]) -> Tuple[int, List[State]]:

    # handle edge case
    if len(input) <= 2:
        return 0, []

    # initialize the state variables
    states = []
    sand = 0
    left_pnt = 0
    max_left_height = input[left_pnt]
    right_pnt = len(input) - 1
    max_right_height = input[right_pnt]

    while (left_pnt != right_pnt):
        left_height = input[left_pnt]
        right_height = input[right_pnt]

        states.append(State(input, left_pnt, max_left_height, right_pnt, max_right_height, sand, 'Iteration'))

        # move the shorter height, then get sand from diff of max height and its height
        if left_height > right_height:
            right_pnt -= 1
            if input[right_pnt] < max_right_height:
                sand += max_right_height - input[right_pnt]
            else:
                max_right_height = input[right_pnt]
        else:
            left_pnt += 1
            if input[left_pnt] < max_left_height:
                sand += max_left_height - input[left_pnt]
            else:
                max_left_height = input[left_pnt]

    states.append(State(input, left_pnt, max_left_height, right_pnt, max_right_height, sand, 'End'))
    return sand, states


if __name__ == '__main__':
    input = [4,2,1,0,5,4,1,0,2,1,0,1]
    output, states = solve(input)
    print(f'the answer of input {input} is {output}')
    for state in states:
        print(state)