import random

class Guessing:

    def __init__(self):
        input = raw_input("Would you like to Play? y/n: ")
        if input == "y":
            words = ["Animal", "Doctor", "People", "World", "Coding"]
            self.word = random.choice(words)
            self.hidden_words = "*"*len(self.word)
            self.count = 0
            self.char_input = ""
        else:
            self.__del__()

    def keep_guessing(self):
        while True:
            print("Enter your character : ")
            self.char_input = raw_input()
            print(self.char_input)
            self.guess(self.char_input)
            if self.count == 6:
                print("Game Over, You Lose!")
                self.__init__()


    def guess(self, char):
        print(self.word.lower())
        if char.lower() in self.word.lower():
            indexes = [i for i, v in enumerate(self.word.lower()) if v == char.lower()]
            self.hidden_words = list(self.hidden_words)
            for i in indexes:
                self.hidden_words[i] = char.lower()
            self.hidden_words = "".join(self.hidden_words)
            print(self.hidden_words)
            if self.hidden_words.count("*") == 0:
                print("Congratulations!! You Win")
                self.__init__()
        else:
            self.count+=1
            self.print_myhangman()

    def print_myhangman(self):
            full_hangman = [
            "____",
            "| |",
            "| | ",
            "| 0 ",
            "|/|\ ",
            "|/ \ "
            ]

            some_count = 0
            for i in full_hangman:
                some_count +=1
                print(i)
                if some_count == self.count:
                    break

    def __del__(self):
        return False




