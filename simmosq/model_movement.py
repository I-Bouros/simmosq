#
# ForwardModelMosqMov Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

from simmosq import Mosquitoes
import scipy.stats
import copy


class ForwardModelMosqMov(object):
    """
    """
    def __init__(self):
        super(ForwardModelMosqMov, self).__init__()

    def simulate_step(self, mosquitoes, parameters):
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
        super(ForwardModelMosqMov, self).__init__()

    def simulate_step(self, mosquitoes, parameters):
        """
        """
        covariance = parameters['covariance_matrix']

        positions = mosquitoes._positions

        # Propose new positions for the mosquitoes
        new_positions = copy.deepcopy(positions)

        for _ in range(mosquitoes._n_mosquitoes):
            if not mosquitoes._trapped[_] or not mosquitoes._dead[_]:
                new_positions[_] = scipy.stats.multivariate_normal.rvs(
                    positions[_], covariance).tolist()

        return new_positions
