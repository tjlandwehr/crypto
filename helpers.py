def alphabet_position(letter):
    """Receives a letter (i.e., a string with only one alphabetic character) 
    and returns the 0-based numerical position 
    of that letter within the alphabet."""
    num_position = ord(letter.lower()) - 97
    return num_position

def rotate_character(char, rot):
    """Return a new string of length 1, 
    the result of rotating char by rot number of places to the right."""
    if char.isalpha():
        char_position = alphabet_position(char)
        temp_char = ((char_position + rot) % 26)
        new_char = ''
        if char.isupper():
            new_char += chr(temp_char + 65)
        else:
            new_char += chr(temp_char + 97)
        return new_char
    else:
        return char
