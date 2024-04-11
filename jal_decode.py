def decoder(encoded):
    decoded = ''
    for number in encoded:
        char = str(10 + int(number) - 3)
        decoded += char[-1]
    return decoded