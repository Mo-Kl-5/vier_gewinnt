Projektdokumentation: Planung & Umsetzung „Vier Gewinnt“
1. Einleitung & Zielsetzung
Ziel dieses Projekts war die Entwicklung einer stabilen, erweiterbaren Version des Spieleklassikers „Vier Gewinnt“ in Python. Von Anfang an lag unser Fokus nicht nur auf der reinen Funktionalität, sondern auf einem sauberen Software-Design, das den Prinzipien der Objektorientierung folgt.

2. Architektur & Designentscheidungen
Das Klassendesign (Konzept)
Wir haben uns für eine klare Trennung der Zuständigkeiten entschieden, um den Code wartbar zu halten.

Code-Snippet
classDiagram
    direction TB
    class Spielbrett {
        +list brett
        +stein_einwerfen(spalte, symbol)
        +pruefe_gewinn(symbol)
    }
    class Spieler {
        <<abstract>>
        +str name
        +naechster_zug(brett)*
    }
    class Spiel {
        +Spielbrett brett
        +spielen()
    }
    Spieler <|-- MenschlicherSpieler
    Spieler <|-- ComputerSpieler
    Spiel "1" *-- "1" Spielbrett
    Spiel "1" *-- "2" Spieler
Warum dieses Muster?
Strategy Pattern für die Spieler: Das war eine bewusste Entscheidung. Durch die Abstraktion der Klasse Spieler ist es unserem System egal, ob ein Mensch vor dem Bildschirm sitzt oder ein Algorithmus die Züge berechnet. Das macht das System extrem flexibel für spätere Upgrades (z. B. eine „schlaue“ KI).

Kapselung der Logik: Das Spielbrett weiß nichts über die Spieler. Es validiert lediglich Züge und erkennt Gewinnmuster. Die Spiel-Klasse fungiert als „Regisseur“, der alles zusammenhält.

3. Der Entwicklungsprozess: Theorie vs. Praxis
Kein Projekt läuft exakt wie geplant. Hier sind die wichtigsten Anpassungen, die wir während der Programmierung vorgenommen haben:

Vom Flag zur Vererbung: Ursprünglich wollten wir nur eine Klasse Spieler mit einem Attribut ist_computer. Wir merkten aber schnell, dass das zu unschönen if-else-Strukturen führt. Der Wechsel auf echte Vererbung hat den Code massiv bereinigt.

Zentralisierte Gewinnprüfung: Wir überlegten, eine eigene Klasse für die Gewinnprüfung zu bauen. Letztlich haben wir diese Logik aber direkt in das Spielbrett integriert, da die Prüfung untrennbar mit dem Zustand des 2D-Arrays verbunden ist.

4. Persönliche Note: Probleme & Lösungen (Lessons Learned)
Ein wichtiger Teil unseres Projekts war die Zusammenarbeit über Git und GitHub. Hier sind wir auf reale Herausforderungen gestoßen, die uns als Team wachsen ließen:

Die „Geister-Dateien“ (Problem mit .DS_Store)
Als Mac-Nutzer hatten wir anfangs das Problem, dass versteckte Systemdateien (.DS_Store) ständig Merge-Konflikte verursachten.

Lösung: Wir haben eine professionelle .gitignore-Datei erstellt, um diese Dateien konsequent aus dem Repository auszuschließen. Das hat den Workflow sofort beruhigt.

Der „Force-Push“-Zwischenfall
Während der finalen Phase gab es einen kritischen Moment: Durch einen erzwungenen Push (--force) wurden versehentlich die Unit-Tests eines Teammitglieds auf GitHub überschrieben.

Lösung & Lerneffekt: Wir haben gelernt, dass Kommunikation wichtiger ist als der Befehl im Terminal. Wir konnten die Tests durch lokale Backups wiederherstellen. Dieser Vorfall hat uns verdeutlicht, warum Git-Workflows (Branches und Pull Requests) in der professionellen Softwareentwicklung unverzichtbar sind.

5. Fazit & Ausblick
Das Projekt steht auf einem soliden Fundament. Dank der sauberen Trennung der Klassen könnten wir in einer nächsten Version problemlos:

Eine grafische Oberfläche (GUI) aufsetzen, ohne die Spiellogik ändern zu müssen.

Die KI verbessern (z. B. mit dem Minimax-Algorithmus), indem wir einfach eine neue Spieler-Unterklasse hinzufügen.