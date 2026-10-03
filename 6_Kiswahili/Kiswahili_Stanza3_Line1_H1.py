#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Swahili Formal Metrics — acoustic verification tool
Kiswahili!!, Stanza 3, Line 1, H1

Line      : mi-mi ma-me-nu si-ta-sa
Lexical   : 2·3·3 | P₁=1, P₂=4, P₃=7 | G-lex = 3
Auditory  : 2·3·3 | P₁=1, P₂=4, P₃=7 | G-aud = 3 | delta —

The script measures fundamental frequency, intensity and syllable duration
for one line of the recitation and produces a figure and a caption.

Method
------
Speaker-derived F0 range. Pass 1 tracks the whole recording with a wide
range; the tenth and ninetieth percentiles of the voiced frames define the
range used for measurement (floor = 0.75 * q10, ceiling = 1.5 * q90). The
range is therefore not set by hand.

Semitone scale. F0 is converted to semitones relative to the speaker median
over the whole recording, so that measurements from different lines are
directly comparable.

Declination. A linear trend is fitted to the voiced frames of the line and
subtracted, so that a prominence late in the line is not penalised relative
to an early one.

Prominence by mean. The prominence of a syllable is the mean of the
detrended contour over that syllable, not its maximum: a single frame at a
voicing onset must not create an accent.

Peak latency. The time of the maximum within each syllable is reported.
Melodic peaks are commonly realised after the onset of the syllable that
carries the prominence, and may fall inside the following syllable.

Instrumental reading. A syllable counts as instrumentally prominent when
its detrended F0 mean is a local maximum across the syllables of the line and
lies above the declination. The criterion uses no information from the lexical
structure or from the auditory annotation, and may designate a syllable that
neither predicts.

Edge positions. The first and last syllables are flagged: their durations
are affected by the segmentation of the line onset, by final lengthening
and by the boundary tone, and they are excluded from durational comparison.

Signal conditioning. A three-point median filter is applied within voiced
runs, and voiced runs shorter than 40 ms are discarded. Both operations
target isolated frames produced at obstruent releases and are applied
uniformly to every line.

