# Running Ushairi with Docker

The Docker image fixes the software environment of the scripts, so that they can still be run when the versions below are no longer current:

- Python 3.12
- praat-parselmouth 0.4.7, which embeds Praat 6.1.38
- numpy 2.5.3
- matplotlib 3.11.2

With these versions, all 34 scripts reproduce the figures of the book: the speaker median and the declination slope printed under each figure were obtained again, identically, for all 34 figures (check run of 3 October 2026).

## 1. Get the image

**From the archive.** Download `Ushairi-1.0.0-docker-image.tar.gz` from the Zenodo record https://doi.org/10.5281/zenodo.23089282, then load it:

```
docker load -i Ushairi-1.0.0-docker-image.tar.gz
```

**Or rebuild it** from the root of this repository:

```
docker build -t ushairi:1.0.0 .
```

## 2. Run one script

From the root of the repository, so that the figures are written into your own folders:

```
docker run --rm -v "$PWD":/ushairi ushairi:1.0.0 python 1_Utenzi_wa_Rasi_Lghuli/Utenzi_wa_Rasi_Lghuli_Stanza28_Line4.py
```

The option `-v "$PWD":/ushairi` makes your folder visible inside the container: the script reads the recording from it and writes the figure and its caption into it.

## 3. Run all the scripts

```
docker run --rm -v "$PWD":/ushairi ushairi:1.0.0 bash -c 'for f in */*.py; do python "$f"; done'
```

The scripts of folder 6 need the recording of *Kiswahili!!*, to be downloaded from Zenodo as explained in `6_Kiswahili/README.md`. Without it, these six scripts stop with an error and the others run normally.

## Without your own copy of the repository

The image also contains version 1.0.0 of the repository, with the recordings of folders 1 to 5. To work inside it:

```
docker run --rm -it ushairi:1.0.0
```

This opens a shell in `/ushairi`. Figures produced there disappear when the container is closed, unless you copy them out with `docker cp`.

## Platform

The archived image is built for `linux/amd64`, the most common platform. On a computer with an ARM processor, such as a recent Mac, Docker runs it through emulation: add `--platform linux/amd64` after `docker run`. Rebuilding the image with `docker build` produces a native image for your machine.

On Windows, in PowerShell, write `${PWD}` instead of `$PWD`.
