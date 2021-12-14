Extract and display the Nintendo logo from a Gameboy ROM. Gameboy documentation
is available across the web. Thank you to the ROM playing and hacking community!

# Resources

 - [gdev](https://gbdev.gg8.se/wiki/articles/The_Cartridge_Header#0104-0133_-_Nintendo_Logo)
 - [catskull](https://catskull.net/gameboy-boot-screen-logo.html)
 - [stacksmashing (YT)](https://www.youtube.com/watch?v=ix5yZm4fwFQ&t=475s)

# Usage

Show help with the `[-h] [--help]` switches.

```
$ python3 dig.py -h
usage: dig.py [-h] [-x] [-b] [-c CUSTOM] rom_file

extract nintendo logo from gameboy rom

positional arguments:
  rom_file              path to .gb rom file

optional arguments:
  -h, --help            show this help message and exit
  -x, --hex             show hex nibble map of logo
  -b, --bits            show bitmap
  -c CUSTOM, --custom CUSTOM
                        customize the logo foreground and background characters ex) [-c $*] prints
                        a $ foreground and * background ex) [-c $] prints a $ foreground and an
                        empty background hint) you may want to escape some symbols or use quotes
                        e.g. \# or '#'
```

Run on a specified gameboy rom file. Here Pokemon Red is in the current directory.

```
$ python3 dig.py Pokemon_Red_Version.gb
@@   @@ @@                             @@
@@@  @@ @@        @@                   @@
@@@  @@          @@@@                  @@
@@ @ @@ @@ @@ @@  @@  @@@@  @@ @@   @@@@@  @@@@
@@ @ @@ @@ @@@ @@ @@ @@  @@ @@@ @@ @@  @@ @@  @@
@@  @@@ @@ @@  @@ @@ @@@@@@ @@  @@ @@  @@ @@  @@
@@  @@@ @@ @@  @@ @@ @@     @@  @@ @@  @@ @@  @@
@@   @@ @@ @@  @@ @@  @@@@@ @@  @@  @@@@@  @@@@
```

Use the `[-c] [--custom]` switch to choose the text and background characters. Provide a string
and the first character will be the text and the second character the background. The background
is blank if one character is given.


```
$ python3 dig.py Pokemon_Red_Version.gb -c '*'
**   ** **                             **
***  ** **        **                   **
***  **          ****                  **
** * ** ** ** **  **  ****  ** **   *****  ****
** * ** ** *** ** ** **  ** *** ** **  ** **  **
**  *** ** **  ** ** ****** **  ** **  ** **  **
**  *** ** **  ** ** **     **  ** **  ** **  **
**   ** ** **  ** **  ***** **  **  *****  ****

$ python3 dig.py Pokemon_Red_Version.gb -c '\'
\\   \\ \\                             \\
\\\  \\ \\        \\                   \\
\\\  \\          \\\\                  \\
\\ \ \\ \\ \\ \\  \\  \\\\  \\ \\   \\\\\  \\\\
\\ \ \\ \\ \\\ \\ \\ \\  \\ \\\ \\ \\  \\ \\  \\
\\  \\\ \\ \\  \\ \\ \\\\\\ \\  \\ \\  \\ \\  \\
\\  \\\ \\ \\  \\ \\ \\     \\  \\ \\  \\ \\  \\
\\   \\ \\ \\  \\ \\  \\\\\ \\  \\  \\\\\  \\\\

$ python3 dig.py Pokemon_Red_Version.gb -c '$.'
$$...$$.$$.............................$$.......
$$$..$$.$$........$$...................$$.......
$$$..$$..........$$$$..................$$.......
$$.$.$$.$$.$$.$$..$$..$$$$..$$.$$...$$$$$..$$$$.
$$.$.$$.$$.$$$.$$.$$.$$..$$.$$$.$$.$$..$$.$$..$$
$$..$$$.$$.$$..$$.$$.$$$$$$.$$..$$.$$..$$.$$..$$
$$..$$$.$$.$$..$$.$$.$$.....$$..$$.$$..$$.$$..$$
$$...$$.$$.$$..$$.$$..$$$$$.$$..$$..$$$$$..$$$$.
```

Print the hex nibble map or bitmap.

```
$ python3 dig.py Pokemon_Red_Version.gb -xb
c 6 c 0 0 0 0 0 0 1 8 0
e 6 c 0 3 0 0 0 0 1 8 0
e 6 0 0 7 8 0 0 0 1 8 0
d 6 d b 3 3 c d 8 f 9 e
d 6 d d b 6 6 e d 9 b 3
c e d 9 b 7 e c d 9 b 3
c e d 9 b 6 0 c d 9 b 3
c 6 d 9 b 3 e c c f 9 e
110001101100000000000000000000000000000110000000
111001101100000000110000000000000000000110000000
111001100000000001111000000000000000000110000000
110101101101101100110011110011011000111110011110
110101101101110110110110011011101101100110110011
110011101101100110110111111011001101100110110011
110011101101100110110110000011001101100110110011
110001101101100110110011111011001100111110011110
@@   @@ @@                             @@
@@@  @@ @@        @@                   @@
@@@  @@          @@@@                  @@
@@ @ @@ @@ @@ @@  @@  @@@@  @@ @@   @@@@@  @@@@
@@ @ @@ @@ @@@ @@ @@ @@  @@ @@@ @@ @@  @@ @@  @@
@@  @@@ @@ @@  @@ @@ @@@@@@ @@  @@ @@  @@ @@  @@
@@  @@@ @@ @@  @@ @@ @@     @@  @@ @@  @@ @@  @@
@@   @@ @@ @@  @@ @@  @@@@@ @@  @@  @@@@@  @@@@

```
