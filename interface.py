import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

from algorithm import *
from Notes import *

while True:
    clear()

    print_instructions()
    choose(input("Введите команду (1 2 3 или 4) "))
    input("Введите enter чтобы продолжить")