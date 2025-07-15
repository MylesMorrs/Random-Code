from spellchecker import SpellChecker

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

spell = SpellChecker()
cipher = input('Input Cypher To Solve: ')
shift = int(input('Shift amount: '))
decoded = shift_cipher(cipher, shift)
print(f"\nShifted sentence: {decoded}")

words = decoded.split()
for word in words:
    if word.lower() in spell:
        print(f"'{word}' is a real word.")
    else:
        suggestion = spell.correction(word)
        print(f"'{word}' is not a real word. Suggestion: {suggestion}")
