morse_code_english = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--.."
}
morse_code_morse = {
    ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f",
    "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
    "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",    "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
    "-.--": "y", "--..": "z"
}
print("English To Morse Code / Morse Code To English. type english to enter english to morse code. type morse to enter morse code to english.")
decision = input("Select Mode-> english / morse: ")
if decision.lower() == "english":
    print("input english to translate to morse code.")
    translation = input("Input: ").lower()
    for input_letter in translation:
        if input_letter == " ":
            print("/", end=" ")
        else:
            print(morse_code_english[input_letter], end=" ")
elif decision.lower() == "morse":
    print("input morse code to translate to english.")
    translation = input("input: ").split()
    for morse in translation:
        if morse == "/":
            print(" ", end="")
        else:
            print(morse_code_morse[morse], end= "")