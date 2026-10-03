# Kiswahili!!

*Kiswahili!!* (*shairi* meter), composed in Kiamu by Sheikh Mahmud Ahmed Abdull Kadir (Ustadh Mau) in 2003, and read by the poet himself in Lamu in September–October 2005. The written text he read is reproduced in Appendix A.2 of the book.

In the book, these analyses belong to section 9.3.1 (the method illustrated), Case Study VII, section 9.6.2, and section 9.6.4 (*The Procrustean Bed*, https://doi.org/10.5281/zenodo.21720211).

## The recording

The recording analyzed here is the poet's own reading, deposited on Zenodo: https://zenodo.org/records/19827932. At 29 MB it is not stored in this repository. To run the scripts, download it from Zenodo and save it in this folder under the name `KiswahiliapoemreadbyitsauthorSheikhMahmudAhmedAbdullKadir.wav`. Its md5 checksum, `3cc2da1fb6b45905aa4bbc836ecb599a`, lets you check that you have the same file.

## The scripts

Each script reproduces one figure of the book. The lexical reading is derived from the printed text by the penultimate stress rule; the auditory reading is the screening of the recording by ear. Both are recorded in the header of the script, which then measures the line and draws the figure.

- **`Kiswahili_Stanza3_Line1_H1.py`**: figure on page 315 of the printed book.
  - Line: *mi-mi ma-me-nu si-ta-sa*
  - Lexical reading: 2·3·3 | P₁=1, P₂=4, P₃=7 | G-lex = 3
  - Auditory reading: 2·3·3 | P₁=1, P₂=4, P₃=7 | G-aud = 3 | delta —
- **`Kiswahili_Stanza3_Line1_H2.py`**: figure on page 316 of the printed book.
  - Line: *wa-la si-na pu-ngu-wa-ni*
  - Lexical reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-lex = 3
  - Auditory reading: 2·2·4 | P₁=1, P₂=3, P₃=7 | G-aud = 3 | delta —
- **`Kiswahili_Stanza2_Line4_H1.py`**: figure on page 488 of the printed book.
  - Line: *ko-sa la-ngu ko-sa ga-ni   (maximal G against the bipartite axiom (G=4), the only such hemistich in this corpus)*
  - Lexical reading: 2·2·2·2 | P₁=1, P₂=3, P₃=5, P₄=7 | G-lex = 4
  - Auditory reading: 2?·2·2?·2 | P₁=1?, P₂=3, P₃=5?, P₄=7 | G-aud = 4 | delta —
- **`Kiswahili_Stanza1_Line4_H2.py`**: figure on page 491 of the printed book.
  - Line: *mbo-na mwa-ni-pi-ja zi-tha   (maximal asymmetry against the Grenzschema; the reading reduces a lexical G=3 to G=2)*
  - Lexical reading: 2·4·2 | P₁=1, P₂=5, P₃=7 | G-lex = 3
  - Auditory reading: 2·6 | P₁=1, P₂=7 | G-aud = 2 | delta −P₂=5
- **`Kiswahili_Stanza3_Line3_H1.py`**: figure on page 494 of the printed book.
  - Line: *ni-ze-e wa-na-si-ya-sa   (random draw; the reading adds a nucleus on the compound *wanasiasa*)*
  - Lexical reading: 3·5 | P₁=2, P₂=7 | G-lex = 2
  - Auditory reading: 3·2?·3 | P₁=2, P₂=4?, P₃=7 | G-aud = 3 | delta +P₂=4
- **`Kiswahili_Stanza1_Line1_H1.py`**: figure on page 496 of the printed book.
  - Line: *ku-nya-ma-a ni-me-cho-ka   (Grenzschema realized, unmarked)*
  - Lexical reading: 4·4 | P₁=3, P₂=7 | G-lex = 2
  - Auditory reading: 4·4 | P₁=3, P₂=7 | G-aud = 2 | delta —

## Running a script

From any directory:

```
python 6_Kiswahili/Kiswahili_Stanza3_Line1_H1.py
```

The script finds the recording in its own folder and writes two files next to itself: the figure (PNG, 300 dpi) and its caption (plain text). See the main README for installation and for the method.
