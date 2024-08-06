#
# SimulationController Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy as np

from simmosq import ForwardModelMosqMov, ForwardModelTrap


class SimulationController:
    """SimulationController Class:
    Class for the simulation of models in any of the subclasses in the
    ``ForwardModel``.

    Parameters
    ----------
    model
        (ForwardModel) Instance of the :class:`ForwardModel` class used for
        the simulation.
    start_sim_time
        (integer) Time from which we start running the SimulationController.
    end_sim_time
        (integer) Time at which we stop running the SimulationController.

    Notes
    -----
    Always apply method switch_resolution before calling
    :meth:`SimulationController.run` for a change of resolution!

    """

    def __init__(self, model_mosq_movement, model_trapping, simulation_domain):
        if not isinstance(model_mosq_movement, ForwardModelMosqMov):
            raise TypeError(
                'Model for mosquito movement needs to be a subclass of the simmosq.ForwardModelMosqMov')
        if not isinstance(model_trapping, ForwardModelTrap):
            raise TypeError(
                'Model for trapping needs to be a subclass of the simmosq.ForwardModelTrap')
        if not isinstance(simulation_domain, SimulationDomain):
            raise TypeError(
                'Simulation domain needs to be a subclass of the simmosq.SimulationDomain')

        self._model_mosq_movement = model_mosq_movement
        self._model_trapping = model_trapping
        self._simulation_domain = simulation_domain

    def switch_resolution(self, step_size):
        """
        Change the number of points we wish to keep from our simulated sample
        of incidences.

        Parameters
        ----------
        num_points
            (integer) number of points we wish to keep from our simulated
            sample of incidences.

        """
        start_sim_time, end_sim_time = self._sim_end_points
        self._regime = np.rint(np.linspace(
            start_sim_time, end_sim_time, num=num_points)).astype(int)

    def get_regime(self):
        """
        Gets all time point the simulation uses.
        """
        return self._regime

    def get_time_bounds(self):
        """
        Gets time bounds of the simulation as a tuple with start and end time
        of the simulation.
        """
        return self._sim_end_points

    def run(self, parameters):
        """
        Operates the ``simulate`` method present in any subclass of the
        ``ForwardModel``.

        Parameters
        ----------
        parameters
            An ordered sequence of parameter values.

        """
        return self.model.simulate(parameters, self._regime)
