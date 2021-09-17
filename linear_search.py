def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    return -1


result = linear_search([], None)
print(result)


def test_linear_search():
    test_cases = [
        {
            'name': 'Simple Case 1',
            'L_input': [3, 2, 6, 2, 3, 7, 9, 33],
            'x_input': 7,
            'expected': 5,
        },
        {
            'name': 'Simple Case 2',
            'L_input': [5, 3, 7, 3, 9, 8, 6, 2, 11, 27, 93, 83],
            'x_input': 3,
            'expected': 1,
        },
        {
            'name': 'List with 1 element',
            'L_input': [77],
            'x_input': 77,
            'expected':  0,
        },
        {
            'name': 'List with 0 element',
            'L_input': [],
            'x_input': None,
            'expected': -1,
        },
        {
            'name': 'This list has no expected element',
            'L_input': [1, 2, 3, 4, 100],
            'x_input': 101,
            'expected': -1,
        }
    ]

    for test_case in test_cases:
        assert test_case['expected'] == linear_search(
            test_case['L_input'], test_case['x_input']
        ), test_case['name']
