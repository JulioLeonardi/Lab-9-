def decode(password):
    string2=""
    for chars in password:
        chars = str((int(chars)+10)-3)
        string2 += chars[-1]

    return string2