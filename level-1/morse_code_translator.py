MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
        else:
            morse.append(' ')
    return ' '.join(morse)

def morse_to_text(morse):
    text = []
    for char in morse.split(' '):
        if char in REVERSE_MORSE_DICT:
            text.append(REVERSE_MORSE_DICT[char])
        else:
            text.append(' ')
    return ''.join(text) 

def main():
    print("Morse Code Calculator 🆘")
    choice = input("""
Choose an option:
 1. Text to Morse Code       
 2. Morse Code to Text
                   
>> """)
    if choice == "1":
        text = input("Enter the text to translate to Morse: ").upper()
        morse = text_to_morse(text)
        print("\nMorse Code:")
        print(morse)
        print("\nOver and Out!\n—hazellenuts")
    elif choice == "2":
        morse = input("Enter the Morse code to translate to text (use spaces between letters and '/' between words): ")
        text = morse_to_text(morse)
        print("\nTranslated Text:")
        print(text)
        print("\n--- ...- . .-. / .- -. -.. / --- ..- - -.-.--\n—hazellenuts")
    else:
        print("Invalid choice. Please enter 1 or 2")

if __name__ == "__main__":
    main()