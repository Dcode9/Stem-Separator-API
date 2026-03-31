"""Stem Separator API - Production-ready FastAPI application for audio stem separation."""

__version__ = "1.0.0"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stem Splitter API is live!"}
