"""module asr"""
import time
from faster_whisper import WhisperModel


class Transcriber:
    """Minimum ASR layer"""

    def __init__(self,
                 #  tiny, base, small, medium, large-v2, large-v3
                 model_size="large-v3",
                 device="cpu",  # cuda | auto
                 compute_type="int8"
                 ):
        print(f'Loading model ${model_size} on device ${device}')
        self.model = WhisperModel(
            model_size, device=device, compute_type=compute_type)
        print('Model Loaded')

    def transcribe(
        self,
        wav_path: str,
        task: str = "transcribe",  # transcribe | translate
        language: str | None = None  # ru | en
    ):
        """transcribe """
        start = time.time()

        segments, info = self.model.transcribe(
            wav_path,
            task=task,
            language=language,
            vad_filter=True,  # Voice Activity Detection
            vad_parameters={"min_silence_duration_ms": 500},
            condition_on_previous_text=False
        )

        text = "".join(segment.text for segment in segments)

        duration = time.time() - start
        return {
            "text": text.strip(),
            "language": info.language,
            "waw_duration": info.duration,
            "transcribe_duration": duration
        }
