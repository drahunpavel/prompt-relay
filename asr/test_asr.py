"""test module"""

# from transcriber import Transcriber
from transcriber import Transcriber


if __name__ == "__main__":
    transcriber = Transcriber(model_size='small')
    # transcriber = Transcriber()

    WAV_PATH = "sample.small.wav"

    result = transcriber.transcribe(WAV_PATH)

    print("Text: ", result["text"])
    print("Language: ", result["language"])
    print("Waw duration: ", result["waw_duration"], "sec")
    print("Transcribe duration: ", result["transcribe_duration"], "sec")
