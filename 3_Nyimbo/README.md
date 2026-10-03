# Nyimbo (wimbo meter)

Three texts in the *wimbo* meter, read in a single recording: *Wimbo wa Miti*, by an anonymous woman poet, Lamu, c. 1800–1850 (Mbele, 1996); *Sina Hali*, example b of the *wimbo* in Shariff (1988); and *Kukwepuka nana*, by Sheikh Ahmed Sheikh Nabhany (1927–2017), example k in Shariff (1988), whose lines are divided into four unequal segments (6 + 3 + 4 + 2 syllables). The scripts named `Hyperfractionated_Wimbo` analyze *Kukwepuka nana*.

In the book, these analyses belong to section 9.5.4, Instrumental Verification of the Hostile Sample (Case Studies III to V) (*The Procrustean Bed*, https://doi.org/10.5281/zenodo.21720211).

## The recording

`3_Nyimbo.wav` (3.1 MB, md5 `68a0fa774d173f49b61f16e6cafcbb8c`) is the formal reading by Fatuma Shaaban that these scripts analyze. It is included here so that the scripts can be run directly in this folder. The reference copy is deposited on Zenodo in *The Fatuma Shaaban Acoustic Corpus* (https://doi.org/10.5281/zenodo.22162387), together with the reading sheet given to the speaker and the description of the reading protocol.

## The scripts

Each script reproduces one figure of the book. The lexical reading is derived from the printed text by the penultimate stress rule; the auditory reading is the screening of the recording by ear. Both are recorded in the header of the script, which then measures the line and draws the figure.

- **`Wimbo_wa_Miti_Stanza8_Line2_H2.py`**: figure on page 438 of the printed book.
  - Line: *ni-me-zi-ye ku-ta-mbu-wa   (Grenzschema realized)*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta —
- **`Wimbo_wa_Miti_Stanza6_Line1_H2.py`**: figure on page 439 of the printed book.
  - Line: *ha-tu-chi twa-po u-wa-wa   (dominant lexical sequence 3·2·3)*
  - Lexical reading: 3·2·3 | P₁=2, P₂=4, P₃=7 | G-lex = 3
  - Auditory reading: 3·2·3 | P₁=2, P₂=4, P₃=7 | G-aud = 3 | delta —
- **`Wimbo_wa_Miti_Stanza5_Line1_H2.py`**: figure on page 440 of the printed book.
  - Line: *wa-si-ye-sa ka-ni za-o   (reading creates a Grenzschema the lexicon does not supply)*
  - Lexical reading: 4·2·2 | P₁=3, P₂=5, P₃=7 | G-lex = 3
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta −P₂=5
- **`Wimbo_wa_Miti_Stanza2_Line3_H2.py`**: figure on page 441 of the printed book.
  - Line: *ku-nya-ma-a ni u-ju-ra   (both nuclei marked weakly realized)*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4?·4? | P₁=3?, P₂=7? | G-aud = 2 | delta —
- **`Hyperfractionated_Wimbo_Stanza1_Line2_H1.py`**: figure on page 442 of the printed book.
  - Line: *Ku-su-bi-ri te-na   (six-syllable segment: no tetrasyllabic partition available)*
  - Lexical reading: 4·2 | P₁=3, P₂=5 | G-lex = 2
  - Auditory reading: 4·2 | P₁=3, P₂=5 | G-aud = 2 | delta —

## Running a script

From any directory:

```
python 3_Nyimbo/Wimbo_wa_Miti_Stanza8_Line2_H2.py
```

The script finds the recording in its own folder and writes two files next to itself: the figure (PNG, 300 dpi) and its caption (plain text). See the main README for installation and for the method.
