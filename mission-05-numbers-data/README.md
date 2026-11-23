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

The program uses input() to ask the user for a decimal number. Then int() turns the typed text into a whole number. After that, bin() converts the number to binary and hex() converts it to hexadecimal, and the program prints both results.

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 10 | 0b1010 | 0xa |
| 255 | 0b11111111 | 0xff |
| 100 | 0b1100100 | 0x64 |


bin() takes a whole number and gives back its binary form as text. The text starts with 0b, which only tells us that the number is in binary. hex() does the same thing for hexadecimal, and its text starts with 0x. These are the same answers I got by hand in my manual working, just done by Python.

### How text is stored
ASCII code for uppercase A and lowercase a is Uppercase A is 65 and lowercase a is 97 (I checked with ord('A') and ord('a') in Python).

Why a computer needs an encoding standard:
A computer only stores numbers, so every letter needs a number. If each computer used its own numbers, a file from one computer would show wrong characters on another. With a standard like ASCII or Unicode everyone uses the same number for the same character.

A character that is not in basic ASCII:
The rupee sign ₹ is not in basic ASCII, because