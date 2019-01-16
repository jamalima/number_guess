#!/usr/bin/env python
#
# Author: Maryam Jamali, 1397
# Description: Number Guess
#
import random

class NumberGuess:

    def __init__(self):
        self.target = random.randint(1,100)
        self.choice = 0
        self.chance = 5
        self.many = ['first', 'second', 'third', 'fourth', 'fifth']
        self.first = 0
        self.end = 100

    def compare(self):
        if self.choice == self.target:
            print("** You are Win ! **")
            exit(0)
        elif self.choice > self.target:
            self.end = self.choice
            print("** Your choice is UPPER than target !")
        elif self.choice < self.target:
            print("** Your choice is LOWER than target !")
            self.first = self.choice

    def play(self):
        for i in range(5):
            try:
                self.choice = int(input("Please enter your {} choice from {} to {} : "
                                        .format(self.many[i], self.first, self.end)))
            except ValueError:
                print("** Please enter digit for your choice ! **")
                return False

            while (self.choice < self.first) or (self.choice > self.end):
                print("** Your choice is incorrect ! **")
                return False

            self.compare()
        print("** You loss ! **")
        print("My target is {}".format(self.target))

if __name__ == "__main__":
    enter = input ("Press enter to start or Q to quit !")
    if enter.lower == 'q':
        exit(0)
    number_guess = NumberGuess()
    number_guess.play()
    exit(0)

