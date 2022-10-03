dicoUpper = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', '0': '-----', ' ': ' ', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
dicoLower = {k.lower() : v for k, v in dicoUpper.items()}
dicoLowerRev = {v : k for k, v in dicoLower.items()}

def morse (phrase):
    code: str = ""
    phrase = str(phrase)

    for i in phrase:
        if i in dicoUpper:
            code += dicoUpper[i] + " "
        elif i in dicoLower:
            code += dicoLower[i] + " "
        else:
            code += "¢" + " "
        
    code = code[:-1]
    return code

def decoder (code):
    transcrit: str = ""
    code = str(code)
    code = code.replace("   ", " ç ")
    codelst = code.split(" ")

    for i in codelst:
        if i in dicoLowerRev:
            transcrit += dicoLowerRev[i]
        elif i == "ç":
            transcrit += " "
        else:
            transcrit += "¢"
    return transcrit

while True:
    choice: str = input("To encode, press e. To decode, press d: ")
    if choice.lower() == "e":
        string_to_encode: str = input("Enter the sentence you want to encode: ")
        print(morse(string_to_encode))
    elif choice.lower() == "d":
        string_to_decode: str = input("Enter the morse code you want to decode: ")
        print(decoder(string_to_decode))
    else: 
        print("Please press e or d")
    moar: str = input("Do you want to do another operation ? y/n: ")
    if moar.lower() != "y":
        break