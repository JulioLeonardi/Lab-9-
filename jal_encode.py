def encoder(password):
    encoded = ''
    for number in password:
        char = str(int(number) + 3)
        encoded += char[-1]
    return encoded

