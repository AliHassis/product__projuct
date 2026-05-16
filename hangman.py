list = ["supper", "good", "office", "nice"]
import random

word = random.choice(list)
secret = ["_"] * len(word)
attempts = 6
tryy = 0
letters = []

picture = [
    """
  +---+
      |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


print(" ".join(secret))
print(picture[0])


while "_" in secret and attempts > 0:
    letter = input("please gusse a letter:").lower()
    if letter in letters:
        print("yuo already guessed that. try again")
        print(f"you have {attempts} more tries")
        continue
    letters.append(letter)
    if letter in word:
        for x in range(len(word)):
            if word[x] == letter:
                secret[x] = letter
        print(" ".join(secret))
        print(f"you have {attempts} more tries")

    else:
        attempts -= 1
        tryy += 1
        print(" ".join(secret))
        print(f"you have {attempts} more tries")
        print(picture[tryy])


if attempts > 0:
    print(
        """
          ***********
           you win
          ***********"""
    )
else:
    print(
        """
          ***********
           you lose
          ***********"""
    )
