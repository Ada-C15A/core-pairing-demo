def get_digits(characters):
    if not characters:
        return None

    digits = []
    for character in characters:
        if character.isdigit():
            digits.append(character)
    return int("".join(digits))
