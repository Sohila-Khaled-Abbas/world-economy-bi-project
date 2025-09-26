from dotenv import load_dotenv
import os, pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

load_dotenv()
DATA_FILE = os.getenv("DATA_FILE", "data/processed_data.csv")
df = pd.read_csv(DATA_FILE)

app = FastAPI(title=os.getenv("APP_NAME","Global Economy API"))

@app.get("/")
async def root():
    return {"msg":"ok","rows": len(df)}

@app.get("/summary")
async def summary():
    return JSONResponse(content=df.describe(include="all").to_dict())

@app.get("/region/{region}")
async def get_region(region: str):
    df_reg = df[df["Region"].str.lower() == region.lower()]
    if df_reg.empty:
        raise HTTPException(404, "Region not found")
    return JSONResponse(content=df_reg.to_dict(orient="records"))

@app.get("/country/{code}")
async def get_country(code: str):
    df_c = df[df["Country Code"].str.upper() == code.upper()]
    if df_c.empty:
        raise HTTPException(404, "Country not found")
    return JSONResponse(content=df_c.to_dict(orient="records"))

@app.get("/health")
async def health():
    return {"status":"healthy"}
