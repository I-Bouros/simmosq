#
# Mosquitoes Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy as np


class Mosquitoes(object):
    """
    """
    def __init__(self, positions):
        self._positions = positions
        self._trapped = [False] * np.array(positions).shape[0]
        self._dead = [False] * np.array(positions).shape[0]
        self._n_mosquitoes = len(self._trapped)

    def update_positions(self, new_positions):
        """
        """
        self._positions = new_positions

    def update_one_position(self, index_mosquito, new_position):
        """
        """
        self._positions[index_mosquito] = new_position

    def become_trapped(self, index_mosquito):
        """
        """
        self._trapped[index_mosquito] = True
        return self._positions[index_mosquito]

    def die(self, index_mosquito):
        """
        """
        self._dead[index_mosquito] = True