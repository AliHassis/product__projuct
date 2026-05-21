import random

# قائمة الكلمات
words_pool = ["supper", "good", "office", "nice", "python"]

word = random.choice(words_pool)
secret = ["_"] * len(word)
attempts = 6
tryy = 0
letters = []

# رسومات الرجل المشنوق نظيفة ومحمية بـ r لمنع الأخطاء
picture = [
    r"""
  +---+
      |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

print("--- Welcome to Hangman Game ---")
print(" ".join(secret))
print(picture[0])

while "_" in secret and attempts > 0:
    letter = input("\nPlease guess a letter: ").lower()
    
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue
        
    if letter in letters:
        print(f"You already guessed '{letter}'. Try again.")
        continue
        
    letters.append(letter)
    
    if letter in word:
        for x in range(len(word)):
            if word[x] == letter:
                secret[x] = letter
        print("\nGood job!")
        print(" ".join(secret))
        print(f"Tries left: {attempts}")
        print(picture[tryy])
    else:
        attempts -= 1
        tryy += 1
        print("\nWrong guess!")
        print(" ".join(secret))
        print(f"Tries left: {attempts}")
        print(picture[tryy])

if "_" not in secret:
    print("\n***********\n YOU WIN! \n***********")
    print(f"The word was: {word}")
else:
    print("\n***********\n YOU LOSE! \n***********")
    print(f"The correct word was: {word}")