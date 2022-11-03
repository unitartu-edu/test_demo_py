#!/usr/bin/env python3
import unittest
import rostest

#from test_demo_py import Counter
from test_demo_py.counter import Counter

## A python unit test for the Counter class
class CounterTestClass(unittest.TestCase):

    def test_increment(self):
        counter = Counter()
        counter.increment(3)
        self.assertEquals(counter.counter_value, 3, "Oh no, counter_value has not increased by 3")

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('test_demo', 'test_counter_increment', CounterTestClass)

