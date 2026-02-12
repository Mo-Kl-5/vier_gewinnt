"""Hauptprogramm zum Starten von Vier Gewinnt."""

from vier_gewinnt.spiel import Spiel


def main():
    """
    Hauptfunktion die das Spiel startet.

    Erstellt ein neues Spiel und startet die Spielschleife.
    Nach Spielende wird gefragt ob ein neues Spiel gestartet werden soll.
    """
    while True:
        spiel = Spiel()
        spiel.spielen()
        
        # Neues Spiel?
        nochmal = input("\nNochmal spielen? (j/n): ")
        if nochmal.lower() != 'j':
            print("\nDanke fürs Spielen! Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()
