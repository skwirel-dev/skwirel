from fastapi import FastAPI

app = FastAPI(title="Skwirel API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "version": "0.1.0"}


@app.get("/")
def root():
    return {"message": "Skwirel API", "version": "0.1.0"}
