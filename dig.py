import argparse
from   typing   import *

# Types
Byte   = str
Nibble = str
Game   = List[Byte]
Logo   = List[List[Nibble]]

def read_input(rom_file: str) -> Game:
    """Read Gameboy ROM and return game data as a list of bytes"""
    game = list()
    with open(rom_file, "rb") as f:
        byte = f.read(1)
        game.append(byte)
        while byte:
            byte = f.read(1)
            game.append(byte)
    return game

# this is the actual algorithm all else is extra! 
def extract_logo(game: Game) -> Logo:
    """Extract logo from game data and return as a 2D nibble map"""
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

    return hexmap

def visualize(logo: Logo, in_hex: bool=False, in_bits: bool=False, custom: str='* ') -> None:
    """Visualize extracted Nintendo logo stored in a 2D list"""
    for i in range(8):
        for j in range(12):
            if in_hex:
                print(logo[i][j], end=' ')
            elif in_bits:
                print(bin(int(logo[i][j], 16))[2:].zfill(4), end='')
            else:
                foreground = custom[0]
                background = ' ' if len(custom) == 1 else custom[1]
                for bit in str(bin(int(logo[i][j], 16))[2:].zfill(4)):
                    if bit == '1':
                        print(foreground, end='')
                    else:
                        print(background, end='')
        print()

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="extract nintendo logo from .gb rom")
    parser.add_argument("-x", "--hex", action="store_true", help="show hex nibble map of logo")
    parser.add_argument("-b", "--bits", action="store_true", help="show bitmap")
    parser.add_argument("-c", "--custom", type=str, default='@ ', help="customize the logo foreground and background characters ex) [-c $*] prints a $ foreground and * background ex) [-c $] prints a $ foreground and an empty background hint) you may want to escape some symbols or use quotes e.g. \# or '#'")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    rom_path = "Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb"
    game = read_input(rom_path)
    logo = extract_logo(game)

    if args.hex:
        visualize(logo, in_hex=True)
    if args.bits:
        visualize(logo, in_bits=True)

    # always show logo
    visualize(logo, custom=args.custom)

main()

# scratch work
# nintendo logo
# each byte is a 2x4 pixel bitmap
# each two byte pair represents 4x4 pixels
# entire logo is 8x12 nibbles or 8x48 bits 
# bytes are scanned vertically
# upper and lower halfs
