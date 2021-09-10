import random


def get_offset():
    choices = '!@#$%^&*()_='
    signs = '+-'
    code_choice = random.choice(choices)
    sign_choice = random.choice(signs)
    code_symbol = sign_choice + code_choice

    offset_list = [5, -3, 11, -10, -6, 4, 6, 8, -9, 2, 3, -7]
    offset = offset_list[choices.find(code_choice)]

    if sign_choice == '-':
        offset *= -1

    return code_symbol, offset


def encrypt(message, code_symbol, offset):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    formatted_message = message.split()

    new_message = [code_symbol]

    for word in formatted_message:
        new_word = ''
        for char in word:
            if alphabet.index(char) + offset > 25:
                new_char = alphabet[(alphabet.index(char) + offset) % 26]
            else:
                new_char = alphabet[alphabet.index(char) + offset]

            new_word += new_char
        new_message.append(new_word)

    new_message = " ".join(new_message)
    return new_message


def decrypt(encrypted_message):
    # Derive offset
    formatted_message = encrypted_message.split()
    code_symbol = formatted_message[0]
    choices = '!@#$%^&*()_='
    offset_list = [5, -3, 11, -10, -6, 4, 6, 8, -9, 2, 3, -7]
    offset = offset_list[choices.find(code_symbol[1])]
    if code_symbol[0] == '-':
        offset *= -1

    # Get inverse of offset to decrypt messagae
    offset *= -1

    formatted_message.pop(0)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    decrypted_message = []

    for word in formatted_message:
        new_word = ''
        for char in word:
            if alphabet.index(char) + offset > 25:
                new_char = alphabet[(alphabet.index(char) + offset) % 26]
            else:
                new_char = alphabet[alphabet.index(char) + offset]

            new_word += new_char
        decrypted_message.append(new_word)

    decrypted_message = " ".join(decrypted_message)
    return decrypted_message
