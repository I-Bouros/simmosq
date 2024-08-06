#
# SimulationDomain Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#


class SimulationDomain(object):
    """
    """
    def __init__(self, traps):
        self._traps = traps

    def get_traps_positions(self):
        return self._traps

    def get_local_diffusion_rate(self, position):
        pass