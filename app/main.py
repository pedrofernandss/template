from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Olá Mundo!"}

@app.get("/health")
def health_check():
    return {"status": "OK"}