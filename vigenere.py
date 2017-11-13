from helpers import alphabet_position, rotate_character

def encrypt(text, encrypt_key):
    """Receives as input a string and an encryption key string.
    Returns the result of rotating each letter in text by the 
    associated key's rotation places to the right. """
    encrypt_rot = []
    rotated_string = ''
    idx = 0
    for i in range(len(encrypt_key)):
        encrypt_rot.append(alphabet_position(encrypt_key[i]))
    for position in range(len(text)):
        rotated_char = rotate_character(text[position], encrypt_rot[idx])
        rotated_string += rotated_char
        if rotated_char.isalpha():
            idx += 1
            if idx == len(encrypt_key):
                idx -= len(encrypt_key)
    return rotated_string

def main():
    from sys import argv, exit
    # print("This is what the user typed on the command line:", argv)
    if len(argv) == 2:
        for pos in range(len(argv[1])):
            if not argv[1][pos].isalpha():
                print("usage: python vigenere.py keyword")
                print("Arguments:")
                print('-keyword : The string to be used as a "key" to encrypt your message. Should')
                print('only contain alphabetic characters-- no numbers or special characters.')
                exit()
    else:
        print("usage: python vigenere.py keyword")
        exit()
    user_msg = input("Type a message:")
    encrypt_key = argv[1]
    print(encrypt(user_msg, encrypt_key))

if __name__ == "__main__":
    main()