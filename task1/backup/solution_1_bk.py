# 1. For any list of integers, develop an approach to summarize the boundaries of any
# continuous series (the start and end of the continuous series).
# Example:
# Input: [1,3,4,5,7]
# Output: [[1,1],[3,5],[7,7]]


from typing import Callable, List


def solve(input: List[int], visualizer: Callable[[List[int], int, int, List[List[int]]], None]) -> List[List[int]]:
    # handle edge case
    if len(input) == 0:
        return []

    # since the problem statement didn't ensure that it's sorted
    input.sort()

    # initialize the state variables
    output = []
    start_idx = 0
    end_idx = 1

    visualizer(input, start_idx, end_idx, output)
    while end_idx < len(input):
        if input[end_idx] != input[end_idx-1] + 1:
            output.append([input[start_idx], input[end_idx-1]])
            start_idx = end_idx
        end_idx += 1
        visualizer(input, start_idx, end_idx, output)

    output.append([input[start_idx], input[end_idx-1]])
    return output

if __name__ == '__main__':
    input = [1,3,4,5,7]
    print(f'the answer of input {input} is {solve(input)}')