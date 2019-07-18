from __future__ import absolute_import
from intervaltree import Interval, IntervalTree
from test import data
import pytest

def round_large(histogram):
    '''
    Helper function for cleaner results / to avoid
    floating point precision irregularities
    '''
    result = []
    for i in histogram:
        result.append(Interval(round(i.begin, 2),
                               round(i.end, 2),
                               round(i.data, 2)))
    return result

def test_simple_histogram():
    tree = IntervalTree.from_tuples(data.histograms.tiny)
    histogram = tree.computeCountHistogram(5)
    expectedResult = [
        Interval(10.0, 20.0, 2),
        Interval(20.0, 30.0, 3),
        Interval(30.0, 40.0, 2),
        Interval(40.0, 50.0, 2),
        Interval(50.0, 60.0, 1)
    ]
    assert histogram == expectedResult

def test_sub_histogram():
    tree = IntervalTree.from_tuples(data.histograms.tiny)
    histogram = tree.computeCountHistogram(2, 20, 40)
    expectedResult = [
        Interval(20.0, 30.0, 3),
        Interval(30.0, 40.0, 2)
    ]
    assert histogram == expectedResult

def test_single_bin_histogram():
    tree = IntervalTree.from_tuples(data.histograms.tiny)
    histogram = tree.computeCountHistogram(1)
    expectedResult = [
        Interval(10.0, 60.0, 4)
    ]
    assert histogram == expectedResult

def test_large_count_histogram():
    tree = IntervalTree.from_tuples(data.ivs3.data)
    histogram = tree.computeCountHistogram(10)
    expectedResult = IntervalTree.from_tuples(data.histograms.large_count)
    assert IntervalTree.from_tuples(round_large(histogram)) == expectedResult

def test_tiny_utilization():
    tree = IntervalTree.from_tuples(data.histograms.tiny)
    histogram = tree.computeUtilizationHistogram(5)
    expectedResult = [
        Interval(10.0, 20.0, 2.0),
        Interval(20.0, 30.0, 3.0),
        Interval(30.0, 40.0, 2.0),
        Interval(40.0, 50.0, 2.0),
        Interval(50.0, 60.0, 1.0)
    ]
    assert histogram == expectedResult

def test_large_utilization_histogram():
    tree = IntervalTree.from_tuples(data.ivs3.data)
    histogram = tree.computeUtilizationHistogram(10)
    expectedResult = IntervalTree.from_tuples(data.histograms.large_utilization)
    assert IntervalTree.from_tuples(round_large(histogram)) == expectedResult

def test_empty_histogram():
    tree = IntervalTree()
    expectedResult = [
        Interval(0.0, 0.25, 0.0),
        Interval(0.25, 0.5, 0.0),
        Interval(0.5, 0.75, 0.0),
        Interval(0.75, 1.0, 0.0)
    ]
    assert tree.computeCountHistogram(4) == expectedResult
    assert tree.computeUtilizationHistogram(4) == expectedResult

if __name__ == "__main__":
    pytest.main([__file__, '-v'])
