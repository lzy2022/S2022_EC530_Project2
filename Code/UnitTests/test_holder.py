import sys
import os
# adding the parent directory to
# the sys.path.
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_1():
    print('Test Holer\n')
    assert 1 == 1
