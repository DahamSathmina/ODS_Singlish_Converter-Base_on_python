import re

vowels = [
    ("oo", "ඌ", "ූ"), ("u)", "ඌ", "ූ"), ("uu", "ඌ", "ූ"),
    ("o)", "ඕ", "ෝ"), ("oe", "ඕ", "ෝ"),
    ("aa", "ආ", "ා"), ("a)", "ආ", "ා"),
    ("Aa", "ඈ", "ෑ"), ("A)", "ඈ", "ෑ"), ("ae", "ඈ", "ෑ"),
    ("ii", "ඊ", "ී"), ("i)", "ඊ", "ී"), ("ie", "ඊ", "ී"),
    ("ee", "ඊ", "ී"),
    ("ea", "ඒ", "ේ"), ("e)", "ඒ", "ේ"), ("ei", "ඒ", "ේ"),
    ("au", "ඖ", "ෞ"),
    ("I", "ඓ", "ෛ"),
    ("A", "ඇ", "ැ"),
    ("a", "අ", ""), ("i", "ඉ", "ි"), ("e", "එ", "ෙ"),
    ("u", "උ", "ු"), ("o", "ඔ", "ො")
]

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
    ("r", "ර")
]

specials = [
    (r"\\h", "ඃ"), (r"\\N", "ඞ"), (r"\\R", "ඍ"),
    (r"R", "ර්‍"), (r"\\r", "ර්‍"),
    (r"\\n", "ං")
]

special_chars = [
    ("ruu", "ෲ"),
    ("ru", "ෘ")
]

SINHALA_RANGE = "අ-ෆ"

def convert_to_sinhala(text: str) -> str:
    # Specials first
    for pattern, replacement in specials:
        text = re.sub(pattern, replacement, text)

    # ru/ruu replacements
    for pattern, replacement in special_chars:
        text = text.replace(pattern, replacement)

    # Consonants
    for pattern, replacement in consonants:
        text = text.replace(pattern, replacement)

    # Vowels
    for pattern, full_vowel, modifier in vowels:
        escaped_pattern = re.escape(pattern)
        text = re.sub(rf"(^|\s){escaped_pattern}", rf"\1{full_vowel}", text)
        text = re.sub(rf"([{SINHALA_RANGE}]){escaped_pattern}", rf"\1{modifier}", text)

    return text

