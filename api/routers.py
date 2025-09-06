"""ASR API Routes"""

import tempfile
import shutil
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from asr.convert import to_wav_16k_mono
from asr.transcriber import Transcriber

transcriber = Transcriber(model_size='small')

router = APIRouter()


@router.post("/transcribe")
async def transcribe_endpoint(
    audio: UploadFile = File(...),
    # task: str = Form("transcribe"),
    # language: str | None = Form(None)
):
    """transcribe endpoint"""

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = f"{tmpdir}/input"
        output_wav_path = f"{tmpdir}/output.wav"

        with open(input_path, "wb") as f:
            shutil.copyfileobj(audio.file, f)

        to_wav_16k_mono(input_path, output_wav_path)

        result = transcriber.transcribe(output_wav_path)

    return JSONResponse(result)
