from fastapi import FastAPI

app = FastAPI()

@app.get("/api/solve")
def solve():
    return {"message": "Promo solving triggered"}
