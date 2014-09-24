import unittest

import numpy as np

import experiment

class TestProbability(unittest.TestCase):
    def testDiePmf(self):
        expectedOutput = np.array([
            0.        ,  0.        ,  0.        ,  0.00462963,  0.01388889,
            0.02777778,  0.0462963 ,  0.06944444,  0.09722222,  0.11574074,
            0.125     ,  0.125     ,  0.11574074,  0.09722222,  0.06944444,
            0.0462963 ,  0.02777778,  0.01388889,  0.00462963
            ])

        output = experiment.diePmf( 3, 6 )

        np.testing.assert_allclose( expectedOutput, output )

    def testSumPmf(self):
        pmf1 = np.array([
            0         ,  0.5       ,  0.5
            ])
        pmf2 = np.array([
            0         ,  0.5       ,  0.5
            ])
        expectedOutput = np.array([
            0         ,  0         ,  0.25      ,  0.5       ,  0.25 
            ])

        output = experiment.sumPmf( pmf1, pmf2 )

        np.testing.assert_allclose( expectedOutput, output )

    def testCdf(self):
        pmf = np.array([
            0.        ,  0.5       ,  0.5
            ])
        expectedOutput = np.array([
            0.        ,  0.5       ,  1.
            ])

        output = experiment.cdf( pmf )

        np.testing.assert_allclose( expectedOutput, output )
