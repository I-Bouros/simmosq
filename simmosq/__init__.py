#
# Root of the simmosq module.
# Provides access to all shared functionality (models, simulation, etc.).
#
# This file is part of SIMMOSQ
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the BSD 3-clause license. See accompanying LICENSE.md for copyright
# notice and full license details.
#
"""simmosq is a Branching Processes modelling library.
It contains functionality for modelling, simulating, and visualising the
number of cases of infections by day during an outbreak of the influenza virus.
"""

# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .mosquitoes import Mosquitoes  # noqa

from .model_movement import ForwardModelMosqMov, RandomDiffussion  # noqa
from .model_trap import ForwardModelTrap, RadialTrap  # noqa

from .simulation_domain import SimulationDomain  # noqa
from .simulate import SimulationController  # noqa
