def encoder(password):
    encoded = ''
    for number in password:
        char = str(int(number) + 3)
        encoded += char[-1]
    return encoded


def decoder(encoded):
    decoded = ''
    for number in encoded:
        char = str(10 + int(number) - 3)
        decoded += char[-1]
    return decoded
