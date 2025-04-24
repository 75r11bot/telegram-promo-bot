
# api/main.py

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
from playwright.promo_apply import run_playwright_flow

app = FastAPI()

class PromoRequest(BaseModel):
    code: str
    chat_title: str

@app.get("/")
def root():
    return {"message": "Promo bot API is live."}

@app.post("/api/solve")
def solve_promo(req: PromoRequest):
    run_playwright_flow(req.code, req.chat_title)
    return {"message": f"Code '{req.code}' submitted for chat {req.chat_title}"}