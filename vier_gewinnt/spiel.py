"""Modul für die Spielsteuerung."""

from vier_gewinnt.spielbrett import Spielbrett
from vier_gewinnt.spieler import MenschlicherSpieler, ComputerSpieler


class Spiel:
    """
    Steuert den Ablauf eines Vier Gewinnt Spiels.

    Attributes
    ----------
    brett : Spielbrett
        Das Spielbrett
    spieler1 : Spieler
        Der erste Spieler
    spieler2 : Spieler
        Der zweite Spieler
    aktueller_spieler : Spieler
        Der Spieler der gerade am Zug ist
    """

    def __init__(self):
        """
        Initialisiert ein neues Spiel.
        """
        self.brett = Spielbrett()
        self.spieler1 = None
        self.spieler2 = None
        self.aktueller_spieler = None

    def spielmodus_waehlen(self):
        """
        Lässt den Benutzer den Spielmodus wählen.

        Der Benutzer kann zwischen zwei menschlichen Spielern oder
        einem Spiel gegen den Computer wählen.
        """
        print("\n=== VIER GEWINNT ===\n")
        print("Wähle den Spielmodus:")
        print("1 - Zwei Spieler")
        print("2 - Gegen Computer")
        
        while True:
            wahl = input("\nDeine Wahl (1 oder 2): ")
            
            if wahl == '1':
                name1 = input("Name Spieler 1: ") or "Spieler 1"
                name2 = input("Name Spieler 2: ") or "Spieler 2"
                self.spieler1 = MenschlicherSpieler(name1, 'X')
                self.spieler2 = MenschlicherSpieler(name2, 'O')
                break
            elif wahl == '2':
                name = input("Dein Name: ") or "Spieler"
                self.spieler1 = MenschlicherSpieler(name, 'X')
                self.spieler2 = ComputerSpieler("Computer", 'O')
                break
            else:
                print("Ungültige Eingabe! Bitte wähle 1 oder 2.")
        
        self.aktueller_spieler = self.spieler1

    def spieler_wechseln(self):
        """
        Wechselt zum nächsten Spieler.
        """
        if self.aktueller_spieler == self.spieler1:
            self.aktueller_spieler = self.spieler2
        else:
            self.aktueller_spieler = self.spieler1

    def spielen(self):
        """
        Startet das Spiel und führt die Spielschleife aus.

        Die Spielschleife läuft bis ein Spieler gewonnen hat,
        das Brett voll ist oder ein Spieler das Spiel beendet.
        """
        self.spielmodus_waehlen()
        
        print("\n=== SPIEL BEGINNT ===")
        self.brett.anzeigen()
        
        while True:
            # Nächster Zug
            spalte = self.aktueller_spieler.naechster_zug(self.brett)
            
            # Spiel beenden
            if spalte == -1:
                print("\nSpiel wurde beendet.")
                break
            
            # Stein einwerfen
            reihe = self.brett.stein_einwerfen(spalte, self.aktueller_spieler.symbol)
            
            # Brett anzeigen
            self.brett.anzeigen()
            
            # Gewinn prüfen
            if self.brett.pruefe_gewinn(self.aktueller_spieler.symbol):
                print(f"\n🎉 {self.aktueller_spieler.name} hat gewonnen! 🎉")
                break
            
            # Unentschieden prüfen
            if self.brett.ist_voll():
                print("\n⚖️  Unentschieden! Das Brett ist voll. ⚖️")
                break
            
            # Spieler wechseln
            self.spieler_wechseln()

    def neues_spiel(self):
        """
        Startet ein neues Spiel mit dem gleichen Spielmodus.
        """
        self.brett.zuruecksetzen()
        self.aktueller_spieler = self.spieler1
        self.spielen()
