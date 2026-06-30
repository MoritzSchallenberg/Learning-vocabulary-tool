📚 Flashcard Learning Tool (Python)

🔍 Beschreibung
Dieses Python-basierte Karteikarten-Tool ermöglicht es Studierenden, effizient für verschiedene Fächer zu lernen. Es bietet eine einfache Alternative zu kostenpflichtigen Programmen wie Anki und nutzt ein eigenes Schwierigkeitssystem, um Lerninhalte individuell zu priorisieren.

🚀 Startanleitung
1. Python installieren (falls noch nicht vorhanden)
2. Projekt herunterladen oder klonen
3. Im Terminal oder Editor ausführen:
   python script.py
4. Den Anweisungen im Programm folgen

⚙️ Funktionsweise (Input → Output)
Input:
Benutzer fügt Wörter + Definitionen hinzu
Benutzer bewertet Schwierigkeit (1–10)
Benutzer beantwortet Fragen im Lernmodus

Output:
Wörter werden gespeichert (JSON-Datenbank)
Schwierige Wörter werden häufiger angezeigt
Lernfortschritt wird sichtbar gemacht (Trefferquote)

🧠 Features
➕ 1. Karten hinzufügen (add)
      - Neue oder bestehende Decks auswählen
      - Wörter und Definitionen eingeben
      - Schwierigkeit (1–10) festlegen
❌ 2. Karten löschen (delete)
      - Ganze Decks oder einzelne Wörter löschen
🎮 3. Lernmodus (play)
      - Deck auswählen
      - Wörter werden abgefragt (abwechselnd Wort ↔ Definition)
      - Schwierigkeit wird nach jeder Karte neu bewertet
      - Karten werden nach Schwierigkeit priorisiert:
      - Schwere Karten zuerst
      - Innerhalb der Schwierigkeit zufällige Reihenfolge
📋 4. Übersicht (show)
      - Anzeige aller Decks, Wörter und:
      - Definition
      - Nächster Lernzeitpunkt
      - Schwierigkeit
🚪 5. Beenden (quit)
      - Programm sauber beenden

💾 Datenstruktur
Die Daten werden in einer JSON-Datei gespeichert:
{
  "Deckname": {
    "Wort": {
      "definition": "Beschreibung",
      "next_review": "Zeitpunkt",
      "difficulty": 7
    }
  }
}

💡 Besonderheiten
Eigenes Priorisierungssystem basierend auf Schwierigkeit
Kombination aus Sortierung + Zufall für optimales Lernen
Einfach erweiterbar (z. B. Spaced Repetition möglich)
Keine externen Libraries notwendig

📈 Beispiel
Input:
Word: Voltage  
Definition: elektrische Spannung  
Difficulty: 8

Output im Lernmodus:
"Voltage"
→ User antwortet falsch
→ Schwierigkeit bleibt hoch
→ Wort erscheint häufiger

🎯 Ziel des Projekts
Ziel ist es, ein einfaches, verständliches und funktionales Lernsystem zu entwickeln, das Studierenden hilft, Inhalte effizient zu wiederholen und langfristig zu behalten.
