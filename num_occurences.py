from typing import List


def unique_occurrences(arr: List[int]) -> bool:
    occurrences = {}

    for a in arr:
        if not a in occurrences:
            occurrences[a] = 0
        occurrences[a] += 1

    return len(set(occurrences.values())) == len(occurrences.keys())


assert unique_occurrences([1,2,3,1,2,1])
assert not unique_occurrences([1,2])
assert unique_occurrences([4,4,0,0,0,1,0,1,5,6,6,1,4,4,0])
