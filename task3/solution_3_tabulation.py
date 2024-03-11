
# 3. By using the dataset given below, create a dataset containing all the common
# substrings between String_1 and String_2 for each ID and use it to identify the
# longest common substring. (Please show the intermediate table containing all the
# common substrings)
# | ID | String_1                                           | String_2                                                      |
# |----|----------------------------------------------------|---------------------------------------------------------------|
# | 1  | ababbacdee                                         | haababadeedc                                                  |
# | 2  | Thisisadocumentcontainingpatienthistory            | Theletteringinthisstoryisquite unique                         |
# | 3  | abcdefgxyz123                                      | xyz789abcdef                                                  |
# | 4  | The adventurous cat explored the mysterious cave.  | A curious cat ventured into the dark cave for exploration.    |
# | 5  | Sunflowers bloomed in the radiant sunlight.        | Radiant sunlight illuminated the field of blooming sunflowers.|
# | 6  | Gentle waves lapped against the sandy shore.       | The shore echoed with the soothing sounds of lapping waves.   |

# Present the final output in the following form:
# | ID | Longest_common_substring |
# |----|--------------------------|
# | 1  | abab                     |


from dataclasses import dataclass
from typing import Dict, List, Tuple
import copy
import pandas as pd
import os

@dataclass
class State:
    str1: str
    str2: str
    str1_idx: int
    str2_idx: int
    table: List[List[int]]
    max_length: int
    max_substring_pos: Tuple[int, int]


def get_longest_common_substring(str1: str, str2: str, is_state_record: bool = False) -> Tuple[str, List[State]]:
   
    # create a global state variables
    # - add extra +1 from len to pad, so that I don't have to check edge in loop
    # - table store the max lenght of longest common substring that `ends` on that position
    table = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    states = []
    max_length = 0
    max_substring_pos = (0,0)

    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            str1_idx = i-1
            str2_idx = j-1
            char1 = str1[str1_idx]
            char2 = str2[str2_idx]
            if is_state_record:
                states.append(State(str1, str2, str1_idx, str2_idx, copy.deepcopy(table), max_length, max_substring_pos))
            if char1 != char2:
                table[i][j] = 0
            else:
                local_max_length = table[i-1][j-1] + 1
                table[i][j] = local_max_length
                if local_max_length > max_length:
                    max_length = local_max_length
                    max_substring_pos = (i,j)
    
    return (str1[max_substring_pos[0]-max_length: max_substring_pos[0]], states)

def read_excel() -> List[Tuple[int, str, str]]:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    input_file = os.path.join(current_dir, 'in', 'longest_common_substring_in.xlsx')

    df = pd.read_excel(input_file)

    data = [(row[0], str(row[1]), str(row[2])) for row in df.iloc[:, :3].values]
    return data

# n = size of list
# i, j = length of str1, and str2
# Time complexity: n * i * j
# Space complexity: i * j
def solve(input: List[Tuple[int, str, str]]) -> List[Tuple[int, str]]:
    output = []
    for id, str1, str2 in input:
        result, _ = get_longest_common_substring(str1, str2)
        output.append((id, result))
    return output
    

if __name__ == '__main__':
    input_data = read_excel()

    output = solve(input_data)
    print(f'The output is {output}')

    df = pd.DataFrame(output, columns=['ID', 'Longest_Common_Substring'])

    current_dir = os.path.dirname(os.path.realpath(__file__))
    output_file = os.path.join(current_dir, 'out', 'longest_common_substring.xlsx')
    df.to_excel(output_file, index=False)
