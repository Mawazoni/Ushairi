# Utendi wa Haudaji

*Utendi wa Haudaji* (*utenzi* meter), by an unknown author, Lamu, 19th century: the text on which the accentual theory of the *Grenzschema* (an ideal two-stress template) was built. The recording covers the first 40 stanzas, read from Vierke (2011, pp. 479–489), whose analytical transcription was simplified for reading (see the Zenodo record of the corpus).

In the book, these analyses belong to Case Study II, section 9.4.2 (*The Procrustean Bed*, https://doi.org/10.5281/zenodo.21720211).

## The recording

`2_Utendi_wa_Haudaji_V2.wav` (8.5 MB, md5 `12ca70cc075f17408cff2fc1f0f1143f`) is the formal reading by Fatuma Shaaban that these scripts analyze. It is included here so that the scripts can be run directly in this folder. The reference copy is deposited on Zenodo in *The Fatuma Shaaban Acoustic Corpus* (https://doi.org/10.5281/zenodo.22162387), together with the reading sheet given to the speaker and the description of the reading protocol.

## The scripts

Each script reproduces one figure of the book. The lexical reading is derived from the printed text by the penultimate stress rule; the auditory reading is the screening of the recording by ear. Both are recorded in the header of the script, which then measures the line and draws the figure.

- **`Utendi_wa_Haudaji_Stanza37_Line2.py`**: figure on page 393 of the printed book.
  - Line: *na-po-ze-wa ni a-zi-zi*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta —
- **`Utendi_wa_Haudaji_Stanza21_Line3.py`**: figure on page 394 of the printed book.
  - Line: *m-no ni-me-wa-ta-ma-ni*
  - Lexical reading: 2·6 | P₁=1, P₂=7 | G-lex = 2
  - Auditory reading: 2·6 | P₁=1, P₂=7 | G-aud = 2 | delta —
- **`Utendi_wa_Haudaji_Stanza37_Line3.py`**: figure on page 395 of the printed book.
  - Line: *ku-wa mi-mi mu-o-mbe-zi*
  - Lexical reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-lex = 3
  - Auditory reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-aud = 3 | delta —
- **`Utendi_wa_Haudaji_Stanza32_Line4.py`**: figure on page 396 of the printed book.
  - Line: *ku-la ya-mbo mo-ya-mo-ya*
  - Lexical reading: 2·2·2·2 | P₁=1, P₂=3, P₃=5, P₄=7 | G-lex = 4
  - Auditory reading: 2·2·2·2 | P₁=1, P₂=3, P₃=5, P₄=7 | G-aud = 4 | delta —
- **`Utendi_wa_Haudaji_Stanza9_Line4.py`**: figure on page 397 of the printed book.
  - Line: *ya-si-yo-m-ti-ndi-ki-a*
  - Lexical reading: 8 | P₁=7 | G-lex = 1
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta +P₁=3
- **`Utendi_wa_Haudaji_Stanza22_Line1.py`**: figure on page 398 of the printed book.
  - Line: *u-si-ku si-la-li te-na*
  - Lexical reading: 3·3·2 | P₁=2, P₂=5, P₃=7 | G-lex = 3
  - Auditory reading: 3·3·2 | P₁=2, P₂=5, P₃=7 | G-aud = 3 | delta —
- **`Utendi_wa_Haudaji_Stanza5_Line3.py`**: figure on page 399 of the printed book.
  - Line: *ni za-ke ye-ye a-zi-zi*
  - Lexical reading: 3·2·3 | P₁=2, P₂=4, P₃=7 | G-lex = 3
  - Auditory reading: 3·5 | P₁=2, P₂=7 | G-aud = 2 | delta −P₂=4
- **`Utendi_wa_Haudaji_Stanza20_Line4.py`**: figure on page 400 of the printed book.
  - Line: *si-che ku-ni-ka-ri-fi-a*
  - Lexical reading: 2·6 | P₁=1, P₂=7 | G-lex = 2
  - Auditory reading: 2·6 | P₁=1, P₂=7 | G-aud = 2 | delta —

## Running a script

From any directory:

```
python 2_Utendi_wa_Haudaji_V2/Utendi_wa_Haudaji_Stanza37_Line2.py
```

The script finds the recording in its own folder and writes two files next to itself: the figure (PNG, 300 dpi) and its caption (plain text). See the main README for installation and for the method.
