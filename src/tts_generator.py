import pyttsx3


def create_tts_engine(
    voice_id=None,
    rate=170
):

    engine = pyttsx3.init()

    if voice_id:
        engine.setProperty(
            "voice",
            voice_id
        )

    engine.setProperty(
        "rate",
        rate
    )

    return engine


def save_speech_to_wav(
    text,
    output_wav,
    voice_id=None,
    rate=170
):

    engine = create_tts_engine(
        voice_id=voice_id,
        rate=rate
    )

    engine.save_to_file(
        text,
        output_wav
    )

    engine.runAndWait()