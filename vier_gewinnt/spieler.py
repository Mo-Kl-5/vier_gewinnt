
import random


class Spieler:
    """
    Basisklasse für einen Spieler.

    Attributes
    ----------
    name : str
        Name des Spielers
    symbol : str
        Spielersymbol ('X' oder 'O')
    """

    def __init__(self, name, symbol):
        """
        Initialisiert einen Spieler.

        Parameters
        ----------
        name : str
            Name des Spielers
        symbol : str
            Spielersymbol ('X' oder 'O')
        """
        self.name = name
        self.symbol = symbol

    def naechster_zug(self, brett):
        """
        Ermittelt den nächsten Zug des Spielers.

        Diese Methode muss von Unterklassen implementiert werden.

        Parameters
        ----------
        brett : Spielbrett
            Das aktuelle Spielbrett

        Returns
        -------
        int
            Die gewählte Spaltennummer

        Raises
        ------
        NotImplementedError
            Wenn die Methode nicht überschrieben wurde
        """
        raise NotImplementedError("Diese Methode muss überschrieben werden")


class MenschlicherSpieler(Spieler):
    """
    Repräsentiert einen menschlichen Spieler.

    Der Spieler gibt seine Züge über die Konsole ein.
    """

    def naechster_zug(self, brett):
        """
        Fragt den menschlichen Spieler nach seinem nächsten Zug.

        Parameters
        ----------
        brett : Spielbrett
            Das aktuelle Spielbrett

        Returns
        -------
        int
            Die gewählte Spaltennummer, oder -1 zum Beenden
        """
        while True:
            eingabe = input(f"\n{self.name} ({self.symbol}), wähle eine Spalte (0-{brett.spalten-1}) oder 'q' zum Beenden: ")
            
            if eingabe.lower() == 'q':
                return -1
            
            try:
                spalte = int(eingabe)
                if brett.ist_spalte_gueltig(spalte):
                    return spalte
                else:
                    print("Ungültige Spalte! Bitte wähle eine Spalte zwischen 0 und {} die noch nicht voll ist.".format(brett.spalten-1))
            except ValueError:
                print("Ungültige Eingabe! Bitte gib eine Zahl ein oder 'q' zum Beenden.")


class ComputerSpieler(Spieler):
    """
    Repräsentiert einen Computer-Gegner.

    Der Computer wählt zufällige gültige Züge.
    """

    def naechster_zug(self, brett):
        """
        Wählt einen zufälligen gültigen Zug.

        Parameters
        ----------
<<<<<<< HEAD
        brett : Spielbrett
=======
        brett : Spielbrett
            Das aktuelle Spielbrett
>>>>>>> f4084ba37824d540d0ab76fd2caa935378ca67f3

        Returns
        -------
        int
            Eine zufällige gültige Spaltennummer
        """
        gueltige_spalten = [s for s in range(brett.spalten) if brett.ist_spalte_gueltig(s)]
        
        if not gueltige_spalten:
            return -1
        
        spalte = random.choice(gueltige_spalten)
        print(f"\n{self.name} ({self.symbol}) wählt Spalte {spalte}")
        return spalte
