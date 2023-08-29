#!/usr/bin/env python3
from enum import Enum

class GameState(Enum):
    DRAW = 0
    P1_WON = 1
    P2_WON = 2
    ONGOING = 3
    # INVALID = 4

    def check_if_won():
        pass

    def check_if_draw():
        pass

    def check_if_ongoing():
        pass

