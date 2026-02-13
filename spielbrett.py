"""Modul für das Vier Gewinnt Spielbrett."""


class Spielbrett:
    """
    Repräsentiert das Spielbrett für Vier Gewinnt.

    Das Spielbrett hat 6 Reihen und 7 Spalten. Spieler lassen ihre Steine
    in eine Spalte fallen, der Stein landet in der untersten freien Position.

    Attributes
    ----------
    reihen : int
        Anzahl der Reihen (Standard: 6)
    spalten : int
        Anzahl der Spalten (Standard: 7)
    brett : list[list[str]]
        2D-Liste die den Zustand des Spielbretts repräsentiert.
        Leere Felder sind ' ', Spieler 1 ist 'X', Spieler 2 ist 'O'.
    """

    def __init__(self, reihen=6, spalten=7):
        """
        Initialisiert ein leeres Spielbrett.

        Parameters
        ----------
        reihen : int, optional
            Anzahl der Reihen (Standard: 6)
        spalten : int, optional
            Anzahl der Spalten (Standard: 7)
        """
        self.reihen = reihen
        self.spalten = spalten
        self.brett = [[' ' for _ in range(spalten)] for _ in range(reihen)]

    def ist_spalte_gueltig(self, spalte):
        """
        Überprüft ob ein Zug in eine Spalte gültig ist.

        Parameters
        ----------
        spalte : int
            Die Spaltennummer (0-6)

        Returns
        -------
        bool
            True wenn die Spalte gültig und nicht voll ist, sonst False
        """
        if spalte < 0 or spalte >= self.spalten:
            return False
        return self.brett[0][spalte] == ' '

    def stein_einwerfen(self, spalte, spieler):
        """
        Wirft einen Stein in die angegebene Spalte.

        Der Stein fällt bis zur untersten freien Position.

        Parameters
        ----------
        spalte : int
            Die Spaltennummer (0-6)
        spieler : str
            Das Spielersymbol ('X' oder 'O')

        Returns
        -------
        int
            Die Reihennummer wo der Stein gelandet ist, oder -1 bei Fehler
        """
        if not self.ist_spalte_gueltig(spalte):
            return -1

        # Von unten nach oben suchen
        for reihe in range(self.reihen - 1, -1, -1):
            if self.brett[reihe][spalte] == ' ':
                self.brett[reihe][spalte] = spieler
                return reihe

        return -1

    def pruefe_gewinn(self, spieler):
        """
        Überprüft ob der angegebene Spieler gewonnen hat.

        Es wird auf horizontale, vertikale und diagonale Viererreihen geprüft.

        Parameters
        ----------
        spieler : str
            Das Spielersymbol ('X' oder 'O')

        Returns
        -------
        bool
            True wenn der Spieler gewonnen hat, sonst False
        """
        # Horizontal prüfen
        for reihe in range(self.reihen):
            for spalte in range(self.spalten - 3):
                if all(self.brett[reihe][spalte + i] == spieler for i in range(4)):
                    return True

        # Vertikal prüfen
        for reihe in range(self.reihen - 3):
            for spalte in range(self.spalten):
                if all(self.brett[reihe + i][spalte] == spieler for i in range(4)):
                    return True

        # Diagonal (links-oben nach rechts-unten) prüfen
        for reihe in range(self.reihen - 3):
            for spalte in range(self.spalten - 3):
                if all(self.brett[reihe + i][spalte + i] == spieler for i in range(4)):
                    return True

        # Diagonal (rechts-oben nach links-unten) prüfen
        for reihe in range(self.reihen - 3):
            for spalte in range(3, self.spalten):
                if all(self.brett[reihe + i][spalte - i] == spieler for i in range(4)):
                    return True

        return False

    def ist_voll(self):
        """
        Überprüft ob das Spielbrett voll ist.

        Returns
        -------
        bool
            True wenn das Brett voll ist (Unentschieden), sonst False
        """
        return all(self.brett[0][spalte] != ' ' for spalte in range(self.spalten))

    def anzeigen(self):
        """
        Gibt das Spielbrett auf der Konsole aus.

        Das Brett wird mit Spaltennummern und Trennlinien formatiert.
        """
        print("\n  " + " ".join(str(i) for i in range(self.spalten)))
        print("  " + "-" * (self.spalten * 2 - 1))
        for reihe in self.brett:
            print("| " + " ".join(reihe) + " |")
        print("  " + "-" * (self.spalten * 2 - 1))

    def zuruecksetzen(self):
        """
        Setzt das Spielbrett zurück (leert alle Felder).
        """
        self.brett = [[' ' for _ in range(self.spalten)] for _ in range(self.reihen)]
