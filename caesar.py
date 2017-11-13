from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    """Receives as input a string and an integer, rot, which specifies 
    the rotation amount.  Returns the result of rotating each letter in 
    the text by rot places to the right."""
    rotated_string = ''
    for position in range(len(text)):
        rotated_string += rotate_character(text[position], rot)
    return rotated_string

def main():
    from sys import argv, exit
    # print("This is what the user typed on the command line:", argv)
    if len(argv) == 2:
        if not argv[1].isdigit():
            print("usage: python caesar.py n")
            print("Arguments:")
            print('-n : The number of rotations to encrypt your message.')
            print('Should only contain a digit-- no letters or special characters.')
            exit()
    else:
        print("usage: python caesar.py n")
        print("Arguments:")
        print('-n : The number of rotations to encrypt your message.')
        print('Should only contain a digit-- no letters or special characters.')
        exit()
    user_msg = input("Type a message:")
    rotations = int(argv[1])
    # rotations = int(input("Rotate by:"))
    print(encrypt(user_msg, rotations))

if __name__ == "__main__":
    main()