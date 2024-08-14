#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy as np
import simmosq as sm
import unittest

class TestSimulationController(unittest.TestCase):
    """
    Test 'SimulationController' class. 
    """
    def test__init__(self):
        mosquitoes = sm.Mosquitoes(positions = [[0,0]])
        with self.assertRaises(TypeError):
            sm.SimulationController(mosquitoes=[0,0], model_mosq_movement=sm.RandomDiffusion)
            sm.SimulationController(mosquitoes=mosquitoes, model_mosq_movement= "RandomDiffusion")
            sm.SimulationController(mosquitoes=mosquitoes, model_mosq_movement=sm.RandomDiffusion,
                                    model_trapping="ForwardModelTrap")
            sm.SimulationController(mosquitoes=mosquitoes, model_mosq_movement=sm.RandomDiffusion,
                                    simulation_domain="Symmetric")


    def test_run(self):

        end_time = 10
        model = sm.RandomDiffusion()
        mosquitoes = sm.Mosquitoes(positions=[[0,0]])
        trap = sm.RadialTrap(position = [0,0],
                                   trapping_parameters={'R' : 0.1, 'trap_prob':0.1})
        simulation = sm.SimulationController(mosquitoes=mosquitoes, model_mosq_movement=model,
                                             model_trapping=trap)
        test_parameters = {'covariance_matrix': np.diag([1,1]), 
                           'death_prob': 0.1}
        
        #end_time must be an integer
        with self.assertRaises(TypeError):
            simulation.run(parameters=test_parameters, end_time=1.5)

        output = simulation.run(parameters = test_parameters, end_time = end_time)

        #Check output length - the 10 steps + initial
        self.assertEqual(len(output), 11)


