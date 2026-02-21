from fastapi import FastAPI
import os
import time

app = FastAPI()

VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.get("/")
def root():
    return {"message": "Snapp DevOps Task - new version"}

@app.get("/version")
def version():
    return {"version": VERSION}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/cpu-load")
def cpu_load():
    start = time.time()
    while time.time() - start < 3:
        pass
    return {"status": "cpu stressed"}