
def to_binary(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result   # remainder goes in front
        n = n // 2
    return result


def to_hex(n):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % 16] + result
        n = n // 16
    return result


number = int(input("Enter a decimal number: "))
print("Binary:", to_binary(number))
print("Hexadecimal:", to_hex(number))
