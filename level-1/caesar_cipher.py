print("""
CAESAR CIPHER      
""")

while True:
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    text = input("your text: ")
    shift = int(input("shift: "))

    ciphered_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if choice == "e" else -shift
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            ciphered_text += chr((ord(char) - start + shift_amount)%26 + start)
        else:
            ciphered_text += char
    print(ciphered_text)
    print("")
    pg = input("Enter to continue or 'e' to end: ").lower()
    if pg == "e":
        print("Goodbye! —hazellenuts")
        break
    else:
        continue
