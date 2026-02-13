# Theorie: Design Patterns

Im Rahmen unserer Projektarbeit haben wir uns mit verschiedenen Design Patterns beschäftigt. Im Folgenden beschreiben wir zwei Muster, die für unser Projekt besonders relevant sind: das Strategy Pattern (welches wir implementiert haben) und das Observer Pattern (welches für eine Erweiterung sinnvoll wäre).

---

## 1. Strategy Pattern (Strategie-Muster)

### Das Problem
Bei der Entwicklung unseres Spiels standen wir vor der Herausforderung, dass es unterschiedliche Arten von Spielern gibt: einen menschlichen Spieler (der Eingaben über die Tastatur macht) und einen Computergegner (der seine Züge automatisch berechnet). 

Ein naiver Ansatz wäre gewesen, direkt in der Spielschleife mit `if`-Abfragen zu arbeiten (z.B. `if spieler_typ == 'computer': berechne_zug() else: frage_tastatur_ab()`). Das führt aber schnell zu Problemen:
* Der Code in der Spiel-Klasse wird unübersichtlich.
* Wenn wir später eine "Schwere KI" hinzufügen wollen, müssen wir wieder in den bestehenden Code eingreifen und noch mehr `if`-Zweige einbauen.
* Das verletzt das "Open-Closed-Principle": Man sollte Klassen erweitern können, ohne den bestehenden Code zu verändern.

### Die Lösung & Unsere Umsetzung
Das Strategy Pattern löst dieses Problem, indem es das unterschiedliche Verhalten (die "Strategie") in eigene Klassen auslagert, die aber alle gleich aussehen (ein gemeinsames Interface haben).

In unserem Projekt (`spieler.py`) haben wir das genau so umgesetzt:
1.  **Die abstrakte Strategie:** Wir haben eine Basisklasse `Spieler` erstellt. Sie definiert, dass jeder Spieler eine Methode `naechster_zug(brett)` haben muss.
2.  **Die konkreten Strategien:** * Die Klasse `MenschlicherSpieler` implementiert diese Methode, indem sie `input()` verwendet.
    * Die Klasse `ComputerSpieler` implementiert die gleiche Methode, wählt aber eine zufällige Spalte.
3.  **Der Kontext:** Unsere Klasse `Spiel` kennt nur die Basisklasse `Spieler`. Wenn sie `spieler.naechster_zug()` aufruft, ist es ihr völlig egal, ob dahinter ein Mensch oder eine Maschine steckt.

Der große Vorteil für uns war, dass wir den Computergenger programmieren konnten, ohne die eigentliche Spielmechanik in `spiel.py` anfassen zu müssen.

---

## 2. Observer Pattern (Beobachter-Muster)

### Das Problem
Ein häufiges Problem in Softwareprojekten ist die Kommunikation zwischen Daten (dem "Modell") und der Anzeige (der "View"). Nehmen wir an, wir würden unserem "Vier Gewinnt" später eine grafische Oberfläche spendieren. 

Wenn sich auf dem Spielbrett ein Stein ändert, muss die Grafik aktualisiert werden. Wenn man das Spielbrett aber direkt die Grafik-Funktionen aufrufen lässt, sind beide Teile fest miteinander "verdrahtet". Man könnte das Spielbrett dann nicht mehr ohne die Grafik nutzen (z.B. für unsere jetzige Konsolen-Version oder für automatisierte Tests). Man will also, dass das Spielbrett Bescheid geben kann "Hallo, ich habe mich geändert!", ohne wissen zu müssen, wer genau zuhört.

### Die Lösung
Das Observer Pattern definiert eine Art "Zeitungs-Abo":
* Es gibt ein **Subjekt** (bei uns wäre das das Spielbrett), bei dem man sich "anmelden" kann.
* Es gibt viele **Beobachter** (Observer), die sich anmelden.
* Wenn sich das Subjekt ändert, ruft es einfach bei allen angemeldeten Beobachtern eine `update()`-Methode auf.

### Bezug zu unserem Projekt
Aktuell nutzen wir dieses Pattern noch nicht, da wir in der Konsole einfach nach jedem Zug das komplette Brett neu zeichnen (`print`). 

Für eine Weiterentwicklung ("Version 2.0") wäre das aber zentral:
Unser `Spielbrett` würde eine Liste von Beobachtern führen. Wenn ein Stein eingeworfen wird, geht es diese Liste durch und benachrichtigt alle. Das Tolle daran ist die Flexibilität: Wir könnten dann gleichzeitig eine grafische Oberfläche, eine Konsolen-Ausgabe und vielleicht eine Log-Datei als Beobachter anhängen. Das Spielbrett müsste seinen Code dafür nicht ändern – es feuert einfach nur das "Update"-Signal ab.