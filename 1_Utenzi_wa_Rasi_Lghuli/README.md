# Utenzi wa Rasi 'lGhuli

*Utenzi wa Rasi 'lGhuli* (*utenzi* meter), composed by Mwalimu Mgeni bin Faqihi in Bagamoyo, c. 1850. The recording covers the first 40 stanzas, read from Mgeni bin Faqihi (1979, pp. 1–2).

In the book, these analyses belong to Case Study I, section 9.4.1 (*The Procrustean Bed*, https://doi.org/10.5281/zenodo.21720211).

## The recording

`1_Utenzi_wa_Rasi_Lghuli.wav` (9.9 MB, md5 `c0c16495dfa1d9036a23403816e2fd16`) is the formal reading by Fatuma Shaaban that these scripts analyze. It is included here so that the scripts can be run directly in this folder. The reference copy is deposited on Zenodo in *The Fatuma Shaaban Acoustic Corpus* (https://doi.org/10.5281/zenodo.22162387), together with the reading sheet given to the speaker and the description of the reading protocol.

## The scripts

Each script reproduces one figure of the book. The lexical reading is derived from the printed text by the penultimate stress rule; the auditory reading is the screening of the recording by ear. Both are recorded in the header of the script, which then measures the line and draws the figure.

- **`Utenzi_wa_Rasi_Lghuli_Stanza31_Line1.py`**: figure on page 351 of the printed book.
  - Line: *na-che-le-a ni m-ji-nga*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta —
- **`Utenzi_wa_Rasi_Lghuli_Stanza28_Line4.py`**: figure on page 352 of the printed book.
  - Line: *ku-tu-nga kwa u-sha-i-ri*
  - Lexical reading: 3·5 | P₁=2, P₂=7 | G-lex 2
  - Auditory reading: 3·5 | P₁=2, P₂=7 | G-aud 2 | delta —
- **`Utenzi_wa_Rasi_Lghuli_Stanza31_Line4.py`**: figure on page 353 of the printed book.
  - Line: *ya-ta-ka m-tu ma-hi-ri*
  - Lexical reading: 3·2·3 | P₁=2, P₂=4, P₃=7 | G-lex = 3
  - Auditory reading: 3·2·3 | P₁=2, P₂=4?, P₃=7 | G-aud = 3 | delta -
- **`Utenzi_wa_Rasi_Lghuli_Stanza32_Line1.py`**: figure on page 354 of the printed book.
  - Line: *wa-la mi si mu-a-li-mu*
  - Lexical reading: 2·6 | P₁=1, P₂=7 | G-lex = 2
  - Auditory reading: 3·1·4 | P₁=2, P₂=4, P₃=7 | G-aud = 3 | delta −P₁=1, +P₁=2, +P₂=4
- **`Utenzi_wa_Rasi_Lghuli_Stanza12_Line4.py`**: figure on page 355 of the printed book.
  - Line: *hi-yo si-ku ya nu-shu-ri*
  - Lexical reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-lex = 3
  - Auditory reading: 2·2·4 | P₁=1?, P₂=3, P₃=7 | G-aud = 3 | delta —
- **`Utenzi_wa_Rasi_Lghuli_Stanza29_Line4.py`**: figure on page 356 of the printed book.
  - Line: *wa-ju-a-o taf-si-ri*
  - Lexical reading: 4·3 | P₁=3, P₂=6 | G-lex = 2
  - Auditory reading: 4·3 | P₁=3, P₂=6 | G-aud = 2 | delta —
- **`Utenzi_wa_Rasi_Lghuli_Stanza7_Line4.py`**: figure on page 357 of the printed book.
  - Line: *wa-ku-u ha-ta sa-ghi-ri*
  - Lexical reading: 3·2·3 | P₁=2, P₂=4, P₃=7 | G-lex = 3
  - Auditory reading: 3·2·3 | P₁=2, P₂=4?, P₃=7 | G-aud = 3 | delta —
- **`Utenzi_wa_Rasi_Lghuli_Stanza22_Line3.py`**: figure on page 358 of the printed book.
  - Line: *u-sa-fi ha-ta u-ju-e*
  - Lexical reading: 3·2·3 | P₁=2, P₂=4, P₃=7 | G-lex = 3
  - Auditory reading: 3·5 | P₁=2, P₂=7 | G-aud = 2 | delta −P₂=4

## Running a script

From any directory:

```
python 1_Utenzi_wa_Rasi_Lghuli/Utenzi_wa_Rasi_Lghuli_Stanza31_Line1.py
```

The script finds the recording in its own folder and writes two files next to itself: the figure (PNG, 300 dpi) and its caption (plain text). See the main README for installation and for the method.
