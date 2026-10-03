# Dua ya Kuombea Mvua (Waji Waji)

*Dua ya Kuombea Mvua* (*Waji Waji*), a five-line *shairi* with lines of 6 + 9 syllables, by Sheikh Muhyddin bin Sheikh bin Jahathwan Al-Waily (1798–1870). The recording covers the 14 stanzas, read from Chiraghdin & Nabhany (1987, pp. 45–47).

In the book, these analyses belong to Case Study VI, section 9.6.1, and section 9.6.4 (*The Procrustean Bed*, https://doi.org/10.5281/zenodo.21720211).

## The recording

`4_Dua_ya_Kuombea_Mvua.wav` (6.8 MB, md5 `b1049bc9dd5356a140265d31b7582eb4`) is the formal reading by Fatuma Shaaban that these scripts analyze. It is included here so that the scripts can be run directly in this folder. The reference copy is deposited on Zenodo in *The Fatuma Shaaban Acoustic Corpus* (https://doi.org/10.5281/zenodo.22162387), together with the reading sheet given to the speaker and the description of the reading protocol.

## The scripts

Each script reproduces one figure of the book. The lexical reading is derived from the printed text by the penultimate stress rule; the auditory reading is the screening of the recording by ear. Both are recorded in the header of the script, which then measures the line and draws the figure.

- **`Waji_Waji_Stanza1_Line5_H2.py`**: figure on page 487 of the printed book.
  - Line: *ku-la si-ku li-si-lo-ko-ma   (maximal G against the bipartite axiom (G=4), unmarked)*
  - Lexical reading: 2·2·3·2 | P₁=1, P₂=3, P₃=6, P₄=8 | G-lex = 4
  - Auditory reading: 2·2·3·2 | P₁=1, P₂=3, P₃=6, P₄=8 | G-aud = 4 | delta —
- **`Waji_Waji_Stanza1_Line3_H1.py`**: figure on page 490 of the printed book.
  - Line: *wa-re-he-mu wa-na   (maximal asymmetry against the Grenzschema within a six-syllable hemistich (replaces 1.2 H1, which contained a divine name))*
  - Lexical reading: 4·2 | P₁=3, P₂=5 | G-lex = 2
  - Auditory reading: 4·2 | P₁=3, P₂=5 | G-aud = 2 | delta —
- **`Waji_Waji_Stanza4_Line2_H2.py`**: figure on page 493 of the printed book.
  - Line: *u-fi-sha-o na ku-fu-fu-wa   (random draw)*
  - Lexical reading: 4·5 | P₁=3, P₂=8 | G-lex = 2
  - Auditory reading: 4·5 | P₁=3, P₂=8 | G-aud = 2 | delta —
- **`Waji_Waji_Stanza1_Line4_H2.py`**: figure on page 495 of the printed book.
  - Line: *ha-li ye-tu ka-ti cha-ka   (Grenzschema realized, unmarked)*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta —

## Running a script

From any directory:

```
python 4_Dua_ya_Kuombea_Mvua/Waji_Waji_Stanza1_Line5_H2.py
```

The script finds the recording in its own folder and writes two files next to itself: the figure (PNG, 300 dpi) and its caption (plain text). See the main README for installation and for the method.
