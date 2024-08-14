#
# ForwardModelTrap Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy.random as random
from simmosq import Mosquitoes
from scipy.spatial.distance import cdist
import pandas as pd


class ForwardModelTrap(object):
    """
    """
    def __init__(self, position, trapping_parameters):
        self._position = position


    def attract_mosquitoes(self, mosquitoes):
        """
        """
        raise NotImplementedError


class RadialTrap(ForwardModelTrap):
    """
    """
    def __init__(self, position, trapping_parameters):
        self._position = position
        self._R = trapping_parameters['R']
        self._trap_prob = trapping_parameters['trap_prob']
        self._has_trapped = pd.DataFrame([], columns=["Has.trapped"])

    def attract_mosquitoes(self, mosquitoes):
        """
        """

        trapped = 0

        for _ in range(mosquitoes._n_mosquitoes):
            #Dead mosquitoes can't be trapped
            if not mosquitoes._dead[_] and not mosquitoes._trapped[_]:
                #Checking if each mosquito is close to a trap and if those are trapped
                if cdist([self._position], [mosquitoes._positions[_]], 'euclidean') < self._R:
                    u = random.uniform(0,1,1)
                    if u < self._trap_prob:
                        position_trapping = mosquitoes.become_trapped(_)
                        trapped += 1

        self._has_trapped = pd.concat([self._has_trapped, pd.DataFrame([trapped], columns=["Has.trapped"])], ignore_index=True)
#Not currently sure if storing in dataframe like this is the cleanest way to do it
