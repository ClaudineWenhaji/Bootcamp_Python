import string

def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if text is None:
        text = input("what's the text to analyze?\n")
    
    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return
    
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0 
    printable = 0

    for char in text:
        if char.isprintable():
            printable += 1

        if char.isupper():
            upper += 1
        elif char.lower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char == " ":
            spaces += 1
    print(f"The text contains {printable} printable character(s):")
    print(f"- {upper} letter(s)")
    print(f"- {lower} letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")    