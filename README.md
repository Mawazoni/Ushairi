# Ushairi: acoustic verification scripts for *The Procrustean Bed*

*Ushairi* is the Swahili word for poetry. This repository contains the Python scripts that produce the acoustic figures of the book:

Roy, M. (2026). *The Procrustean Bed: The Fallacy of Accentual Metrics in Swahili Poetry. A Manifesto for Data-Driven Models for the Utenzi, Wimbo, and Shairi Meters*. DL2A Buluu Publishing. ISBN 978-1-291-70670-3. https://doi.org/10.5281/zenodo.21720211

The book tests two accounts of the classical Swahili meters. The first is the account given by the master poets of the Swahili language, who wrote about the rules of their own art: a line is governed by its syllable count (*mizani*) and by its rhyme (*vina*). The second is the account of the accentual school, which holds that the line is organized by a fixed number of stressed beats. Chapter 9 of the book confronts both with a corpus of recordings. Each of the 34 scripts in this repository reproduces one of its figures, line by line, from the recording itself.

## How this repository relates to the other records

This repository is one part of a set of linked deposits, gathered in the Zenodo community *The Procrustean Bed Project: Data-Driven Swahili Poetics*:

- **The book**, which states the questions, gives the analyses and prints the figures: https://doi.org/10.5281/zenodo.21720211 (section 9.2.7 describes all deposits).
- **The Fatuma Shaaban Acoustic Corpus**, the formal readings of the classical poems analyzed in folders 1 to 5, with the reading sheets and the reading protocol: https://doi.org/10.5281/zenodo.22162387
- **The recording of *Kiswahili!!*** read by its author, Sheikh Mahmud Ahmed Abdull Kadir (Ustadh Mau), in Lamu in 2005, analyzed in folder 6: https://zenodo.org/records/19827932
- **The archived copy of this repository**, with a Docker image that preserves the software environment over the long term: https://doi.org/10.5281/zenodo.23089282

The recordings of folders 1 to 5 are also stored here, next to the scripts that analyze them, so that you can work directly in this repository. The Zenodo copies are the reference copies; their checksums are given in each folder's README.

## Contents

```
1_Utenzi_wa_Rasi_Lghuli/   8 scripts   utenzi meter     book section 9.4.1
2_Utendi_wa_Haudaji_V2/    8 scripts   utenzi meter     book section 9.4.2
3_Nyimbo/                  5 scripts   wimbo meter      book section 9.5.4
4_Dua_ya_Kuombea_Mvua/     4 scripts   shairi meter     book sections 9.6.1 and 9.6.4
5_Uwongo/                  3 scripts   shairi meter     book sections 9.6.3 and 9.6.4
6_Kiswahili/               6 scripts   shairi meter     book sections 9.3.1, 9.6.2 and 9.6.4
```

Each folder is named after the recording it contains, without its extension, and has its own README. That README describes the poem and its source edition, and lists for each script the line it measures, its lexical and auditory readings, and the page of the printed book where its figure appears.

## Installation

The scripts need Python 3 and three libraries:

```
pip install -r requirements.txt
```

The libraries are `praat-parselmouth`, which gives Python access to the acoustic engine of Praat, together with `numpy` and `matplotlib`. The exact versions are preserved in the Docker image of the Zenodo archive.

## Running a script

```
python 1_Utenzi_wa_Rasi_Lghuli/Utenzi_wa_Rasi_Lghuli_Stanza28_Line4.py
```

A script can be run from any directory: it looks for its recording in its own folder. It writes two files next to itself, the figure (PNG, 300 dpi) and its caption (plain text), and prints their names. The scripts read the recordings under the exact file names they have in this repository, so the names must not be changed.

For folder 6, the recording is not stored here because of its size (29 MB). Download it from https://zenodo.org/records/19827932 and save it in `6_Kiswahili/` under the name given in that folder's README.

## What each script does

Each script contains, in its header, the line it measures and two readings established before any measurement:

- the **lexical reading**, derived from the printed text by the penultimate stress rule of Swahili, which needs no recording;
- the **auditory reading**, the screening of the recording by ear.

The script then measures the line in the recording. This instrumental reading is reported for information. In the book, no statistic rests on it, and it never overrides the auditory reading.

The method, documented in the header of every script, is the same for all lines:

- **Speaker-derived F0 range.** A first pass tracks the whole recording with a wide range. The tenth and ninetieth percentiles of the voiced frames then define the range used for measurement (floor = 0.75 × q10, ceiling = 1.5 × q90), so that the range is not set by hand.
- **Semitone scale.** F0 is converted to semitones relative to the speaker's median over the whole recording, so that the lines of a recording share one scale.
- **Declination.** A linear trend is fitted to the voiced frames of the line and subtracted, so that a prominence late in the line is not penalized relative to an early one.
- **Prominence by mean.** The prominence of a syllable is the mean of the detrended contour over that syllable, not its maximum: a single frame at a voicing onset must not create an accent.
- **Peak latency.** The time of the maximum within each syllable is reported, since melodic peaks often fall after the onset of the syllable that carries the prominence.
- **Instrumental reading.** A syllable counts as instrumentally prominent when its detrended F0 mean is a local maximum across the syllables of the line and lies above the declination. The criterion uses no information from the lexical or auditory readings.
- **Edge positions.** The first and last syllables are flagged and excluded from durational comparison, because the segmentation of the onset, final lengthening and the boundary tone affect their durations.
- **Signal conditioning.** A three-point median filter is applied within voiced runs, and voiced runs shorter than 40 ms are discarded, uniformly for every line.

The syllable boundaries written in each script were placed by the researcher in Praat, by ear and by eye; nothing in the segmentation is automated. One script, `Utendi_wa_Haudaji_Stanza20_Line4.py`, documents in its header the exclusion of a false start by the reader.

## Reading the figures

Green: intensity. Blue: F0 in semitones relative to the speaker median, measured once over the whole recitation so that all figures of a recitation share one scale. Dotted blue: the declination internal to the line, removed before measurement. Red triangles mark the accentual nuclei established by ear; a question mark above a triangle marks a nucleus heard but judged weak. Open circles mark the measured F0 peak of each annotated nucleus, with its latency from the syllable onset. Durations are in milliseconds; a dagger marks the first and last syllables, excluded from durational comparison.

## Licenses

- The **code** in this repository is released under the MIT License (see `LICENSE.md`).
- The **documentation** and the **figures** the scripts produce are released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
- The **recordings** are released under CC BY 4.0, as stated on their Zenodo records.

## How to cite

Please cite the book, and this software archive if you use the scripts:

Roy, M. (2026). *The Procrustean Bed: The Fallacy of Accentual Metrics in Swahili Poetry. A Manifesto for Data-Driven Models for the Utenzi, Wimbo, and Shairi Meters*. DL2A Buluu Publishing. https://doi.org/10.5281/zenodo.21720211

Roy, M. (2026). *Ushairi: Acoustic verification scripts for The Procrustean Bed* [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23089282

## Author

Mathieu Roy (Mawazoni), DL2A Buluu Publishing. ORCID: https://orcid.org/0000-0001-7684-4355
