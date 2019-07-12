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
    histogram = tree.computeCountHistogram(5)
    expectedResult = [
        Interval(10.0, 20.0, 2),
        Interval(20.0, 30.0, 3),
        Interval(30.0, 40.0, 2),
        Interval(40.0, 50.0, 2),
        Interval(50.0, 60.0, 1)
    ]
    assert len(histogram) == len(expectedResult)
    for i in range(5):
        assert histogram[i].begin == expectedResult[i].begin
        assert histogram[i].end == expectedResult[i].end
        assert histogram[i].data == expectedResult[i].data

def test_sub_histogram():
    tree = IntervalTree([
        Interval(10, 30),
        Interval(20, 60),
        Interval(40, 50),
        Interval(10, 40)
    ])
    histogram = tree.computeCountHistogram(2, 20, 40)
    expectedResult = [
        Interval(20.0, 30.0, 3),
        Interval(30.0, 40.0, 2)
    ]
    assert len(histogram) == len(expectedResult)
    for i in range(2):
        print(histogram[i], expectedResult[i])
        assert histogram[i].begin == expectedResult[i].begin
        assert histogram[i].end == expectedResult[i].end
        assert histogram[i].data == expectedResult[i].data

def test_single_bin_histogram():
    tree = IntervalTree([
        Interval(10, 30),
        Interval(20, 60),
        Interval(40, 50),
        Interval(10, 40)
    ])
    histogram = tree.computeCountHistogram(1)
    expectedResult = [
        Interval(10.0, 60.0, 4)
    ]
    assert len(histogram) == len(expectedResult)
    assert histogram[0].begin == expectedResult[0].begin
    assert histogram[0].end == expectedResult[0].end
    assert histogram[0].data == expectedResult[0].data

if __name__ == "__main__":
    test_simple_histogram()
    test_sub_histogram()
    test_single_bin_histogram()
    pytest.main([__file__, '-v'])
