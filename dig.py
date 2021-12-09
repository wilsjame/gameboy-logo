red = "Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb"

# Imports, Types, Utility Functions
from typing import *

Game = list

def hex(hexstr: str) -> int:
    return int(hexstr, 16)

def read_input(rom_file: str=red) -> Game:
    game = list() 
    with open(rom_file, "rb") as f:
        byte = f.read(1)
        game.append(byte)
        while byte:
            byte = f.read(1)
            game.append(byte)
    return game

# scratch work
game = read_input()

# find nintendo logo
for addr in range(hex('104'), hex('133') + 1):
    print(game[addr].hex(), end=' ')
