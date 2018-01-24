"""Hangman challenge

https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1124/handouts/200%20Assignment%204.pdf
"""
import string
from typing import Union


class TerminalOutput:
    @staticmethod
    def info(s):
        print(s)

    @staticmethod
    def status(g: 'Game'):
        print("Password: {password}\n"
              "Guessed letters: {guessed}\n"
              "Lives left: {lives}\n".format(password=g.masked_secret(), guessed=' '.join(g.guessed), lives=g.lives))


class TerminalInput:
    @staticmethod
    def is_valid(s: str) -> bool:
        return len(s) == 1 and s in string.ascii_letters

    @staticmethod
    def get_input() -> str:
        return input()

# TODO: pierscin: words from file.
class Game:
    mask = '-'
    lives = 8

    def __init__(self, secret: str, input=TerminalInput, output=TerminalOutput):
        self.secret = secret.upper()
        self.input = input
        self.output = output

        self.lives = Game.lives
        self.guessed = set()

    def guess(self, s: str) -> Union[bool, None]:
        s = s.upper()
        correct = s in self.secret

        if not correct: self.lives -= 1

        self.guessed.add(s)

        return correct

    def masked_secret(self) -> str:
        return ''.join([c if c in self.guessed else Game.mask for c in self.secret])

    def finished(self) -> bool:
        return not self.lives or self.won()

    def won(self) -> bool:
        return set(self.secret).issubset(self.guessed)

    def play(self):
        while not self.finished():
            self.output.info("Waiting for a letter: ")

            s = self.input.get_input()

            if self.input.is_valid(s):
                hit = self.guess(s)

                if hit:
                    self.output.info("Correct guess!")
                else:
                    self.output.info("Incorrect guess!")

                self.output.status(self)
            else:
                self.output.info("Input {0} is not correct".format(s))

        if self.won():
            self.output.info("Congratulations, you guessed it!")
        else:
            self.output.info("Dead! :(")
