import unittest
import numpy as np
# Wir importieren unsere Spielbrett-Klasse
from vier_gewinnt.spielbrett import Spielbrett


class TestSpielbrett(unittest.TestCase):

    def setUp(self):
        # Wird vor jedem Test aufgerufen, damit wir immer ein frisches Brett haben
        self.brett = Spielbrett()

    def test_initialisierung(self):
        # Prüfen ob das Brett am Anfang wirklich leer ist (nur Nullen)
        self.assertEqual(self.brett.zeilen, 6)
        self.assertEqual(self.brett.spalten, 7)
        self.assertTrue(np.all(self.brett.brett == 0))

    def test_stein_setzen(self):
        # Wir setzen einen Stein in Spalte 3
        erfolg = self.brett.stein_setzen(3, "X")
        self.assertTrue(erfolg)
        # Der Stein muss in der untersten Zeile (Index 5) landen
        self.assertEqual(self.brett.brett[5][3], 1)

    def test_spalte_voll(self):
        # Wir machen Spalte 0 absichtlich voll
        for i in range(6):
            self.brett.stein_setzen(0, "X")

        # Jetzt darf die Spalte nicht mehr gültig sein
        self.assertFalse(self.brett.ist_spalte_gueltig(0))
        # Ein weiterer Stein darf nicht gesetzt werden können
        self.assertFalse(self.brett.stein_setzen(0, "O"))

    def test_horizontaler_sieg(self):
        # Wir bauen eine Reihe von 4 Steinen horizontal
        for s in range(4):
            self.brett.stein_setzen(s, "X")

        self.assertTrue(self.brett.hat_gewonnen("X"))

    def test_vertikaler_sieg(self):
        # Wir stapeln 4 Steine übereinander in Spalte 5
        for _ in range(4):
            self.brett.stein_setzen(5, "O")

        self.assertTrue(self.brett.hat_gewonnen("O"))

    def test_unentschieden(self):
        # Hier testen wir nur kurz, ob das Brett erkennt, wenn es NICHT voll ist
        self.assertFalse(self.brett.ist_voll())


if __name__ == '__main__':
    unittest.main()