import os
from dotenv import load_dotenv
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

# Load .env file
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Global Economy API")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
DATA_FILE = os.getenv("DATA_FILE", "data/processed_data.csv")

# Load dataset
df = pd.read_csv(DATA_FILE)

app = FastAPI(title=APP_NAME, description="Query World Bank + HDI data", version=APP_VERSION)

@app.get("/")
async def root():
    return {
        "message": f"🌍 Welcome to {APP_NAME}!",
        "rows": len(df),
        "columns": list(df.columns)
    }
