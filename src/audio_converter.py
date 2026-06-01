from pydub import AudioSegment


def wav_to_mp3(
    input_wav,
    output_mp3
):

    audio = AudioSegment.from_wav(
        input_wav
    )

    audio.export(
        output_mp3,
        format="mp3"
    )