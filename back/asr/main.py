"""asr module"""
import tempfile
import shutil

from fastapi import APIRouter, FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn

from .config import FASTAPI_HOST, FASTAPI_PORT

from .convert import to_wav_16k_mono
from .transcriber import Transcriber


app = FastAPI(title="ASR Service")
asr_router = APIRouter(prefix="/api/asr", tags=["ASR API"])

transcriber = Transcriber(model_size='small')

@asr_router.post("/transcribe")
async def asr_transcribe(audio: UploadFile = File(...)):
    """transcribe endpoint"""

    with tempfile.TemporaryDirectory() as tmpdir:
        raw_path = f"{tmpdir}/input"
        wav_path = f"{tmpdir}/output.wav"

        with open(raw_path, "wb") as f:
            shutil.copyfileobj(audio.file, f)

        to_wav_16k_mono(raw_path, wav_path)

        result = transcriber.transcribe(wav_path)

    return JSONResponse(result)

app.include_router(asr_router)

def main():
    """run ASR API"""
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)

if __name__ == '__main__':
    main()
