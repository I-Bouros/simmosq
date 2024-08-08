#
# ForwardModelMosqMov Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy.random as random
from simmosq import Mosquitoes


class ForwardModelTrap(object):
    """
    """
    def __init__(self, position, trapping_parameters):
        self._position = position


    def attract_mosquito(self, mosquito):
        """
        """
        return NotImplemented


class RadialTrap(ForwardModelTrap):
    """
    """
    def __init__(self, position, trapping_parameters):
        self._position = position
        self._R = trapping_parameters['R']
        self._trap_prob = trapping_parameters['trap_prob']

    def attract_mosquito(self, mosquito):
        """
        """
        if distance(self._position, mosquito._position) < self._R:
            u = random.unif(1)
            if u < self._trap_prob:
                position_trapping = mosquito.get_trapped()
