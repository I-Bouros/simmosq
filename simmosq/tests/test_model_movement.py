#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy as np
import simmosq as sm
import unittest

class TestForwardModelMosqMov(unittest.TestCase):
    """
    Test the 'ForwardModelMosqMov' class.
    """

    def test__init__(self):
        sm.ForwardModelMosqMov()
    
    def test_simulate_step(self):
        mosquitoes = sm.Mosquitoes(positions = [[0,0]])
        test_parameters = {'covariance_matrix': np.diag([1,1]), 
                           'death_prob': 0.1}
        forward_model = sm.ForwardModelMosqMov()
        with self.assertRaises(NotImplementedError):
            forward_model.simulate_step(mosquitoes=mosquitoes, parameters=test_parameters)


class TestRandomDiffusion(unittest.TestCase):
    """
    Test the 'RandomDiffusion' class.
    """

    def test__init__(self):
        sm.RandomDiffusion()

    def test_simulate_step(self):
        model = sm.RandomDiffusion()
        mosquitoes = sm.Mosquitoes(positions = [[0,0]])
        test_parameters = {'covariance_matrix': np.diag([1,1]), 
                           'death_prob': 0.1}
        
        output = model.simulate_step(mosquitoes=mosquitoes, parameters=test_parameters)
        #Only one mosquito so should give an output of length 1
        #(x coord and y coord in a nested list)
        self.assertEqual(len(output),1)