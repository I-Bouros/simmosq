#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy as np
import simmosq as sm
import unittest
import pandas as pd

class TestForwardModelTrap(unittest.TestCase):
    """
    Test the 'ForwardModelTrap' class.
    """

    def test__init__(self):
        test_parameters = {'R': 0.1, 'trap_prob': 0.1}
        trap = sm.ForwardModelTrap(position=[0,0], trapping_parameters=test_parameters)
        self.assertEqual(trap._position, [0,0])

    def test_attract_mosquitoes(self):
        test_parameters = {'R': 0.1, 'trap_prob': 0.1}
        trap = sm.ForwardModelTrap(position=[0,0], trapping_parameters=test_parameters)
        mosquitoes = sm.Mosquitoes(positions=[[0,0]])
        with self.assertRaises(NotImplementedError):
            trap.attract_mosquitoes(mosquitoes=mosquitoes)


class TestRadialTrap(unittest.TestCase):
    """
    Test the 'RadialTrap' class.
    """

    def test__init__(self):
        test_parameters = {'R': 0.1, 'trap_prob': 0.1}
        trap = sm.RadialTrap(position=[0,0], trapping_parameters=test_parameters)
        self.assertEqual(trap._R, 0.1)
        self.assertEqual(trap._position, [0,0])
        self.assertEqual(trap._trap_prob, 0.1)
        self.assertEqual(len(trap._has_trapped), 0)

    def test_attract_mosquitoes(self):
        test_parameters = {'R': 0.1, 'trap_prob': 0.1}
        mosquitoes = sm.Mosquitoes(positions = [[0, 0] for _ in range(10000)])
        trap = sm.RadialTrap(position=[0,0], trapping_parameters=test_parameters)
        trap.attract_mosquitoes(mosquitoes=mosquitoes)
        #Has trapped should now have shape (1,1)
        self.assertEqual(trap._has_trapped.shape, (1,1))
