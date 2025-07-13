from week0 import dose
import pytest

testdata =[
    ([250, 0, 250, 0, 0, 0],  "No medicine given"),
    ([40,35,23,68,45,29], [(4, 0), (4, 5), (3, 7), (7, 2), (5, 5), (3, 1)]),
    ([223, 12, 126, 0, 37, 12], [(23, 7), (2, 8), (13, 4), (0, 0), (4, 3), (2, 8)])
]

@pytest.mark.parametrize("case, expected", testdata)
def test_ex2(case, expected):
	assert dose(case) == expected

