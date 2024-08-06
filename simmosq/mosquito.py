#
# Mosquito Class
#
# This file is part of simmosq
# (https://github.com/I-Bouros/simmosq.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#


class Mosquito(object):
    """
    """
    def __init__(self, position):
        self._position = position
        self._trapped = False

    def update_position(self, new_position):
        """
        """
        self._position = new_position

    def get_trapped(self):
        """
        """
        self._trapped = True
        return self._position