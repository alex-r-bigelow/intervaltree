from __future__ import absolute_import
from intervaltree import Interval, IntervalTree
import pytest

def test_simple_histogram():
    tree = IntervalTree([
        Interval(10, 30),
        Interval(20, 60),
        Interval(40, 50),
        Interval(10, 40)
    ])
    histogram = tree.computeHistogram(5)
    expectedResult = [
        Interval(10.0, 20.0, 2),
        Interval(20.0, 30.0, 3),
        Interval(30.0, 40.0, 3),
        Interval(40.0, 50.0, 3),
        Interval(50.0, 60.0, 2)
    ]
    for i in range(5):
        assert histogram[i].begin == expectedResult[i].begin
        assert histogram[i].end == expectedResult[i].end
        assert histogram[i].data == expectedResult[i].data

if __name__ == "__main__":
    test_simple_histogram()
    pytest.main([__file__, '-v'])
