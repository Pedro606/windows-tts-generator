# Windows TTS Generator 🎙️

Generate MP3 audio files from text using native Microsoft Windows voices.

---

## Features

- Offline Text-to-Speech
- Uses installed Windows voices
- WAV to MP3 conversion
- Simple file-based workflow
- Lightweight and fast

---

## Project Structure

```text
windows-tts-generator/
├── src/
├── data/
│   ├── input/
│   └── output/
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

Place your script inside:

```text
data/input/script.txt
```

Run:

```bash
python src/main.py
```

Generated audio:

```text
data/output/speech.mp3
```

---

## Voice Configuration

Example:

```python
VOICE_ID = (
r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
)
```

You can replace it with any installed Windows voice.

---

## Technologies

- Python
- pyttsx3
- pydub
- Microsoft Speech API

---

## Future Improvements

- Batch processing
- Multiple voice selection
- GUI interface
- Subtitle generation
- SSML support
- Docker image

---

## License

MIT