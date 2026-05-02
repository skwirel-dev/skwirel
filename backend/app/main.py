from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import engine
from app.core.base import BaseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="Skwirel API", version="0.1.0", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}


@app.get("/")
def root():
    return {"message": "Skwirel API", "version": "0.1.0"}
