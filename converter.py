import re

# Prioritize longest matches first (important for transliteration)
vowels = [
    ("oo", "ඌ", "ූ"), ("u\\)", "ඌ", "ූ"), ("uu", "ඌ", "ූ"),
    ("o\\)", "ඕ", "ෝ"), ("oe", "ඕ", "ෝ"),
    ("aa", "ආ", "ා"), ("a\\)", "ආ", "ා"),
    ("Aa", "ඈ", "ෑ"), ("A\\)", "ඈ", "ෑ"), ("ae", "ඈ", "ෑ"),
    ("ii", "ඊ", "ී"), ("i\\)", "ඊ", "ී"), ("ie", "ඊ", "ී"),
    ("ee", "ඊ", "ී"),
    ("ea", "ඒ", "ේ"), ("e\\)", "ඒ", "ේ"), ("ei", "ඒ", "ේ"),
    ("au", "ඖ", "ෞ"),
    ("I", "ඓ", "ෛ"),
    ("A", "ඇ", "ැ"),  # standalone vowel uppercase A
    ("a", "අ", ""), ("i", "ඉ", "ි"), ("e", "එ", "ෙ"),
    ("u", "උ", "ු"), ("o", "ඔ", "ො")
]

# Correct Sinhala IME logic ordering
consonants = [
    ("nndh", "ඳ"), ("nnd", "ඬ"), ("nng", "ඟ"),
    ("Th", "ථ"), ("Dh", "ධ"), ("Ch", "ඡ"), ("ph", "ඵ"),
    ("bh", "භ"), ("sh", "ශ"), ("Sh", "ෂ"), ("GN", "ඥ"),
    ("KN", "ඤ"),
    ("dh", "ද"), ("ch", "ච"), ("kh", "ඛ"), ("th", "ත"),
    ("gh", "ඝ"),
    ("t", "ට"), ("k", "ක"), ("d", "ඩ"), ("n", "න"),
    ("p", "ප"), ("b", "බ"), ("m", "ම"), ("y", "ය"),
    ("j", "ජ"), ("l", "ල"), ("v", "ව"), ("w", "ව"),
    ("s", "ස"), ("h", "හ"), ("N", "ණ"), ("L", "ළ"),
    ("G", "ඝ"), ("T", "ඨ"), ("D", "ඪ"),
    ("P", "ඵ"), ("B", "ඹ"),
    ("f", "ෆ"), ("q", "ඣ"), ("g", "ග"),
    ("r", "ර")  # Keep last → prevents conflict with R
]

# Fix wrong escaped patterns & reorder R rules
specials = [
    ("\\\\h", "ඃ"), ("\\\\N", "ඞ"), ("\\\\R", "ඍ"),
    ("R", "ර්‍"), ("\\\\r", "ර්‍"),
    ("\\\\n", "ං")
]

special_chars = [
    ("ruu", "ෲ"),  # latest replace first
    ("ru", "ෘ")
]

SINHALA_RANGE = "අ-ෆ"

def convert_to_sinhala(text: str) -> str:

    #  Special Sinhala Unicode sequences first
    for pattern, replacement in specials:
        text = re.sub(pattern, replacement, text)

    #  ru/ruu rule before consonant replacements
    for pattern, replacement in special_chars:
        text = text.replace(pattern, replacement)

    # Consonants with rule priority (order matters)
    for pattern, replacement in consonants:
        text = re.sub(pattern, replacement, text)

    # Vowels → full + modifier forms
    for pattern, full_vowel, modifier in vowels:

        # Standalone vowel first
        text = re.sub(rf"(^|\s){pattern}", rf"\1{full_vowel}", text)

        # Vowel modifiers: Sinhala consonant range
        text = re.sub(rf"([{SINHALA_RANGE}]){pattern}", rf"\1{modifier}", text)

    return text
