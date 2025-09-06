"""FASTAPI server"""

from fastapi import FastAPI
import uvicorn


from api.routers import router as asr_router
from config import FASTAPI_HOST, FASTAPI_PORT



app = FastAPI(title="FASTAPI Server")
app.include_router(asr_router, prefix="/asr", tags=["ASR"])




def main():
    """Run FASTAPI server"""
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)

if __name__ == '__main__':
    main()
