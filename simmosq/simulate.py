#
# SimulationController Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import numpy as np
import copy

from simmosq import Mosquitoes, ForwardModelMosqMov, ForwardModelTrap, SimulationDomain


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

    def __init__(self, mosquitoes, model_mosq_movement, model_trapping=None, simulation_domain=None):
        if not isinstance(mosquitoes, Mosquitoes):
            raise TypeError(
                'The mosquito population needs to be of type simmosq.Mosquitoes.')

        if not isinstance(model_mosq_movement, ForwardModelMosqMov):
            raise TypeError(
                'Model for mosquito movement needs to be a subclass of the simmosq.ForwardModelMosqMov.')
        
        self._mosquitoes = mosquitoes
        self._model_mosq_movement = model_mosq_movement

        if model_trapping is not None:
            if not isinstance(model_trapping, ForwardModelTrap):
                raise TypeError(
                    'Model for trapping needs to be a subclass of the simmosq.ForwardModelTrap.')
            self._model_trapping = model_trapping

        if simulation_domain is not None:
            if not isinstance(simulation_domain, SimulationDomain):
                raise TypeError(
                    'Simulation domain needs to be of type simmosq.SimulationDomain.')
            self._simulation_domain = simulation_domain

    def run(self, parameters, end_time):
        """
        Operates the ``simulate`` method present in any subclass of the
        ``ForwardModel``.

        Parameters
        ----------
        parameters
            An ordered sequence of parameter values.

        """
        if not isinstance(end_time, int):
            raise TypeError(
                'Simulation time must be an integer.')

        list_of_mosquitoes = [copy.deepcopy(self._mosquitoes)]

        for _ in range(end_time):
            new_positions = self._model_mosq_movement.simulate_step(
                self._mosquitoes, parameters)

            self._mosquitoes.update_positions(new_positions)

            list_of_mosquitoes.append(copy.deepcopy(self._mosquitoes))

        return list_of_mosquitoes
