# Learning Vocabulary Tool

### Ziel

Das **Learning Vocabulary Tool** ist ein kleines Python-Projekt zum Lernen von Vokabeln und Fachbegriffen.  
Nutzer können eigene Karteikarten-Decks erstellen, Wörter mit mehreren Definitionen speichern und diese im Lernmodus abfragen lassen.

---

## Dokumentation

### Was macht das Tool?

Das Tool verwaltet digitale Karteikarten in einer JSON-Datei.  
Im Lernmodus werden Wörter oder Definitionen zufällig abgefragt und die Schwierigkeit der Karteikarten wird abhängig von der Antwort angepasst.

---

### Beispiel: Input → Output

#### Beispiel-Eingabe

```text
Deck: Technisches Englisch
Wort: Assembly line
Definition: Fließband
```

#### Beispiel im Lernmodus

```text
Was bedeutet: Assembly line?
Antwort: Fließband
```

#### Beispiel-Ausgabe

```text
Correct!

Neue Schwierigkeit: 3
Fortschritt:
Bearbeitet: 15 / 40
Richtig: 13
```

---

## Startanleitung

### 1. Python installieren

Python muss auf dem Computer installiert sein.

Download:  
https://www.python.org/


### 2. Repository herunterladen

```bash
git clone https://github.com/MoritzSchallenberg/Learning-vocabulary-tool.git
```

### 3. In den Projektordner wechseln

```bash
cd Learning-vocabulary-tool
```


### 4. Programm starten

```bash
python script.py
```

---

## Bedienung

Nach dem Start erscheinen mehrere Auswahlmöglichkeiten:

```text
1. add
2. delete
3. play
4. show
5. quit
```

### add

Mit `add` können neue Decks, Wörter und Definitionen hinzugefügt werden.

### delete

Mit `delete` können Decks, Wörter oder einzelne Definitionen gelöscht werden.

### play

Mit `play` startet der Lernmodus.  

### show

Mit `show` werden die gespeicherten Decks, Wörter, Definitionen und Schwierigkeitswerte angezeigt.

### quit

Mit `quit` wird das Programm beendet.

---

### Projektstruktur

```text
Learning-vocabulary-tool
│
├── script.py
├── flashcards.json
├── README.md
```

### script.py

Enthält die Hauptlogik des Programms:

- Menüführung
- Hinzufügen von Decks und Wörtern
- Löschen von Einträgen
- Lernmodus
- Bewertung der Antworten

### flashcards.json

Speichert die Lerninhalte:

- Decks
- Wörter
- Definitionen
- Schwierigkeitsgrad

---

## Bewertung der Antworten

Im Lernmodus wird die Antwort automatisch bewertet.

| Antworttyp | Auswirkung |
|---|---|
| Richtig | Schwierigkeit wird verringert |
| Kleiner Schreibfehler | Schwierigkeit wird leicht erhöht |
| Falsch | Schwierigkeit wird stärker erhöht |

Dadurch werden schwierige Wörter häufiger wiederholt.

---

## Mögliche Verbesserungen

Für zukünftige Versionen sind folgende Erweiterungen sinnvoll:

- Ähnliche Definitionen direkt im `play`-Modus hinzufügen.
- Verbesserte Erkennung ähnlicher Wörter.

---