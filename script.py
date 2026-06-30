import json
import random
from collections import defaultdict

# Zeiterfassung
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATA_FILE = "flashcards.json"

# Open Json
try:
    with open("flashcards.json", "r") as json_file:
        words = json.load(json_file)
except (FileNotFoundError, json.JSONDecodeError):
    words = {}

def save_data():
    try:
        with open("flashcards.json", "w") as json_file:
            json.dump(words, json_file, indent=4)
    except FileNotFoundError:
        with open("flashcards.json", "w") as json_file:
            json.dump(words, json_file, indent=4)

# Längeres Wort = a setzen, kürzeres Wort = b, vergleicht jeden Buchstaben danach einzelnd (einsetzung im play)
def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)
    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Auswählen was hinzugefügt werden soll und dann hinzufügen 
def add_words():
    prompt = input("Type 'n' for new deck or 'o' for old one: ").strip().lower()
    if prompt == "n":
        deck = input("Enter a deck name: ").strip()
        if deck not in words:
            print(f'Deck "{deck}" is selected')
            words[deck] = {}
        else:
            print(f'Deck "{deck}" already exists, adding words to it...')

        filling = True
        while filling:
            action = input("Add 'word' or 'definition': ").strip().lower()
            if action == "word":
                word = input('Enter a word: ').strip()
                if word not in words[deck]:
                    definition = input('Enter definitions (comma separated): ').strip()
                    definitions = [d.strip() for d in definition.split(",")]
                    difficulty = int(input("Rate difficulty (1-10): ").strip())
                    words[deck][word] = {
                        "definition": definitions,
                        "difficulty": difficulty
                    }
                    save_data()
                else:
                    print("This word already exists!")
            elif action == "definition":
                if not words[deck]:
                    print("No words in this deck.")
                    continue
                for w, info in words[deck].items():
                    print(f"{w}: {info['definition']}")
                chosen_word = input("Which word?: ").strip()
                if chosen_word not in words[deck]:
                    print("Word not found")
                    continue
                new_def = input("New definition: ").strip()
                if isinstance(words[deck][chosen_word]["definition"], list):
                    words[deck][chosen_word]["definition"].append(new_def)
                else:
                    words[deck][chosen_word]["definition"] = [
                        words[deck][chosen_word]["definition"], new_def
                    ]
                save_data()
            more = input("Do you want to add more? (y/n): ").strip().lower()
            if more != "y":
                filling = False

    elif prompt == "o":
        if not words:
            print("No decks available. Please create a new deck first.")
            return
        for d in words:
            print(f'- {d}')
        deck = input("Enter an old deck: ").strip()
        if deck in words:
            print(f'Deck "{deck}" is selected')
            filling = True
            while filling:
                action = input("Add 'word' or 'definition': ").strip().lower()
                if action == "word":
                    word = input('Enter a word: ').strip()
                    if word not in words[deck]:
                        definition = input('Enter definitions (comma separated): ').strip()
                        definitions = [d.strip() for d in definition.split(",")]
                        difficulty = int(input("Rate difficulty (1-10): ").strip())
                        words[deck][word] = {
                            "definition": definitions,
                            "difficulty": difficulty
                        }
                        save_data()
                    else:
                        print("This word already exists!")
                elif action == "definition":
                    if not words[deck]:
                        print("No words in this deck.")
                        continue
                    for w, info in words[deck].items():
                        print(f"{w}: {info['definition']}")
                    chosen_word = input("Which word?: ").strip()
                    if chosen_word not in words[deck]:
                        print("Word not found")
                        continue
                    new_def = input("New definition: ").strip()
                    if isinstance(words[deck][chosen_word]["definition"], list):
                        words[deck][chosen_word]["definition"].append(new_def)
                    else:
                        words[deck][chosen_word]["definition"] = [
                            words[deck][chosen_word]["definition"], new_def
                        ]
                    save_data()
                more = input("Do you want to add more? (y/n): ").strip().lower()
                if more != "y":
                    filling = False

