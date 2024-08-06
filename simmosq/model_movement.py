#
# ForwardModelMosqMov Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

from simmosq import Mosquito


class ForwardModelMosqMov(object):
    """
    """
    def __init__(self):
        super(ForwardModelMosqMov, self).__init__()

    def simulate_step(self, state, simulation_domain, parameters):
        """
        Runs a forward simulation with the given ``parameters`` and returns a
        time-series with data points corresponding to the given ``times``.

        Returns a sequence of length ``n_times`` (for single output problems)
        or a NumPy array of shape ``(n_times, n_outputs)`` (for multi-output
        problems), representing the values of the model at the given ``times``.

        Parameters
        ----------
        parameters
            An ordered sequence of parameter values.
        times
            The times at which to evaluate. Must be an ordered sequence,
            without duplicates, and without negative values.
            All simulations are started at time 0, regardless of whether this
            value appears in ``times``.

        """
        raise NotImplementedError

class RandomDiffussion(ForwardModelMosqMov):
    """
    """
    def __init__(self):
        pass

    def simulate_step(self, state, simulation_domain, parameters):
        """
        """
        step_size = parameters['step_size']

        for i in range(n_mosquitoes):
            state = random.normal()

        return
