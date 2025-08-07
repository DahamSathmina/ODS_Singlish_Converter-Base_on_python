import re

vowels = [
    ("oo", "ඌ", "ූ"), ("o\\)", "ඕ", "ෝ"), ("oe", "ඕ", "ෝ"),
    ("aa", "ආ", "ා"), ("a\\)", "ආ", "ා"), ("Aa", "ඈ", "ෑ"),
    ("A\\)", "ඈ", "ෑ"), ("ae", "ඈ", "ෑ"), ("ii", "ඊ", "ී"),
    ("i\\)", "ඊ", "ී"), ("ie", "ඊ", "ී"), ("ee", "ඊ", "ී"),
    ("ea", "ඒ", "ේ"), ("e\\)", "ඒ", "ේ"), ("ei", "ඒ", "ේ"),
    ("uu", "ඌ", "ූ"), ("u\\)", "ඌ", "ූ"), ("au", "ඖ", "ෞ"),
    ("/\\a", "ඇ", "ැ"), ("a", "අ", ""), ("A", "ඇ", "ැ"),
    ("i", "ඉ", "ි"), ("e", "එ", "ෙ"), ("u", "උ", "ු"),
    ("o", "ඔ", "ො"), ("I", "ඓ", "ෛ")
]

consonants = [
    ("nnd", "ඬ"), ("nndh", "ඳ"), ("nng", "ඟ"), ("Th", "ථ"),
    ("Dh", "ධ"), ("gh", "ඝ"), ("Ch", "ඡ"), ("ph", "ඵ"),
    ("bh", "භ"), ("sh", "ශ"), ("Sh", "ෂ"), ("GN", "ඥ"),
    ("KN", "ඤ"), ("Lu", "ළු"), ("dh", "ද"), ("ch", "ච"),
    ("kh", "ඛ"), ("th", "ත"), ("t", "ට"), ("k", "ක"),
    ("d", "ඩ"), ("n", "න"), ("p", "ප"), ("b", "බ"),
    ("m", "ම"), ("\\u005Cy", "‍ය"), ("Y", "‍ය"), ("y", "ය"),
    ("j", "ජ"), ("l", "ල"), ("v", "ව"), ("w", "ව"),
    ("s", "ස"), ("h", "හ"), ("N", "ණ"), ("L", "ළ"),
    ("K", "ඛ"), ("G", "ඝ"), ("T", "ඨ"), ("D", "ඪ"),
    ("P", "ඵ"), ("B", "ඹ"), ("f", "ෆ"), ("q", "ඣ"),
    ("g", "ග"), ("r", "ර")
]

specials = [
    ("\\n", "ං"), ("\\h", "ඃ"), ("\\N", "ඞ"), ("\\R", "ඍ"),
    ("R", "ර්\u200D"), ("\\r", "ර්\u200D")
]

special_chars = [
    ("ruu", "ෲ"), ("ru", "ෘ")
]

def convert_to_sinhala(text: str) -> str:
    # Replace special characters first
    for pattern, replacement in specials:
        text = re.sub(pattern, replacement, text)

    # Replace special chars like "ruu" and "ru"
    for pattern, replacement in special_chars:
        text = text.replace(pattern, replacement)

    # Replace consonants
    for pattern, replacement in consonants:
        text = text.replace(pattern, replacement)

    # Replace vowels: handle full vowels (start of word or after space) and modifiers (after consonants)
    for pattern, full_vowel, modifier in vowels:
        # Standalone vowels
        text = re.sub(rf'(^|\s){pattern}', rf'\1{full_vowel}', text)
        # Vowel modifiers after consonants (range: Sinhala letters: ක-ෆ)
        text = re.sub(rf'([ක-ෆ]){pattern}', rf'\1{modifier}', text)

    return text
