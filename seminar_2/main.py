from random import choice

from GemGenerator import GemGenerator
from GoldGenerator import GoldGenerator
from StoneGenerator import StoneGenerator


def main():
    lst = (GoldGenerator(), GemGenerator(), StoneGenerator())
    for i in range(5):
        choice(lst).open_reward()

print(main())






