from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend_app.service.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # app startup
    yield
    # Clean up the ML models and release the resources


app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/ping")
async def ping():
    return {"ping": "pong"}
