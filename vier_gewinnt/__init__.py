"""
Vier Gewinnt - Ein klassisches Strategiespiel.

Dieses Package enthält die Implementation des Spiels Vier Gewinnt
mit Unterstützung für zwei menschliche Spieler oder gegen den Computer.
"""

from vier_gewinnt.spielbrett import Spielbrett
from vier_gewinnt.spieler import Spieler, MenschlicherSpieler, ComputerSpieler
from vier_gewinnt.spiel import Spiel

__all__ = ['Spielbrett', 'Spieler', 'MenschlicherSpieler', 'ComputerSpieler', 'Spiel']
