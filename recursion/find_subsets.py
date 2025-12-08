# Find All Subsets of a Set
# -	Problem: Write a recursive function find_subsets(lst) that returns all possible subsets of a given list of unique elements.
# -	Example: find_subsets([1, 2]) should return [[], [1], [2], [1, 2]].


def find_subsets(lst):
    # Base case: empty list → one subset (the empty set)
    if not lst:
        return [[]]

    first = lst[0]        # the first element
    rest = lst[1:]        # the rest of the list

    # Recursively get all subsets of the smaller list
    subsets_without_first = find_subsets(rest)

    # Build new subsets that include the first element
    subsets_with_first = []
    for subset in subsets_without_first:
        subsets_with_first.append([first] + subset)

    # Combine and return all subsets
    return subsets_without_first + subsets_with_first

# ------------
def find_subsets(lst):
    if not lst:
        return [[]]
    
    rest_subsets = find_subsets(lst[1:])
    return rest_subsets + [[lst[0]] + s for s in rest_subsets]






# -------------------------
# FINAL RECURSIVE SOLUTION
def find_subsets(lst):
    # Base case: empty list → one subset (the empty set)
    if not lst:
        return [[]]

    first = lst[0]
    rest = lst[1:]

    # Recursively get subsets of the smaller list
    subsets_without_first = find_subsets(rest)

    # Create new subsets that include the first element
    subsets_with_first = []
    for subset in subsets_without_first:
        subsets_with_first.append([first] + subset)

    # Combine both sets of subsets
    return subsets_without_first + subsets_with_first