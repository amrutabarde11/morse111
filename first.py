# Morse Code Dictionary
MORSE_CODE_DICT = { 
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Function to encrypt plain text into Morse code
def encrypt(message):
    morse_code = ''
    for letter in message.upper():  # Convert to uppercase for consistency
        if letter != ' ':
            morse_code += MORSE_CODE_DICT.get(letter, '') + ' '  # Convert to Morse code
        else:
            morse_code += ' '  # Add a space to separate words
    return morse_code

# Function to decrypt Morse code into plain text
def decrypt(morse_message):
    morse_message += ' '  # Extra space to ensure last code is processed
    translated_text = ''
    morse_char = ''
    space_count = 0
    
    for symbol in morse_message:
        if symbol != ' ':
            space_count = 0  # Reset space count
            morse_char += symbol  # Build the current Morse code character
        else:
            space_count += 1
            if space_count == 2:  # If two spaces, add a space in plain text
                translated_text += ' '
            elif morse_char:  # If there's a complete Morse code character
                translated_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_char)]
                morse_char = ''  # Reset for next character
    return translated_text

# Main function to run the encryption and decryption
def main():
    print("Welcome to the Morse Code Translator!")
    
    # Ask the user what they want to do
    choice = input("Type '1' for Encryption, '2' for Decryption: ")

    if choice == '1':
        # Encryption mode
        message = input("Enter the message you want to encrypt: ")
        result = encrypt(message)
        print("Morse Code:", result)
    
    elif choice == '2':
        # Decryption mode
        morse_message = input("Enter the Morse code you want to decrypt (use space between letters): ")
        result = decrypt(morse_message)
        print("Plain Text:", result)
    
    else:
        print("Invalid choice. Please enter '1' or '2'.")

# Run the main function when the program starts

    main()