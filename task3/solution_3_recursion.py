
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
import string
from typing import Dict, List, Tuple

# @dataclass
# class State:
#     input: List[int]
#     left_pnt: int
#     max_left_height: int
#     right_pnt: int
#     max_right_height: int
#     sand: int

# """
# This get longest common substring seems hard to explain. Let's get the simple case first.

# str1 = "a"
# str2 = "a"

# """

@dataclass
class State:
    str1: str
    str2: str
    str1_idx: int
    str2_idx: int
    longest_common_substring: str
    
  
def get_longest_common_substring(str1: str, str2: str) -> string:
    tracking = {
      'max_length': 0,
      'substring_pos': (0, 0)
    }
    memo = [[-1 for _ in range(len(str2))] for _ in range(len(str1))]

    def recursive(str1: str, str2: str, str1_idx: int, str2_idx: int) -> int:
        if str1_idx == -1 or str2_idx == -1 :
            return 0
        if memo[str1_idx][str2_idx] != -1:
            return memo[str1_idx][str2_idx]
        
        
        recursive(str1, str2, str1_idx, str2_idx-1) # traverse 2 paths and remember the result
        recursive(str1, str2, str1_idx-1, str2_idx)
        local_max = recursive(str1, str2, str1_idx-1, str2_idx-1) + 1 # visit other nodes first

        char1 = str1[str1_idx]
        char2 = str2[str2_idx]
        if (char1 == char2):
            local_max = recursive(str1, str2, str1_idx-1, str2_idx-1) + 1
            if local_max > tracking['max_length']:
                tracking['max_length'] = local_max
                tracking['substring_pos'] = (str1_idx, str2_idx)
            memo[str1_idx][str2_idx] = local_max
            return local_max
        else:
            return 0
        
    recursive(str1, str2, len(str1)-1, len(str2)-1)
    return str1[tracking['substring_pos'][0]-tracking['max_length']+1: tracking['substring_pos'][0]+1]
    


# Time complexity: TODO
# Space complexity: TODO
def solve(input: List[Tuple[int, str, str]]) -> Dict[int, str]:
    output = []
    for id, str1, str2 in input:
        result = get_longest_common_substring(str1, str2)
        output.append((id, result))
    return output
    

if __name__ == '__main__':
    input_data = [
        # (1, "ascascaacsacasc", "kopkopaacskopko"),

        (1, "a", "a"),
        # (2, "Thisisadocumentcontainingpatienthistory", "Theletteringinthisstoryisquite unique"),
        # (3, "abcdefgxyz123", "xyz789abcdef"),
        # (4, "The adventurous cat explored the mysterious cave.", "A curious cat ventured into the dark cave for exploration."),
        # (5, "Sunflowers bloomed in the radiant sunlight.", "Radiant sunlight illuminated the field of blooming sunflowers."),
        # (6, "Gentle waves lapped against the sandy shore.", "The shore echoed with the soothing sounds of lapping waves.")
    ]
    # output = solve(input_data)
    # print(f'the answer of input {input_data} is {output}')
    # for state in states:
    #     print(state)

    print(get_longest_common_substring('aa','aab'))