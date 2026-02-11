"""Unit Tests für das Spielbrett Modul."""

import unittest
from vier_gewinnt.spielbrett import Spielbrett


class TestSpielbrett(unittest.TestCase):
    """
    Testklasse für die Spielbrett Klasse.

    Testet die Spielzug-Validierung und Gewinnüberprüfung.
    """

    def setUp(self):
        """
        Wird vor jedem Test ausgeführt.

        Erstellt ein neues leeres Spielbrett.
        """
        self.brett = Spielbrett()

    def test_initialisierung(self):
        """
        Test: Spielbrett wird korrekt initialisiert.
        """
        self.assertEqual(self.brett.reihen, 6)
        self.assertEqual(self.brett.spalten, 7)
        self.assertEqual(len(self.brett.brett), 6)
        self.assertEqual(len(self.brett.brett[0]), 7)
        # Alle Felder sollten leer sein
        for reihe in self.brett.brett:
            for feld in reihe:
                self.assertEqual(feld, ' ')

    def test_ist_spalte_gueltig_leeres_brett(self):
        """
        Test: Alle Spalten sind auf leerem Brett gültig.
        """
        for spalte in range(7):
            self.assertTrue(self.brett.ist_spalte_gueltig(spalte))

    def test_ist_spalte_gueltig_ungueltige_spalte(self):
        """
        Test: Ungültige Spaltennummern werden erkannt.
        """
        self.assertFalse(self.brett.ist_spalte_gueltig(-1))
        self.assertFalse(self.brett.ist_spalte_gueltig(7))
        self.assertFalse(self.brett.ist_spalte_gueltig(10))

    def test_ist_spalte_gueltig_volle_spalte(self):
        """
        Test: Volle Spalten werden als ungültig erkannt.
        """
        # Spalte 3 komplett füllen
        for _ in range(6):
            self.brett.stein_einwerfen(3, 'X')
        
        self.assertFalse(self.brett.ist_spalte_gueltig(3))
        # Andere Spalten sollten noch gültig sein
        self.assertTrue(self.brett.ist_spalte_gueltig(2))
        self.assertTrue(self.brett.ist_spalte_gueltig(4))

    def test_stein_einwerfen_erfolg(self):
        """
        Test: Stein wird korrekt eingeworfen und landet unten.
        """
        reihe = self.brett.stein_einwerfen(3, 'X')
        self.assertEqual(reihe, 5)  # Unterste Reihe
        self.assertEqual(self.brett.brett[5][3], 'X')

    def test_stein_einwerfen_stapeln(self):
        """
        Test: Steine stapeln sich korrekt übereinander.
        """
        reihe1 = self.brett.stein_einwerfen(3, 'X')
        self.assertEqual(reihe1, 5)
        
        reihe2 = self.brett.stein_einwerfen(3, 'O')
        self.assertEqual(reihe2, 4)
        
        reihe3 = self.brett.stein_einwerfen(3, 'X')
        self.assertEqual(reihe3, 3)
        
        # Überprüfe dass alle Steine an der richtigen Position sind
        self.assertEqual(self.brett.brett[5][3], 'X')
        self.assertEqual(self.brett.brett[4][3], 'O')
        self.assertEqual(self.brett.brett[3][3], 'X')

    def test_stein_einwerfen_ungueltige_spalte(self):
        """
        Test: Einwerfen in ungültige Spalte wird abgelehnt.
        """
        reihe = self.brett.stein_einwerfen(-1, 'X')
        self.assertEqual(reihe, -1)
        
        reihe = self.brett.stein_einwerfen(7, 'X')
        self.assertEqual(reihe, -1)

    def test_stein_einwerfen_volle_spalte(self):
        """
        Test: Einwerfen in volle Spalte wird abgelehnt.
        """
        # Spalte 3 komplett füllen
        for i in range(6):
            reihe = self.brett.stein_einwerfen(3, 'X')
            self.assertNotEqual(reihe, -1)
        
        # Versuch in volle Spalte einzuwerfen
        reihe = self.brett.stein_einwerfen(3, 'O')
        self.assertEqual(reihe, -1)

    def test_pruefe_gewinn_horizontal(self):
        """
        Test: Horizontaler Gewinn wird erkannt.
        """
        # Vier 'X' in Reihe 5, Spalten 1-4
        for spalte in range(1, 5):
            self.brett.stein_einwerfen(spalte, 'X')
        
        self.assertTrue(self.brett.pruefe_gewinn('X'))
        self.assertFalse(self.brett.pruefe_gewinn('O'))

    def test_pruefe_gewinn_horizontal_verschiedene_positionen(self):
        """
        Test: Horizontaler Gewinn an verschiedenen Positionen.
        """
        # Teste am rechten Rand
        self.brett.zuruecksetzen()
        for spalte in range(3, 7):
            self.brett.stein_einwerfen(spalte, 'O')
        self.assertTrue(self.brett.pruefe_gewinn('O'))
        
        # Teste am linken Rand
        self.brett.zuruecksetzen()
        for spalte in range(0, 4):
            self.brett.stein_einwerfen(spalte, 'X')
        self.assertTrue(self.brett.pruefe_gewinn('X'))

    def test_pruefe_gewinn_vertikal(self):
        """
        Test: Vertikaler Gewinn wird erkannt.
        """
        # Vier 'O' vertikal in Spalte 3
        for _ in range(4):
            self.brett.stein_einwerfen(3, 'O')
        
        self.assertTrue(self.brett.pruefe_gewinn('O'))
        self.assertFalse(self.brett.pruefe_gewinn('X'))

    def test_pruefe_gewinn_vertikal_verschiedene_spalten(self):
        """
        Test: Vertikaler Gewinn in verschiedenen Spalten.
        """
        # Teste in Spalte 0
        for _ in range(4):
            self.brett.stein_einwerfen(0, 'X')
        self.assertTrue(self.brett.pruefe_gewinn('X'))
        
        # Teste in Spalte 6
        self.brett.zuruecksetzen()
        for _ in range(4):
            self.brett.stein_einwerfen(6, 'O')
        self.assertTrue(self.brett.pruefe_gewinn('O'))

    def test_pruefe_gewinn_diagonal_links_oben_rechts_unten(self):
        """
        Test: Diagonaler Gewinn (links-oben nach rechts-unten) wird erkannt.
        """
        # Erstelle diagonale Viererreihe
        # X
        # O X
        # O O X
        # O O O X
        self.brett.stein_einwerfen(0, 'O')
        self.brett.stein_einwerfen(0, 'O')
        self.brett.stein_einwerfen(0, 'O')
        self.brett.stein_einwerfen(0, 'X')
        
        self.brett.stein_einwerfen(1, 'O')
        self.brett.stein_einwerfen(1, 'O')
        self.brett.stein_einwerfen(1, 'X')
        
        self.brett.stein_einwerfen(2, 'O')
        self.brett.stein_einwerfen(2, 'X')
        
        self.brett.stein_einwerfen(3, 'X')
        
        self.assertTrue(self.brett.pruefe_gewinn('X'))
        self.assertFalse(self.brett.pruefe_gewinn('O'))

    def test_pruefe_gewinn_diagonal_rechts_oben_links_unten(self):
        """
        Test: Diagonaler Gewinn (rechts-oben nach links-unten) wird erkannt.
        """
        # Erstelle diagonale Viererreihe
        #       X
        #     X O
        #   X O O
        # X O O O
        self.brett.stein_einwerfen(3, 'X')
        
        self.brett.stein_einwerfen(2, 'O')
        self.brett.stein_einwerfen(2, 'X')
        
        self.brett.stein_einwerfen(1, 'O')
        self.brett.stein_einwerfen(1, 'O')
        self.brett.stein_einwerfen(1, 'X')
        
        self.brett.stein_einwerfen(0, 'O')
        self.brett.stein_einwerfen(0, 'O')
        self.brett.stein_einwerfen(0, 'O')
        self.brett.stein_einwerfen(0, 'X')
        
        self.assertTrue(self.brett.pruefe_gewinn('X'))
        self.assertFalse(self.brett.pruefe_gewinn('O'))

    def test_pruefe_gewinn_keine_viererreihe(self):
        """
        Test: Kein Gewinn wenn keine Viererreihe vorhanden.
        """
        # Drei in einer Reihe - kein Gewinn
        self.brett.stein_einwerfen(0, 'X')
        self.brett.stein_einwerfen(1, 'X')
        self.brett.stein_einwerfen(2, 'X')
        
        self.assertFalse(self.brett.pruefe_gewinn('X'))

    def test_pruefe_gewinn_unterbrochene_reihe(self):
        """
        Test: Unterbrochene Reihe wird nicht als Gewinn gewertet.
        """
        # X X O X - kein Gewinn
        self.brett.stein_einwerfen(0, 'X')
        self.brett.stein_einwerfen(1, 'X')
        self.brett.stein_einwerfen(2, 'O')
        self.brett.stein_einwerfen(3, 'X')
        
        self.assertFalse(self.brett.pruefe_gewinn('X'))

    def test_ist_voll_leeres_brett(self):
        """
        Test: Leeres Brett ist nicht voll.
        """
        self.assertFalse(self.brett.ist_voll())

    def test_ist_voll_teilweise_gefuellt(self):
        """
        Test: Teilweise gefülltes Brett ist nicht voll.
        """
        for spalte in range(3):
            self.brett.stein_einwerfen(spalte, 'X')
        
        self.assertFalse(self.brett.ist_voll())

    def test_ist_voll_volles_brett(self):
        """
        Test: Komplett gefülltes Brett wird als voll erkannt.
        """
        # Brett komplett füllen
        for spalte in range(7):
            for _ in range(6):
                self.brett.stein_einwerfen(spalte, 'X')
        
        self.assertTrue(self.brett.ist_voll())

    def test_zuruecksetzen(self):
        """
        Test: Spielbrett wird korrekt zurückgesetzt.
        """
        # Brett füllen
        for spalte in range(3):
            self.brett.stein_einwerfen(spalte, 'X')
        
        # Zurücksetzen
        self.brett.zuruecksetzen()
        
        # Prüfen ob leer
        for reihe in self.brett.brett:
            for feld in reihe:
                self.assertEqual(feld, ' ')

    def test_mehrere_gewinne_gleichzeitig(self):
        """
        Test: Mehrere Gewinnmöglichkeiten werden erkannt.
        """
        # Erstelle ein Brett mit horizontal und vertikal Gewinn für X
        # Horizontal in unterster Reihe
        for spalte in range(4):
            self.brett.stein_einwerfen(spalte, 'X')
        
        # Das sollte schon Gewinn sein
        self.assertTrue(self.brett.pruefe_gewinn('X'))
        
        # Zusätzlich vertikal in Spalte 0
        for _ in range(3):
            self.brett.stein_einwerfen(0, 'X')
        
        # Sollte immer noch Gewinn sein
        self.assertTrue(self.brett.pruefe_gewinn('X'))


if __name__ == '__main__':
    unittest.main()
