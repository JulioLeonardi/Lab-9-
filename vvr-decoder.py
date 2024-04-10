def decode(pass_word):
    string2=""
    for chars in pass_word:
        chars = str((int(chars)+10)-3)
        string2 += chars[-1]

    return string2