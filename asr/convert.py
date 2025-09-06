"""
Module for converting audio to format for Whisper
WAV, 16kHz, mono
"""

import subprocess
from pathlib import Path


def to_wav_16k_mono(src_path: str, dst_path: str) -> str:
    """
       Converts audio file to WAV via ffmpeg
    """

    Path(dst_path).parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg", "-y", "-i", src_path,   # input file
        "-ac", "1",                       # single channel (mono)
        "-ar", "16000",                   # sampling frequency 16kHz
        "-vn",                            # if video - remove
        "-f", "wav",                      # output format
        dst_path
    ]

    subprocess.run(cmd, check=True, capture_output=True)

    return dst_path
