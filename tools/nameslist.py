#!/usr/bin/python3

Vowels = [
    0x0A05,  # GURMUKHI LETTER A
    0x0A06,  # GURMUKHI LETTER AA
    0x0A07,  # GURMUKHI LETTER I
    0x0A08,  # GURMUKHI LETTER II
    0x0A09,  # GURMUKHI LETTER U
    0x0A0A,  # GURMUKHI LETTER UU
    0x0A0F,  # GURMUKHI LETTER EE
    0x0A10,  # GURMUKHI LETTER AI
    0x0A13,  # GURMUKHI LETTER OO
    0x0A14,  # GURMUKHI LETTER AU
    ]

Matras = [
    0x0A3E,  # GURMUKHI VOWEL SIGN AA
    0x0A3F,  # GURMUKHI VOWEL SIGN I
    0x0A40,  # GURMUKHI VOWEL SIGN II
    0x0A41,  # GURMUKHI VOWEL SIGN U
    0x0A42,  # GURMUKHI VOWEL SIGN UU
    0x0A47,  # GURMUKHI VOWEL SIGN EE
    0x0A48,  # GURMUKHI VOWEL SIGN AI
    0x0A4B,  # GURMUKHI VOWEL SIGN OO
    0x0A4C,  # GURMUKHI VOWEL SIGN AU
    ]

Consonants = [
    0x0A15,  # GURMUKHI LETTER KA
    0x0A16,  # GURMUKHI LETTER KHA
    0x0A17,  # GURMUKHI LETTER GA
    0x0A18,  # GURMUKHI LETTER GHA
    0x0A19,  # GURMUKHI LETTER NGA
    0x0A1A,  # GURMUKHI LETTER CA
    0x0A1B,  # GURMUKHI LETTER CHA
    0x0A1C,  # GURMUKHI LETTER JA
    0x0A1D,  # GURMUKHI LETTER JHA
    0x0A1E,  # GURMUKHI LETTER NYA
    0x0A1F,  # GURMUKHI LETTER TTA
    0x0A20,  # GURMUKHI LETTER TTHA
    0x0A21,  # GURMUKHI LETTER DDA
    0x0A22,  # GURMUKHI LETTER DDHA
    0x0A23,  # GURMUKHI LETTER NNA
    0x0A24,  # GURMUKHI LETTER TA
    0x0A25,  # GURMUKHI LETTER THA
    0x0A26,  # GURMUKHI LETTER DA
    0x0A27,  # GURMUKHI LETTER DHA
    0x0A28,  # GURMUKHI LETTER NA
    0x0A2A,  # GURMUKHI LETTER PA
    0x0A2B,  # GURMUKHI LETTER PHA
    0x0A2C,  # GURMUKHI LETTER BA
    0x0A2D,  # GURMUKHI LETTER BHA
    0x0A2E,  # GURMUKHI LETTER MA
    0x0A2F,  # GURMUKHI LETTER YA
    0x0A30,  # GURMUKHI LETTER RA
    0x0A32,  # GURMUKHI LETTER LA
    0x0A33,  # GURMUKHI LETTER LLA
    0x0A35,  # GURMUKHI LETTER VA
    0x0A36,  # GURMUKHI LETTER SHA
    0x0A38,  # GURMUKHI LETTER SA
    0x0A39,  # GURMUKHI LETTER HA
    0x0A59,  # GURMUKHI LETTER KHHA
    0x0A5A,  # GURMUKHI LETTER GHHA
    0x0A5B,  # GURMUKHI LETTER ZA
    0x0A5C,  # GURMUKHI LETTER RRA
    0x0A5E,  # GURMUKHI LETTER FA
    ]

Nukta = [
    0x0A3C,  # GURMUKHI SIGN NUKTA
    ]

Virama = [
    0x0A4D,  # GURMUKHI SIGN VIRAMA
    ]

Digits = [
    0x0A66,  # GURMUKHI DIGIT ZERO
    0x0A67,  # GURMUKHI DIGIT ONE
    0x0A68,  # GURMUKHI DIGIT TWO
    0x0A69,  # GURMUKHI DIGIT THREE
    0x0A6A,  # GURMUKHI DIGIT FOUR
    0x0A6B,  # GURMUKHI DIGIT FIVE
    0x0A6C,  # GURMUKHI DIGIT SIX
    0x0A6D,  # GURMUKHI DIGIT SEVEN
    0x0A6E,  # GURMUKHI DIGIT EIGHT
    0x0A6F,  # GURMUKHI DIGIT NINE
    ]

vowels = list(map(chr, Vowels))
matras = list(map(chr, Matras))
consonants = list(map(chr, Consonants))
n = nukta = list(map(chr, Nukta))[0]
h = virama = list(map(chr, Virama))[0]
digits = list(map(chr, Digits))
