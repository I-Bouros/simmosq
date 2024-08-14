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

class TestMosquitoes(unittest.TestCase):
    """
    Test the 'Mosquitoes' class.
    """

    def test__init__(self):
        mosquitoes = sm.Mosquitoes(positions=[[0,0]])
        self.assertEqual(mosquitoes._dead, [False])
        self.assertEqual(mosquitoes._n_mosquitoes, 1)
        self.assertEqual(mosquitoes._trapped, [False])
        self.assertEqual(mosquitoes._positions, [[0,0]])
    
    def test_update_positions(self):
        mosquitoes = sm.Mosquitoes(positions=[[0,0]])
        mosquitoes.update_positions([[1,1]])
        self.assertEqual(mosquitoes._positions, [[1,1]])

    def test_update_one_position(self):
        mosquitoes = sm.Mosquitoes(positions=[[0,0], [0,0], [0,0]])
        mosquitoes.update_one_position(1, [1,1])
        self.assertEqual(mosquitoes._positions, [[0,0], [1,1], [0,0]])

    def test_become_trapped(self):
        mosquitoes = sm.Mosquitoes(positions=[[0,0], [0,0], [0,0]])
        mosquitoes.become_trapped(2)
        self.assertEqual(mosquitoes._trapped, [False, False, True])

    def test_die(self):
        mosquitoes = sm.Mosquitoes(positions=[[0,0], [0,0], [0,0]])
        mosquitoes.die(0)
        self.assertEqual(mosquitoes._dead, [True, False, False])