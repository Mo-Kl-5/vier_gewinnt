# Theorie: Software Design

## Antwort zur Fragestellung "Legacy Code"

### 1. Welche Nachteile ergeben sich für mich als Entwickler?

Wenn ich auf ein solches Modul treffe (wenige Klassen, riesige Methoden, kaum Doku), entstehen für mich ganz praktische Probleme im Arbeitsalltag:

* **Enorme Einarbeitungszeit ("Cognitive Load"):** Es ist extrem schwer, eine Methode mit hunderten Zeilen im Kopf zu behalten. Ich muss ständig hoch- und runterscrollen, um zu verstehen, welche Variable wo geändert wurde. Ich verliere den Überblick, was der Code eigentlich fachlich tun soll.
* **Angst vor Änderungen ("Regression Bugs"):** In so langen Methoden hängen oft Dinge zusammen, die nichts miteinander zu tun haben sollten (z.B. Berechnung und Datenbankzugriff). Wenn ich an Zeile 50 etwas ändere, habe ich Angst, dass in Zeile 400 etwas kaputtgeht, ohne dass ich es merke.
* **Keine Testbarkeit:** Es ist fast unmöglich, für eine "Monolith"-Methode sinnvolle Unit-Tests zu schreiben, da sie viel zu viele Aufgaben gleichzeitig erledigt. Ich kann die Logik nicht isoliert prüfen.
* **Frustration:** Die Arbeit macht keinen Spaß, weil man mehr Zeit mit dem "Entziffern" des Codes verbringt als mit dem eigentlichen Lösen von Problemen.

### 2. Welche Software Design Prinzipien werden hier verletzt?

Der beschriebene Code verstößt gegen die wichtigsten Grundregeln der Softwareentwicklung, auf die wir auch in unserem Projekt geachtet haben:

* **Single Responsibility Principle (SRP):**
    Das ist wohl der stärkste Verstoß. Eine Methode oder Klasse sollte nur *eine* Aufgabe haben. Wenn eine Methode hunderte Zeilen lang ist, macht sie garantiert zu viel (z.B. Daten laden, validieren, berechnen UND ausgeben gleichzeitig).
    
* **Separation of Concerns (Trennung von Zuständigkeiten):**
    In dem Szenario sind Logik, Datenhaltung und vermutlich auch Benutzeroberfläche (UI) vermischt. Sauberes Design trennt diese Schichten (so wie wir `Spielbrett` von der `main`-Ausgabe getrennt haben).

* **KISS (Keep It Simple, Stupid):**
    Code sollte so einfach wie möglich sein. Riesige Textwüsten sind unnötig komplex und schwer verständlich.

* **DRY (Don't Repeat Yourself):**
    In sehr langen Methoden wird oft Code per Copy-Paste wiederholt, anstatt ihn in kleine Hilfsmethoden auszulagern. Das macht Wartung zur Hölle, weil man Änderungen an fünf Stellen gleichzeitig machen muss.