from spellchecker import SpellChecker
# pip install pyspellchecker


def shift_cipher(cipher, shift=1):
    result = []
    for char in cipher:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

def close_window():
        root.destroy()

def main():
    spell = SpellChecker()
    cipher = input('Input Cypher To Solve: ')

    for shift in range(-25, 26):
        decoded = shift_cipher(cipher, shift)
        words = decoded.split()
        if all(word.lower() in spell for word in words if word.isalpha()):
            print(decoded, shift)
            return
    

    print("\nNo real words found for any shift in the given range.")

if __name__ == "__main__":
    main()
