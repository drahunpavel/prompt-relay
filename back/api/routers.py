"""ASR API Routes"""

import tempfile
import shutil
import httpx
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse

from .config import API_TRANSCRIBE_URL

router = APIRouter()


@router.post("/transcribe")
async def transcribe_endpoint(
        audio: UploadFile = File(...),
    # task: str = Form("transcribe"),
    # language: str | None = Form(None)
):
    """Proxy to ASR service"""

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = f"{tmpdir}/{audio.filename}"

        with open(tmp_path, "wb") as f:
            shutil.copyfileobj(audio.file, f)

        async with httpx.AsyncClient() as client:
            with open(tmp_path, "rb") as f:
                files = {"audio": (audio.filename, f, audio.content_type)}
                resp = await client.post(API_TRANSCRIBE_URL, files=files)

        return JSONResponse(resp.json())
