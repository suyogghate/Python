import random

words = [
    {"german": "der", "english": "the (masculine)"},
    {"german": "die", "english": "the (feminine)"},
    {"german": "das", "english": "the (neuter)"},
    {"german": "und", "english": "and"},
    {"german": "sein", "english": "to be"},
    {"german": "in", "english": "in"},
    {"german": "ein", "english": "a, an"},
    {"german": "zu", "english": "to, at"},
    {"german": "haben", "english": "to have"},
    {"german": "ich", "english": "I"},
    {"german": "werden", "english": "to become, will"},
    {"german": "sie", "english": "she, they"},
    {"german": "von", "english": "from, of"},
    {"german": "nicht", "english": "not"},
    {"german": "mit", "english": "with"},
    {"german": "es", "english": "it"},
    {"german": "sich", "english": "oneself"},
    {"german": "auch", "english": "also"},
    {"german": "auf", "english": "on, upon"},
    {"german": "für", "english": "for"},
    {"german": "an", "english": "at, on"},
    {"german": "er", "english": "he"},
    {"german": "so", "english": "so, thus"},
    {"german": "dass", "english": "that"},
    {"german": "können", "english": "can, to be able to"},
    {"german": "dies", "english": "this"},
    {"german": "als", "english": "as, when"},
    {"german": "ihr", "english": "her, their"},
    {"german": "ja", "english": "yes"},
    {"german": "wie", "english": "how, like"},
    {"german": "bei", "english": "by, at"},
    {"german": "oder", "english": "or"},
    {"german": "wir", "english": "we"},
    {"german": "aber", "english": "but"},
    {"german": "dann", "english": "then"},
    {"german": "man", "english": "one, you (general)"},
    {"german": "da", "english": "there"},
    {"german": "mein", "english": "my"},
    {"german": "schon", "english": "already"},
    {"german": "doch", "english": "however, still"},
    {"german": "bis", "english": "until"},
    {"german": "uns", "english": "us"},
    {"german": "mal", "english": "time (instance)"},
    {"german": "noch", "english": "still, yet"},
    {"german": "nach", "english": "after, to"},
    {"german": "was", "english": "what"},
    {"german": "also", "english": "thus, therefore"},
    {"german": "all", "english": "all"},
    {"german": "wenn", "english": "if, when"},
    {"german": "sehen", "english": "to see"},
    {"german": "lassen", "english": "to let, allow"},
    {"german": "über", "english": "over, about"},
    {"german": "mir", "english": "me (dative)"},
    {"german": "denn", "english": "because, for"},
    {"german": "ganz", "english": "whole, entirely"},
    {"german": "hier", "english": "here"},
    {"german": "durch", "english": "through"},
    {"german": "müssen", "english": "must, to have to"},
    {"german": "viel", "english": "much, many"},
    {"german": "wirklich", "english": "really"},
    {"german": "immer", "english": "always"},
    {"german": "nichts", "english": "nothing"},
    {"german": "dein", "english": "your"},
    {"german": "könnte", "english": "could"},
    {"german": "machen", "english": "to make, do"},
    {"german": "schreiben", "english": "to write"},
    {"german": "kommen", "english": "to come"},
    {"german": "gehen", "english": "to go"},
    {"german": "wissen", "english": "to know"},
    {"german": "leben", "english": "to live"},
    {"german": "geben", "english": "to give"},
    {"german": "finden", "english": "to find"},
    {"german": "nehmen", "english": "to take"},
    {"german": "sprechen", "english": "to speak"},
    {"german": "arbeiten", "english": "to work"},
    {"german": "spielen", "english": "to play"},
    {"german": "stehen", "english": "to stand"},
    {"german": "bleiben", "english": "to stay"},
    {"german": "bringen", "english": "to bring"},
    {"german": "helfen", "english": "to help"},
    {"german": "denken", "english": "to think"},
    {"german": "lernen", "english": "to learn"},
    {"german": "setzen", "english": "to set, place"},
    {"german": "lesen", "english": "to read"},
    {"german": "folgen", "english": "to follow"},
    {"german": "hören", "english": "to hear, listen"},
    {"german": "tragen", "english": "to carry, wear"},
    {"german": "fragen", "english": "to ask"},
    {"german": "öffnen", "english": "to open"},
    {"german": "schließen", "english": "to close"},
    {"german": "laufen", "english": "to run, walk"},
    {"german": "verlieren", "english": "to lose"},
    {"german": "gewinnen", "english": "to win"},
    {"german": "lieben", "english": "to love"},
    {"german": "zeigen", "english": "to show"},
    {"german": "essen", "english": "to eat"},
    {"german": "trinken", "english": "to drink"},
    {"german": "fahren", "english": "to drive, travel"},
    {"german": "beginnen", "english": "to begin"},
    {"german": "verstehen", "english": "to understand"},
    {"german": "erzählen", "english": "to tell, narrate"},
    {"german": "ziehen", "english": "to pull, move"},
    {"german": "schlafen", "english": "to sleep"}
]


def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the english translation for '{word['german']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!!!\n")
            score += 1
        else:
            print(f"Wrong, idiot! The correct answer is '{word['english']}'.\n")
    
    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()