Requires: praat-parselmouth, numpy, matplotlib.
"""

import os
import numpy as np
import parselmouth
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.patches import Rectangle

# --------------------------------------------------------------------------
# 1. Input
# --------------------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
audio_file_name = "KiswahiliapoemreadbyitsauthorSheikhMahmudAhmedAbdullKadir.wav"
audio_file = os.path.join(script_dir, audio_file_name)

stanza_number = 3
line_number = 1
line_text = "mi-mi ma-me-nu si-ta-sa"

# Accentual analysis of this line, from the mapping of section 9.4.2 §4.
lexical_chain = "2·3·3"
lexical_positions = [1, 4, 7]
g_lex = 3
auditory_chain = "2·3·3"
auditory_positions = [1, 4, 7]
uncertain_positions = []
g_aud = 3
lexical_display = "P₁=1, P₂=4, P₃=7"
auditory_display = "P₁=1, P₂=4, P₃=7"
delta = "—"

# Line boundaries in the recording, in seconds. A value of 0 means the
# boundary has not yet been established.
start_time = 41.63
end_time = 43.85

# Syllable onsets, in seconds, in the order of the verse. A value of 0 means
# the onset has not yet been established.
syllables = [
    ("mi", 41.69),
    ("mi", 41.97),
    ("ma", 42.27),
    ("me", 42.44),
    ("nu", 42.74),
    ("si", 42.99),
    ("ta", 43.25),
    ("sa", 43.63)
]

# --------------------------------------------------------------------------
# 2. Speaker calibration (pass 1)
# --------------------------------------------------------------------------
snd = parselmouth.Sound(audio_file)
wide = snd.to_pitch_ac(pitch_floor=60.0, pitch_ceiling=600.0)
voiced = wide.selected_array["frequency"]
voiced = voiced[voiced > 0]
q10, speaker_median, q90 = np.percentile(voiced, [10, 50, 90])
floor, ceiling = max(50.0, 0.75 * q10), 1.5 * q90

# --------------------------------------------------------------------------
# 3. Measurement (pass 2)
# --------------------------------------------------------------------------
margin = 0.15
part = snd.extract_part(from_time=max(0.0, start_time - margin),
                        to_time=end_time + margin, preserve_times=True)
pitch = part.to_pitch_ac(pitch_floor=floor, pitch_ceiling=ceiling,
                         voicing_threshold=0.35, octave_jump_cost=0.35,
                         very_accurate=False)
times, freq = pitch.xs(), pitch.selected_array["frequency"].copy()

# three-point median filter inside voiced runs
smoothed = freq.copy()
for i in range(1, len(freq) - 1):
    if freq[i - 1] > 0 and freq[i] > 0 and freq[i + 1] > 0:
        smoothed[i] = np.median(freq[i - 1:i + 2])
freq = smoothed

# removal of voiced runs shorter than 40 ms
step = times[1] - times[0]
minimum_run = int(round(0.040 / step))
i = 0
while i < len(freq):
    if freq[i] > 0:
        j = i
        while j < len(freq) and freq[j] > 0:
            j += 1
        if j - i < minimum_run:
            freq[i:j] = 0.0
        i = j
    else:
        i += 1

intensity = part.to_intensity(minimum_pitch=floor)
int_times, int_values = intensity.xs(), intensity.values[0]

inside = (times >= start_time) & (times <= end_time) & (freq > 0)
x = times[inside]
y = 12 * np.log2(freq[inside] / speaker_median)
slope, intercept = np.polyfit(x, y, 1)

measures = []
for index, (label, onset) in enumerate(syllables):
    offset = syllables[index + 1][1] if index + 1 < len(syllables) else end_time
    window = (x >= onset) & (x < offset)
    iwindow = (int_times >= onset) & (int_times < offset)
    if window.sum():
        detrended = y[window] - (slope * x[window] + intercept)
        peak_time = x[window][int(np.argmax(detrended))]
        f0_mean = detrended.mean()
        latency = 1000.0 * (peak_time - onset)
    else:
        f0_mean, peak_time, latency = np.nan, np.nan, np.nan
    measures.append(dict(
        position=index + 1, label=label, onset=onset, offset=offset,
        duration_ms=1000.0 * (offset - onset),
        reliable=0 < index < len(syllables) - 1,
        f0_mean_detrended=f0_mean, peak_time=peak_time, latency_ms=latency,
        intensity_mean=int_values[iwindow].mean() if iwindow.sum() else np.nan,
        intensity_max=int_values[iwindow].max() if iwindow.sum() else np.nan))

# --------------------------------------------------------------------------
# 3b. Instrumental reading
# --------------------------------------------------------------------------
# The instrumental reading is established without reference to the lexical
# structure or to the auditory annotation. A syllable counts as
# instrumentally prominent when its detrended F0 mean is a local maximum
# across the syllables of the line and lies above the declination. The
# criterion is applied identically to every line, and it is free to confirm a
# nucleus the lexicon predicts, to leave one unconfirmed, or to designate a
# syllable the lexicon does not predict at all.
values = [m["f0_mean_detrended"] for m in measures]
instrumental_positions = []
for i, v in enumerate(values):
    if np.isnan(v) or v <= 0:
        continue
    left = values[i - 1] if i > 0 else -np.inf
    right = values[i + 1] if i + 1 < len(values) else -np.inf
    if v >= left and v >= right:
        instrumental_positions.append(i + 1)
if not instrumental_positions:
    instrumental_positions = [int(np.nanargmax(values)) + 1]
g_inst = len(instrumental_positions)

# The sequence of nucleus volumes follows from the positions: a nucleus ends
# one syllable after the syllable that carries its stress, and the last
# nucleus closes the line.
_ends = [p + 1 for p in instrumental_positions]
_ends[-1] = len(syllables)
instrumental_chain_list, _previous = [], 0
for _end in _ends:
    instrumental_chain_list.append(_end - _previous)
    _previous = _end
instrumental_chain = "\u00b7".join(str(v) for v in instrumental_chain_list)

_subscripts = {1: "\u2081", 2: "\u2082", 3: "\u2083", 4: "\u2084",
               5: "\u2085", 6: "\u2086", 7: "\u2087", 8: "\u2088"}
instrumental_display = ", ".join(
    "P%s=%d" % (_subscripts[i + 1], p) for i, p in enumerate(instrumental_positions))

# Delta of the instrumental reading is taken against the lexical structure.
_delta_inst = []
for i, p in enumerate(lexical_positions):
    if p not in instrumental_positions:
        _delta_inst.append("\u2212P%s=%d" % (_subscripts[i + 1], p))
for i, p in enumerate(instrumental_positions):
    if p not in lexical_positions:
        _delta_inst.append("+P%s=%d" % (_subscripts[i + 1], p))
delta_instrumental = ", ".join(_delta_inst) if _delta_inst else "\u2014"

convergent = sorted(instrumental_positions) == sorted(auditory_positions)

# --------------------------------------------------------------------------
# 4. Figure
# --------------------------------------------------------------------------
figure = plt.figure(figsize=(11.5, 5.6))
grid = figure.add_gridspec(2, 1, height_ratios=[1, 6.5], hspace=0.05)
strip = figure.add_subplot(grid[0])
axis = figure.add_subplot(grid[1], sharex=strip)
strip.set_ylim(0, 1)
strip.axis("off")

plot_start, plot_end = max(0.0, start_time - margin), end_time + margin
for a, b in ((plot_start, start_time), (end_time, plot_end)):
    if b > a:
        axis.add_patch(Rectangle((a, 0), b - a, 100, facecolor="0.92",
                                 hatch="///", edgecolor="0.8", linewidth=0,
                                 zorder=0))

axis.plot(part.xs(), part.values[0, :] * 40 + 50, color="gray", alpha=0.28, zorder=1)
axis.plot(int_times, int_values, color="green", linewidth=2, zorder=3)
axis.set_ylabel("Intensity (dB)", color="green")
axis.set_ylim(0, 100)

twin = axis.twinx()
plotted = freq.astype(float).copy()
plotted[plotted == 0] = np.nan
semitones = 12 * np.log2(plotted / speaker_median)
twin.plot(times, semitones, color="blue", linewidth=2.6, zorder=4)
low, high = np.nanmin(semitones), np.nanmax(semitones)
twin.set_ylim(low - 1.0, high + 1.0)
twin.set_ylabel("F0 (st re %.0f Hz)" % speaker_median, color="blue")
trend_x = np.linspace(start_time, end_time, 200)
trend_y = slope * trend_x + intercept
visible = (trend_y >= low - 1.0) & (trend_y <= high + 1.0)
twin.plot(trend_x[visible], trend_y[visible], color="blue", linestyle=":",
          linewidth=1.6, alpha=0.85, zorder=4)

axis.xaxis.set_major_locator(MultipleLocator(0.5))
axis.xaxis.set_minor_locator(MultipleLocator(0.1))
axis.grid(which="major", axis="x", linestyle="-", color="gray", alpha=0.3)
axis.grid(which="minor", axis="x", linestyle=":", color="lightgray", alpha=0.7)

for m in measures:
    axis.axvline(x=m["onset"], color="black", linestyle="--", alpha=0.55, zorder=2)
    annotated = m["position"] in auditory_positions
    mid = (m["onset"] + m["offset"]) / 2
    axis.text(mid, 10, m["label"], fontsize=11.5, ha="center",
              fontweight="bold" if annotated else "normal",
              color="darkred" if annotated else "black")
    duration = str(int(m["duration_ms"])) + ("" if m["reliable"] else "\u2020")
    axis.text(mid, 3, duration, fontsize=8.5, ha="center",
              color="purple" if m["reliable"] else "0.55")
    if annotated:
        marker = "v"
        strip.plot([mid], [0.62], marker=marker, markersize=10,
                   color="darkred", clip_on=False)
        if m["position"] in uncertain_positions:
            strip.text(mid, 0.78, "?", fontsize=10, color="darkred", ha="center")
        if not np.isnan(m["peak_time"]):
            value = float(np.interp(m["peak_time"], times, semitones))
            if not np.isnan(value):
                twin.plot([m["peak_time"]], [value], marker="o", markersize=8,
                          markerfacecolor="none", markeredgecolor="darkblue",
                          markeredgewidth=2, zorder=7)
            if m["latency_ms"] > 40:
                strip.annotate("", xy=(m["peak_time"], 0.30), xytext=(m["onset"], 0.30),
                               arrowprops=dict(arrowstyle="->", color="darkblue", lw=1.3))
                strip.text((m["onset"] + m["peak_time"]) / 2, 0.02,
                           "+%d ms" % int(m["latency_ms"]), fontsize=8,
                           color="darkblue", ha="center")

strip.text(0.5, 1.30,
           "annotated nuclei: %s   G-aud = %d\n"
           "instrumentally confirmed: %s   G-inst = %d   \u2192 %s   |   "
           "declination %+.1f st/s   |   durations in ms, \u2020 = edge position"
           % (auditory_positions, g_aud, instrumental_positions, g_inst,
              "CONVERGENT" if convergent else "DIVERGENT", slope),
           transform=strip.transAxes, fontsize=8.2, va="bottom", ha="center",
           family="monospace", linespacing=1.5)

figure.suptitle("Stanza %d, Line %d: %s" % (stanza_number, line_number, line_text),
                fontsize=12.5, y=0.985)
axis.set_xlim(plot_start, plot_end)
plt.setp(strip.get_xticklabels(), visible=False)
figure.subplots_adjust(left=0.075, right=0.925, top=0.80, bottom=0.085)

base = os.path.splitext(audio_file_name)[0]
image_path = os.path.join(script_dir, "%s_Stanza%d_Line%d_H1.png" % (base, stanza_number, line_number))
caption_path = os.path.join(script_dir, "%s_Stanza%d_Line%d_H1_caption.txt" % (base, stanza_number, line_number))
figure.savefig(image_path, dpi=300)
plt.close(figure)

# --------------------------------------------------------------------------
# 5. Caption
# --------------------------------------------------------------------------
if convergent:
    verdict = ("The syllables the instrument designates as prominent are exactly "
               "those annotated by ear: the two readings agree on the accentual "
               "structure of this line.")
else:
    heard_only = [p for p in auditory_positions if p not in instrumental_positions]
    measured_only = [p for p in instrumental_positions if p not in auditory_positions]
    parts = []
    if heard_only:
        parts.append("position(s) %s annotated by ear are not designated by the "
                     "instrument, their detrended F0 mean being either below the "
                     "declination or lower than that of an adjacent syllable"
                     % heard_only)
    if measured_only:
        parts.append("position(s) %s are designated by the instrument without "
                     "having been annotated by ear" % measured_only)
    verdict = ("The instrumental reading diverges from the auditory reading: %s. "
               "The divergence is recorded and the annotation is not revised, in "
               "accordance with the rule of non-revision stated in section 9.2.3. "
               "Fundamental frequency is one of three parameters and is not decisive "
               "on its own; the durations and intensities given below are reported "
               "whether or not they agree with it.")
    verdict = verdict % "; and ".join(parts)

lines = []
lines.append("Kiswahili!!, Stanza %d, Line %d, H1: \"%s\"" % (stanza_number, line_number, line_text))
lines.append("Lexical reading: %s, %s, G-lex = %d." % (lexical_chain, lexical_display, g_lex))
lines.append("Auditory reading: %s, %s, G-aud = %d, delta %s." % (auditory_chain, auditory_display, g_aud, delta))
lines.append("Instrumental reading: %s, %s, G-inst = %d, delta %s (against the lexical reading)."
             % (instrumental_chain, instrumental_display, g_inst, delta_instrumental))
lines.append("")
lines.append("Green: intensity. Blue: F0 in semitones relative to the speaker median "
             "(%.0f Hz), measured once over the whole recitation so that all figures "
             "share one scale. Dotted blue: the declination internal to the line "
             "(%+.2f st/s), removed before measurement. Red triangles mark the "
             "accentual nuclei established by ear; a question mark above a triangle "
             "marks a nucleus heard but judged weak. Open circles mark the measured "
             "F0 peak of each annotated nucleus, with its latency from the syllable "
             "onset. Durations are in milliseconds; a dagger marks the first and last "
             "syllables, excluded from durational comparison." % (speaker_median, slope))
lines.append("")
lines.append(verdict)
lines.append("")
lines.append("Per-syllable measurements:")
for m in measures:
    lines.append("  %d %-4s  %4d ms%s  F0 %+5.2f st  peak +%3d ms  intensity %5.1f dB"
                 % (m["position"], m["label"], int(m["duration_ms"]),
                    " " if m["reliable"] else "\u2020",
                    m["f0_mean_detrended"], int(m["latency_ms"]), m["intensity_mean"]))

with open(caption_path, "w", encoding="utf-8") as handle:
    handle.write("\n".join(lines) + "\n")

print(os.path.basename(image_path))
print(os.path.basename(caption_path))
