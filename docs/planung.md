# Planung der Umsetzung

## Übersicht

Dieses Dokument beschreibt die initiale Planung des Vier Gewinnt Projekts, einschließlich der Klassenstruktur, Methoden und Interaktionen.

## Klassendiagramm (Konzept)

```
┌─────────────────────┐
│    Spielbrett       │
├─────────────────────┤
│ - reihen: int       │
│ - spalten: int      │
│ - brett: list[][]   │
├─────────────────────┤
│ + ist_spalte_gueltig() │
│ + stein_einwerfen()    │
│ + pruefe_gewinn()      │
│ + ist_voll()           │
│ + anzeigen()           │
│ + zuruecksetzen()      │
└─────────────────────┘
         △
         │
         │ verwendet
         │
┌─────────────────────┐         ┌─────────────────────┐
│     Spiel           │────────▷│     Spieler         │
├─────────────────────┤         ├─────────────────────┤
│ - brett: Spielbrett │         │ - name: str         │
│ - spieler1: Spieler │         │ - symbol: str       │
│ - spieler2: Spieler │         └─────────────────────┘
│ - aktueller_spieler │                   △
├─────────────────────┤                   │
│ + spielmodus_waehlen()│                 │
│ + spieler_wechseln()  │    ┌────────────┴──────────┐
│ + spielen()           │    │                       │
│ + neues_spiel()       │    │                       │
└─────────────────────┘    │                       │
                      ┌────────────┐        ┌──────────────┐
                      │ Menschlicher│        │  Computer-   │
                      │   Spieler   │        │   Spieler    │
                      ├────────────┤        ├──────────────┤
                      │+ naechster_zug()│   │+ naechster_zug()│
                      └────────────┘        └──────────────┘
```

## Geplante Klassen

### 1. Klasse `Spielbrett`

**Verantwortung**: Verwaltung des Spielfeldes und Spiellogik

**Attribute**:
- `reihen`: Anzahl der Reihen (6)
- `spalten`: Anzahl der Spalten (7)
- `brett`: 2D-Liste für Spielfeld-Zustand

**Methoden**:
- `ist_spalte_gueltig(spalte)`: Prüft ob Zug gültig ist
- `stein_einwerfen(spalte, spieler)`: Führt einen Zug aus
- `pruefe_gewinn(spieler)`: Überprüft Gewinnbedingung
- `ist_voll()`: Prüft ob Brett voll ist (Unentschieden)
- `anzeigen()`: Gibt Brett auf Konsole aus
- `zuruecksetzen()`: Setzt Brett zurück

**Begründung**: Das Spielbrett ist zentral für die Spiellogik. Eine eigene Klasse ermöglicht gute Testbarkeit und Wiederverwendbarkeit.

### 2. Klasse `Spieler` (abstrakte Basisklasse)

**Verantwortung**: Gemeinsame Schnittstelle für alle Spielertypen

**Attribute**:
- `name`: Name des Spielers
- `symbol`: Spielersymbol ('X' oder 'O')

**Methoden**:
- `naechster_zug(brett)`: Gibt nächsten Zug zurück (muss überschrieben werden)

**Begründung**: Abstraktion ermöglicht verschiedene Spielertypen (Mensch, Computer) mit gleicher Schnittstelle.

### 3. Klasse `MenschlicherSpieler` (erbt von `Spieler`)

**Verantwortung**: Eingabeverarbeitung für menschliche Spieler

**Methoden**:
- `naechster_zug(brett)`: Fordert Benutzereingabe an und validiert diese

**Begründung**: Trennung von Eingabelogik und Spiellogik.

### 4. Klasse `ComputerSpieler` (erbt von `Spieler`)

**Verantwortung**: KI-Logik für Computer-Gegner

**Methoden**:
- `naechster_zug(brett)`: Wählt zufälligen gültigen Zug

**Begründung**: Einfache KI-Implementierung, später erweiterbar für intelligentere Strategien.

### 5. Klasse `Spiel`

**Verantwortung**: Spielablauf koordinieren

**Attribute**:
- `brett`: Das Spielbrett
- `spieler1`, `spieler2`: Die beiden Spieler
- `aktueller_spieler`: Wer gerade am Zug ist

