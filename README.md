Each task have three files:

- solution_n.py: This file contains the actual code to solve the task.
- test_n.py: It includes unit test cases that help ensure the correctness of the result.
- presentation_n.ipynb: This file contains the code responsible for displaying states.
- presentation_n.html: It exports the visualized result from the Jupyter notebook.
- 
Note: 
- [Task3] I have solution_3_recursion.py for solving this problem with recursive + memoization. However, the presentation doesn't look good and is not easy to understand. To improve it, we need to record the state twice: before recursion and after recursion.
- [Task3] I disabled state recording because when it prints, it is really hard to read. To enable it, pass `is_state_record` as True to the `get_longest_common_substring` function.