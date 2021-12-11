# test input
red = "Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb"

# Imports, Types, Utility Functions
from typing import *

Byte   = str
Nibble = str
Game   = List[Byte]
Logo   = List[List[Nibble]]

def read_input(rom_file: str=red) -> Game:
    """Read Gameboy ROM and return game data as a list of bytes"""
    game = list()
    with open(rom_file, "rb") as f:
        byte = f.read(1)
        game.append(byte)
        while byte:
            byte = f.read(1)
            game.append(byte)
    return game

def visualize(logo: Logo, in_bits: bool=False) -> None:
    """Visualize extracted Nintendo logo stored in a 2D list"""
    for i in range(8):
        for j in range(12):
            if in_bits:
                print(bin(int(logo[i][j], 16))[2:].zfill(4), end='')
            else:
                print(logo[i][j], end=' ')
        print()

# scratch work
# nintendo logo
# each byte is a 2x4 pixel bitmap
# each two byte pair represents 4x4 pixels
# entire logo is 8x12 nibbles or 8x48 bits 
# bytes are scanned vertically
# upper and lower halfs
game   = read_input()
nibble = list()
hexmap = [[0] * 12 for row in range(8)] # of nibbles

# extract logo from game data
for addr in range(int('0x0104', 16), int('0x0133', 16) + 1):
    nibble.append(game[addr].hex()[0])
    nibble.append(game[addr].hex()[1])

# arrange logo data in correct order
for i in range(2*48):
    if (i + 1) % 4 == 0:
        if i < 48:             
            for j in range(4): # top half
                hexmap[j][((i + 1) // 4) - 1] = nibble[i - (3 - j)]
        else:                  
            for j in range(4): # bottom half
                hexmap[j + 4][(((i - 48) + 1) // 4) - 1] = nibble[i - (3 - j)]

visualize(hexmap)
visualize(hexmap, in_bits=True)
