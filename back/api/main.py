"""FASTAPI server"""

from fastapi import FastAPI
import uvicorn


from .routers import router as asr_router
from .config import FASTAPI_HOST, FASTAPI_PORT


app = FastAPI(title="UI Service")
app.include_router(asr_router, prefix="/api/ui", tags=["UI API"])


def main():
    """Run UI API"""
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)

if __name__ == '__main__':
    main()
