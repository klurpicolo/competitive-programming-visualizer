# 1. For any list of integers, develop an approach to summarize the boundaries of any
# continuous series (the start and end of the continuous series).
# Example:
# Input: [1,3,4,5,7]
# Output: [[1,1],[3,5],[7,7]]

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class State:
    input: List[int]
    start_idx: int
    end_idx: int
    output: List[List[int]]

# With out sort
# Time complexity: O(n)
# Space complexity: O(1)
    
# With sort
# Time complexity: O(nlogn)
# Space complexity: O(1)
def solve(input: List[int]) -> Tuple[List[List[int]], List[State]]:
    # handle edge case
    if len(input) == 0:
        return [], []

    # since the problem statement didn't ensure that it's sorted
    input.sort()

    # initialize the state variables
    states = []
    output = []
    start_idx = 0
    end_idx = 1
    states.append(State(input, start_idx, end_idx, output.copy()))

    while end_idx < len(input):
        if input[end_idx] != input[end_idx-1] + 1:
            output.append([input[start_idx], input[end_idx-1]])
            start_idx = end_idx
        states.append(State(input, start_idx, end_idx, output.copy()))
        end_idx += 1

    output.append([input[start_idx], input[end_idx-1]])
    states.append(State(input, start_idx, end_idx, output.copy()))
    return output, states

if __name__ == '__main__':
    input = [1,3,4,5,7]
    output, states = solve(input)
    print(f'the answer of input {input} is {output}')
    for state in states:
        print(state)