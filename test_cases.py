#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample_a (self):
                self.assertEqual (21, calc(3,7))

        def test_sample_b (self):
                self.assertEqual (21, calc(7,3))

        def test_sample_c (self):
                self.assertEqual (49, calc(7,7))

        def test_sample_d (self):
                self.assertEqual (-1, calc(1,'b'))
                
        def test_sample_e (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample_f (self):
                self.assertEqual (-1, calc(0,999))

        def test_sample_g (self):
                self.assertEqual (-1, calc(0,1000))

        def test_sample_h (self):
                self.assertEqual (-1, calc(1.1,999))

        def test_sample_i (self):
                self.assertEqual (-1, calc(1.1,1.2))


        
        def test_sample_j (self):
                self.assertEqual (-1, calc(1,2,3))

        def test_sample_k (self):
                self.assertEqual (-1, calc(1))



