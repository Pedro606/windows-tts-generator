from pathlib import Path

from tts_generator import save_speech_to_wav
from audio_converter import wav_to_mp3


INPUT_FILE = Path(
    "data/input/script.txt"
)

OUTPUT_DIR = Path(
    "data/output"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

TEMP_WAV = OUTPUT_DIR / "speech.wav"

FINAL_MP3 = OUTPUT_DIR / "speech.mp3"


VOICE_ID = (
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
)


def main():

    if not INPUT_FILE.exists():

        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    text = INPUT_FILE.read_text(
        encoding="utf-8"
    )

    print("Generating speech...")

    save_speech_to_wav(
        text=text,
        output_wav=str(TEMP_WAV),
        voice_id=VOICE_ID,
        rate=170
    )

    print("Converting to MP3...")

    wav_to_mp3(
        str(TEMP_WAV),
        str(FINAL_MP3)
    )

    TEMP_WAV.unlink()

    print(
        f"MP3 created successfully: {FINAL_MP3}"
    )


if __name__ == "__main__":
    main()