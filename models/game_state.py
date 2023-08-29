#!/usr/bin/env python3
from enum import Enum

class GameState(Enum):
    DRAW = 0
    P1_WON = 1
    P2_WON = 2
    ONGOING = 3
    # INVALID = 4

    # TODO : create function
    def check_if_won():
        pass

    # TODO : create function
    def check_if_draw():
        pass

    # TODO : create function
    def check_if_ongoing():
        pass