**Methoden**:
- `spielmodus_waehlen()`: Benutzer wählt Spielmodus
- `spieler_wechseln()`: Wechselt zwischen Spielern
- `spielen()`: Hauptspielschleife
- `neues_spiel()`: Startet neues Spiel

**Begründung**: Zentrale Koordination des Spielablaufs, getrennt von der Spiellogik.

## Interaktionen zwischen Klassen

1. **Spiel → Spielbrett**: 
   - `Spiel` erstellt ein `Spielbrett` Objekt
   - Ruft Methoden wie `stein_einwerfen()`, `pruefe_gewinn()` auf

2. **Spiel → Spieler**:
   - `Spiel` verwaltet zwei `Spieler` Objekte
   - Ruft `naechster_zug()` für aktuellen Spieler auf

3. **Spieler → Spielbrett**:
   - Spieler erhalten Brett als Parameter bei `naechster_zug()`
   - Können Brett-Zustand abfragen (z.B. für KI-Entscheidungen)

## Spielablauf (Sequenz)

1. `Spiel` Objekt wird erstellt
2. Benutzer wählt Spielmodus (`spielmodus_waehlen()`)
3. `Spieler` Objekte werden erstellt (Mensch oder Computer)
4. Spielschleife in `spielen()`:
   - Brett anzeigen
   - Aktueller Spieler macht Zug (`naechster_zug()`)
   - Zug ausführen (`stein_einwerfen()`)
   - Gewinn prüfen (`pruefe_gewinn()`)
   - Falls gewonnen: Sieger ausgeben, Ende
   - Falls unentschieden (`ist_voll()`): Ende
   - Spieler wechseln
5. Neues Spiel Option

## Designentscheidungen

### Warum Vererbung für Spieler?
- Gemeinsame Schnittstelle ermöglicht austauschbare Spielertypen
- Mensch vs. Computer unterscheiden sich nur in `naechster_zug()`
- Erweiterbar für weitere KI-Varianten

### Warum separate Spielbrett-Klasse?
- Klare Trennung: Spiellogik vs. Spielablauf
- Bessere Testbarkeit (Brett-Logik isoliert testbar)
- Wiederverwendbar in anderen Projekten/Varianten

### Warum Spiel-Klasse?
- Koordiniert den Ablauf
- Hält Spielzustand (aktueller Spieler, etc.)
- Ermöglicht Erweiterungen (z.B. Spielstand speichern)

## Änderungen während der Umsetzung

### Ursprüngliche Planung
- Initialplanung sah vor, dass `Spieler` eine konkrete Klasse ist mit einem `ist_computer` Flag
- Gewinnprüfung sollte in separater Klasse `Gewinnpruefer` sein

### Tatsächliche Umsetzung
- **Änderung 1**: Vererbungshierarchie für Spieler
  - **Grund**: Bessere Erweiterbarkeit, cleaner Code, folgt OOP-Prinzipien
  - **Auswirkung**: Mehr Klassen, aber bessere Struktur

- **Änderung 2**: Gewinnprüfung direkt in `Spielbrett`
  - **Grund**: Gewinnprüfung ist eng mit Brett-Zustand verbunden
  - **Auswirkung**: Weniger Klassen, einfacherer Code, ausreichend für Projektumfang

- **Änderung 3**: Trennung von horizontaler, vertikaler, diagonaler Prüfung in einer Methode
  - **Grund**: Alle Prüfungen folgen gleichem Muster, eine Methode mit 4 Prüfungen ist übersichtlich
  - **Auswirkung**: Kompakterer Code, trotzdem gut lesbar

## Testbarkeit

Die gewählte Struktur ermöglicht gutes Testen:
- `Spielbrett` Logik ist vollständig isoliert testbar
- Keine UI-Abhängigkeiten in Kernlogik
- `naechster_zug()` kann mit Mock-Objekten getestet werden
- Gewinnbedingungen haben klare Ein-/Ausgaben

## Erweiterungsmöglichkeiten

Die Architektur erlaubt folgende Erweiterungen ohne große Änderungen:
- Verschiedene Brett-Größen (Parameter im Konstruktor)
- Intelligentere KI (neue Klasse, erbt von `Spieler`)
- Grafische Oberfläche (neue View-Klasse, nutzt bestehendes `Spielbrett`)
- Online-Multiplayer (neue Netzwerk-Spieler-Klasse)
- Spielstand speichern/laden (Methoden in `Spiel` Klasse)
