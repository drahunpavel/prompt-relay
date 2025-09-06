"""FASTAPI server"""

import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
load_dotenv()

from api.routers import router as asr_router

FASTAPI_HOST = os.getenv('FASTAPI_HOST')
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT'))

app = FastAPI(title="FASTAPI Server")
app.include_router(asr_router, prefix="/asr", tags=["ASR"])




def main():
    """Run FASTAPI server"""
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)

if __name__ == '__main__':
    main()
