# Mission 5 - Numbers and Data

## Objective
My task was to convert numbers between decimal, binary and hexadecimal by hand, check them with Python, build a small converter program, and explain how text is stored.

## Work completed

### Manual conversions
| Question | My working and answer |
|---|---|
| Decimal 13 to binary | 13/2=6 r1, 6/2=3 r0, 3/2=1 r1, 1/2=0 r1. Reading the remainders from the bottom up gives 1101 |
| Decimal 25 to binary | 25/2=12 r1, 12/2=6 r0, 6/2=3 r0, 3/2=1 r1, 1/2=0 r1. Reading from the bottom up gives 11001 |
| Binary 1010 to decimal | 8 + 0 + 2 + 0 = 10 |
| Binary 1101 to decimal | 8 + 4 + 0 + 1 = 13 |
| Hexadecimal A to decimal | A is 10 in hex, so the answer is 10 |
| Hexadecimal 1F to decimal | (1 x 16) + 15 = 31 |
| Binary 1111 to hexadecimal | 1111 is one group of four bits. 8+4+2+1 = 15 which is F, so F |

### Python verification
| Expression I tested | Result | Matches my manual answer? |
|---|---|---|
| bin(13) | 0b1101 | Yes, 1101 (0b is just Python saying it's binary) |
| bin(25) | 0b11001 | Yes, 11001 |
| int('1F', 16) | 31 | Yes |
| hex(int('1111', 2)) | 0xf | Yes, F (0x means hex) |

I also checked the remaining ones (int('1010', 2), int('1101', 2), int('A', 16)) and they gave 10, 13 and 10. All matched.

### Number converter (number_converter.py)
How the program works:
It asks the user for a decimal number and then prints it in binary and in hexadecimal. I wrote the two conversion functions myself instead of using bin() and hex(), so I could see the method working.

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 10 | 1010 | A |
| 255 | 11111111 | FF |
| 100 | 1100100 | 64 |

What the binary and hexadecimal conversion functions do:
to_binary keeps dividing the number by 2 and takes the remainder each time, and puts the new remainder in front. This is same as reading the remainders from the bottom up in my manual working. to_hex does the same thing but divides by 16, and it uses the string "0123456789ABCDEF" to change remainders 10 to 15 into A to F.

### How text is stored
ASCII code for uppercase A and lowercase a:
Uppercase A is 65 and lowercase a is 97 (I checked with ord('A') and ord('a') in Python).

Why a computer needs an encoding standard:
A computer only stores numbers, so every letter needs a number. If each computer used its own numbers, a file from one computer would show wrong characters on another. With a standard like ASCII or Unicode everyone uses the same number for the same character.


## Commands used
- `python3`
- `python3 number_converter.py`
- `bin()`, `hex()`, `int(x, base)` and `ord()` inside Python

## My understanding
Computers store everything as binary. Hex is a shorter way to write binary because one hex digit is 4 bits. Now I can convert decimal, binary and hex by hand and check it with Python. Text is also stored as numbers, and the encoding standard decides which number is which character.

## Difficulties faced
I didn't know how to check binary and hex in the Python terminal at all. I had never used int(), bin(), hex() or ord() before, so I didn't know what to type or what the 0b and 0x in the answers meant. I also mixed up the order of the remainders in binary at first.

## How I resolved them
I searched on google and asked ai how these functions work, then tried them myself in the Python terminal until I got it. Now I know bin() gives binary, hex() gives hex, int('1F', 16) turns it back to decimal and ord('A') gives the ASCII number. I checked each answer with my manual working, and that's how I fixed the remainder order too.

## Evidence

Files for this mission: `README.md` and `number_converter.py`


## Commit details
Mission 5 README and number_converter.py committed to the repo.
