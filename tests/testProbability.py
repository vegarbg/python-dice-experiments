import unittest

import numpy as np

import experiment

class TestProbability(unittest.TestCase):
    def testDiePmf(self):
        expectedOutput = np.array([
            0.,          0.        ,  0.        ,  0.00462963,  0.01388889,
            0.02777778,  0.0462963 ,  0.06944444,  0.09722222,  0.11574074,
            0.125     ,  0.125     ,  0.11574074,  0.09722222,  0.06944444,
            0.0462963 ,  0.02777778,  0.01388889,  0.00462963
            ])

        output = experiment.diePmf( 3, 6 )

        np.testing.assert_allclose( expectedOutput, output )
