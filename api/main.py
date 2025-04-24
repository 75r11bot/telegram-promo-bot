# api/main.py

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.promo_apply import apply_promo_code

app = FastAPI(title="Promo Code Solver API")

class PromoRequest(BaseModel):
    code: str
    url: Optional[str] = "https://example.com/promo"

@app.get("/")
def read_root():
    return {"message": "Promo Code Solver API is running."}

@app.post("/solve")
def solve_promo(data: PromoRequest):
    video_path = apply_promo_code(data.code, data.url)
    return {
        "message": f"Promo code {data.code} has been processed.",
        "video_path": video_path
    }
