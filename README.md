
# 🔴 Vier Gewinnt - Python Projekt 🟡

Dies ist eine Implementierung des Spieleklassikers "Vier Gewinnt" in Python. Das Projekt wurde mit einem Fokus auf sauberes Software-Design (OOP) und Erweiterbarkeit entwickelt. Es bietet eine Konsolenoberfläche, in der zwei Spieler gegeneinander oder ein Spieler gegen eine KI antreten können.

## 🚀 Features

-   **Dynamisches Spielbrett**: Ein 7x6 Gitter, das den Spielstand visuell in der Konsole darstellt.
-   **Spieler-Management**: Unterstützung für menschliche Spieler und Computer-Gegner.
-   **Gewinnerkennung**: Automatische Prüfung auf horizontale, vertikale und diagonale Gewinnreihen.
-   **Unentschieden**: Erkennung, wenn das Brett voll ist (Draw).

## 🛠️ Tech Stack

* **Sprache**: Python 3.x
* **Abhängigkeiten**: Keine externen Bibliotheken notwendig (nur Standard-Bibliotheken wie `random`, `sys`, `os` ).

## 📂 Projektstruktur

Das Projekt folgt einer flachen, modularen Struktur für maximale Kompatibilität:

```text
.
├── main.py        # Einstiegspunkt (Startet das Spiel)
├── spiel.py       # Steuerung des Spielablaufs (Game Loop)
├── spieler.py     # Klassen für Mensch und Computer
├── spielbrett.py  # Logik des Spielfelds (Gitter & Gewinnprüfung)
└── README.md      # Dokumentation

📦 Installation & Start
Um das Spiel zu starten, benötigst du nur eine installierte Python-Version.

Repository klonen (oder Ordner herunterladen):

Bash
git clone [https://github.com/DEIN-USER/vier_gewinnt.git](https://github.com/DEIN-USER/vier_gewinnt.git)
cd vier_gewinnt
Spiel starten:
Führe die main.py aus.

Bash
python3 main.py
(Falls du Windows nutzt, reicht oft python main.py)

💻 Bedienung
Nach dem Start wählst du im Menü den Spielmodus:

1: Zwei menschliche Spieler (abwechselnd am selben PC).

2: Mensch gegen Computer (Leicht).

Gib im Spiel einfach die Nummer der Spalte (0-6) ein, in die du deinen Stein werfen möchtest.

Mit q kannst du das Spiel jederzeit beenden.

🤝 Mitwirkende
Dieses Projekt wurde im Rahmen der Projektarbeit für SEM-AI WS 2025. erstellt.

-Moritz 

-Lovepreet 


Danke fürs Spielen! 🎮

