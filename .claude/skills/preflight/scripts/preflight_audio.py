"""Render a preflight dialogue to MP3 with local Piper voices, so no text leaves the machine."""

import argparse
import json
import re
import subprocess
import tempfile
from pathlib import Path

# Spoken forms for units and symbols that speech engines misread; applied in order.
SPOKEN = [
    (r"(\d)\s?m/s", r"\1 meters per second"),
    (r"(\d)\s?kg", r"\1 kilograms"),
    (r"(\d)\s?cm", r"\1 centimeters"),
    (r"(\d)\s?mm", r"\1 millimeters"),
    (r"(\d)\s?ms\b", r"\1 milliseconds"),
    (r"(\d)\s?Hz", r"\1 hertz"),
    (r"(\d)\s?N\b", r"\1 newtons"),
    (r"(\d)\s?m\b", r"\1 meters"),
    (r"(\d)\s?s\b", r"\1 seconds"),
    (r"°", " degrees"),
    (r"≈", "about "),
    (r"×", " by "),
    (r"λ", "lambda"),
    (r"σ", "sigma"),
    (r"√", " root "),
    (r"F/T", "F T"),
    (r"\bC([0-9])\b", r"C \1"),
    (r"[*_`#>\"]", " "),
    (r"\s+", " "),
]


def spoken(text: str) -> str:
    """Strip markdown and spell out units and symbols."""
    for pattern, replacement in SPOKEN:
        text = re.sub(pattern, replacement, text)
    return text.strip()


def silence(path: Path, seconds: float) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-v",
            "error",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=22050:cl=mono",
            "-t",
            str(seconds),
            str(path),
        ],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "dialogue",
        type=Path,
        help='JSON list of [speaker, text]; speaker "pause" marks a section break',
    )
    parser.add_argument("output", type=Path, help="the MP3 to write")
    parser.add_argument(
        "--voice",
        action="append",
        required=True,
        metavar="SPEAKER=MODEL.onnx",
        help="one Piper voice model per speaker, e.g. pilot=en_US-lessac-medium.onnx",
    )
    args = parser.parse_args()
    voices = dict(v.split("=", 1) for v in args.voice)
    lines = json.loads(args.dialogue.read_text())

    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp)
        short, long = work / "short.wav", work / "long.wav"
        silence(short, 0.7)
        silence(long, 1.6)
        order = []
        for i, (speaker, text) in enumerate(lines):
            if speaker == "pause":
                order.append(long)
                continue
            segment = work / f"{i:04d}.wav"
            subprocess.run(
                [
                    "piper",
                    "-m",
                    voices[speaker],
                    "-f",
                    str(segment),
                    "--sentence_silence",
                    "0.3",
                ],
                input=spoken(text).encode(),
                check=True,
                capture_output=True,
            )
            order += [segment, short]
        playlist = work / "concat.txt"
        playlist.write_text("".join(f"file '{p}'\n" for p in order))
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                str(playlist),
                "-ar",
                "22050",
                "-ac",
                "1",
                "-c:a",
                "libmp3lame",
                "-q:a",
                "4",
                str(args.output),
            ],
            check=True,
        )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
