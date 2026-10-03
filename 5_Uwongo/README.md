# Uwongo

*Uwongo* (*shairi* meter, *mashairi ya vidato*: stanzas chained like the rungs of a ladder), by Muyaka bin Haji al-Ghassaniy (1776–1840). The recording covers the 4 stanzas, read from Hichens (1940, pp. 92–93).

In the book, these analyses belong to Case Study VIII, section 9.6.3, and section 9.6.4 (*The Procrustean Bed*, https://doi.org/10.5281/zenodo.21720211).

## The recording

`5_Uwongo.wav` (1.8 MB, md5 `c336b5373b74b64e744ff569555ed186`) is the formal reading by Fatuma Shaaban that these scripts analyze. It is included here so that the scripts can be run directly in this folder. The reference copy is deposited on Zenodo in *The Fatuma Shaaban Acoustic Corpus* (https://doi.org/10.5281/zenodo.22162387), together with the reading sheet given to the speaker and the description of the reading protocol.

## The scripts

Each script reproduces one figure of the book. The lexical reading is derived from the printed text by the penultimate stress rule; the auditory reading is the screening of the recording by ear. Both are recorded in the header of the script, which then measures the line and draws the figure.

- **`Uwongo_Stanza1_Line3_H2.py`**: figure on page 489 of the printed book.
  - Line: *ku-lla ja-mbo kwa ndi-a-ye   (maximal G available in this corpus (G=3), unmarked)*
  - Lexical reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-lex = 3
  - Auditory reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-aud = 3 | delta —
- **`Uwongo_Stanza1_Line1_H2.py`**: figure on page 492 of the printed book.
  - Line: *le-o u-ni-tu-mi-ki-ye   (maximal asymmetry against the Grenzschema, unmarked)*
  - Lexical reading: 2·6 | P₁=1, P₂=7 | G-lex = 2
  - Auditory reading: 2·6 | P₁=1, P₂=7 | G-aud = 2 | delta —
- **`Uwongo_Stanza1_Line1_H1.py`**: figure on page 497 of the printed book.
  - Line: *ka-ra-ta-si na-ku-tu-ma   (Grenzschema realized, unmarked)*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta —

## Running a script

From any directory:

```
python 5_Uwongo/Uwongo_Stanza1_Line3_H2.py
```

The script finds the recording in its own folder and writes two files next to itself: the figure (PNG, 300 dpi) and its caption (plain text). See the main README for installation and for the method.
