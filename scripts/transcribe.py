"""Transcribe client audio in docs/feedback/ to <name>.md next to each file.

Setup: pip install faster-whisper   (decodes audio itself, no ffmpeg needed)
Run:   python scripts/transcribe.py
"""
from pathlib import Path

from faster_whisper import WhisperModel

AUDIO_DIR = Path(__file__).resolve().parent.parent / "docs" / "feedback"
EXTS = {".ogg", ".opus", ".oga", ".m4a", ".mp3", ".wav"}

todo = [f for f in sorted(AUDIO_DIR.iterdir())
        if f.suffix.lower() in EXTS and not f.with_suffix(".md").exists()]

if todo:
    # ponytail: "small" can mishear names/numbers, switch to "medium" if accuracy is poor
    model = WhisperModel("small", device="cpu", compute_type="int8")
    for f in todo:
        segments, _ = model.transcribe(str(f), language="pt")
        f.with_suffix(".md").write_text(" ".join(s.text.strip() for s in segments) + "\n", encoding="utf-8")
        print("ok:", f.name)
else:
    print("nothing to transcribe")