# Auswählen was gelöscht werden und dann löschen
def delete_words():
    choice = input('Delete "deck", "word" or "definition": ').strip().lower()
    if choice == "deck":
        if not words:
            print("No decks available to delete.")
            return
        for d in words:
            print(f'- {d}')
        deck = input("Enter a deck name to delete: ").strip()
        if deck in words:
            del words[deck]
            save_data()
            print(f'Deck "{deck}" has been deleted.')
        else:
            print(f'Deck "{deck}" does not exist.')

    elif choice == "word":
        if not words:
            print("No decks available.")
            return
        for d in words:
            print(f'- {d}')
        deck = input("Enter the deck name to delete words from or type 'exit': ").strip()
        if deck == "exit":
            return
        if deck not in words:
            print(f'Deck "{deck}" does not exist.')
            return
        while True:
            if not words[deck]:
                print(f'Deck "{deck}" is empty.')
                break
            for w in words[deck]:
                print(f'- {w}')
            word = input("Enter the word to delete or type 'exit': ").strip()
            if word == "exit":
                break
            if word in words[deck]:
                del words[deck][word]
                save_data()
                print(f'Word "{word}" deleted.')
            else:
                print(f'Word "{word}" does not exist.')

    elif choice == "definition":
        for d in words:
            print(f"- {d}")
    
        deck = input("Choose deck: ").strip()
    
        if deck not in words:
            return
    
        for word, info in words[deck].items():
            print(f"{word}: {info['definition']}")
    
        chosen_word = input("Choose word: ").strip()
    
        if chosen_word not in words[deck]:
            return
    
        definitions = words[deck][chosen_word]["definition"]
    
        if isinstance(definitions, str):
            definitions = [definitions]
    
        for d in definitions:
            print(f"- {d}")
    
        del_def = input("Which definition to delete?: ").strip()
        
        # Überprüfung nicht 0 definitions
        if del_def in definitions:
            definitions.remove(del_def)
            if len(definitions) == 0:
                print("At least one definition required.")
                definitions.append(del_def)
            words[deck][chosen_word]["definition"] = definitions
            save_data()

# Lernmodus
def play():
    # Nachschauen ob überhaupt Decks angelegt wurden.
    if not words:
        print("No decks available to play.")
        return
    
    # Auswählen Deck zum lernen
    for deck in words:
        print(f'- {deck}')
    deck = input("Which deck do you want to play: ").strip()
    if deck not in words:
        print(f'Deck "{deck}" does not exist.')
        return
    print(f'Deck "{deck}" is selected')
    due_words = list(words[deck].keys())
    if not due_words:
        print("No cards are due for review right now.")
        return

    # Wörter nach schwierigkeit sortiern (in Gruppen aufteilen, random shuffel, wieder zusammenführen)
    due_words.sort(key=lambda w: words[deck][w].get("difficulty", 5), reverse=True)
    grouped = {}
    for w in due_words:
        diff = words[deck][w].get("difficulty", 5)
        grouped.setdefault(diff, []).append(w)
    due_words = []
    for diff in sorted(grouped.keys(), reverse=True):
        group = grouped[diff]
        random.shuffle(group)
        due_words.extend(group)

    # Erfolgscounter Variable setzen, 
    counter = 0
    for i, word in enumerate(due_words):
        definitions = words[deck][word]["definition"]

        if isinstance(definitions, str):
            definitions = [definitions]

        definitions = [d.lower() for d in definitions]

        # Wörter eintragen + Überprüfung und einordnung Fehlerkategorie
        if i % 2 == 0:
            # FRONT → Wort anzeigen
            print(f'"{word}"')
            answer = input('Which is the correct definition?: ').strip().lower()

            if answer in definitions:
                result = "correct"
                counter += 1
            else:
                min_distance = min([levenshtein(answer, d) for d in definitions])

                if min_distance <= 2:
                    print("Spelling mistake")
                    result = "typo"
                else:
                    print(f"Wrong! Correct answers: {', '.join(definitions)}")
                    result = "wrong"
        else:
            # BACK → Definition anzeigen
            chosen_definition = random.choice(definitions)
            print(f'"{chosen_definition}"')
            answer = input('Which is the correct word?: ').strip().lower()
            if answer == word.lower():
                result = "correct"
                counter += 1
            else:
                distance = levenshtein(answer, word.lower())
                if distance <= 2:
                    print("Spelling mistake")
                    result = "typo"
                else:
                    print(f"Wrong! Correct answer: {word}")
                    result = "wrong"

        # Je nach Fehlerkategorie Schwierigkeit anpassen
        current_difficulty = int(words[deck][word].get("difficulty", 5))
        if result == "correct":
            new_difficulty = max(1, current_difficulty - 2)
        elif result == "typo":
            new_difficulty = min(10, current_difficulty + 1)
        else:  # wrong
            new_difficulty = min(10, current_difficulty + 2)
        words[deck][word]["difficulty"] = new_difficulty
        total = len(due_words)
        print(f"Done: {i+1}/{total} | Correct: {counter}")
        save_data()

    print(f'You have finished this deck')

# Anzeige aller Decks und Wörter in der Json
def show():
    if not words:
        print("No decks to show.")
        return
    for deck, cards in words.items():
        print(f"Deck: {deck}")
        for word, info in cards.items():
            definition = info["definition"]
            difficulty = info["difficulty"]
            print(f"  Word: {word}")
            if isinstance(definition, list):
                print(f"    Definition: {', '.join(definition)}")
            else:
                print(f"    Definition: {definition}")
            print(f"    Difficulty: {difficulty}")

# Funktion am Anfang und Ansteuerung verschieden Befehle
def start():
    while True:
        option = input(
            "Choose:\n 1.add \n 2.delete \n 3.play \n 4.show \n 5.quit\n"
        ).strip().lower()
        if option == "1" or option == "add":
            add_words()
        elif option == "2" or option == "delete":
            delete_words()
        elif option == "3" or option == "play":
            play()
        elif option == "4" or option == "show":
            show()
        elif option == "5" or option == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

start()
