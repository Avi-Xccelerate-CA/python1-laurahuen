# week 0 problem 1
# create a function that returns a list of (vitamins, injections) tuples for each attribute that they need.
# Complete problem statement in README.mds

# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful


from typing import List, Tuple, Union

Result = Union[str, List[Tuple[int, int]]]

def dose(needs: List[int]) -> Result:
    if not isinstance(needs, (list, tuple)) or len(needs) != 6:
        return "No medicine given"

    if any((not isinstance(n, int)) or n < 0 or n >= 250 for n in needs):
        return "No medicine given"

    if sum(needs) >= 500:            
        return "No medicine given"
    
    result: List[Tuple[int, int]] = []
    for n in needs:
        vitamins = (n + 9) // 10      
        injections = vitamins * 10 - n 
        result.append((vitamins, injections))

    return result
