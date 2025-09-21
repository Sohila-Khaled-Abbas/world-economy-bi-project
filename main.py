from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd

# Load processed dataset
DATA_FILE = "d:\courses\Data Science\Projects\Python\world-economy-bi-project\data\processed_data.csv"
df = pd.read_csv(DATA_FILE)

app = FastAPI(title="Global Economy API", description="Query World Bank + HDI data", version="1.0")

@app.get("/")
async def root():
    return {"message": "🌍 Welcome to the Global Economy API!", "rows": len(df), "columns": list(df.columns)}

@app.get("/summary")
async def summary():
    return JSONResponse(content=df.describe(include="all").to_dict())

@app.get("/region/{region}")
async def get_region(region: str):
    region_df = df[df["Region"].str.lower() == region.lower()]
    if region_df.empty:
        raise HTTPException(status_code=404, detail=f"Region '{region}' not found")
    return JSONResponse(content=region_df.to_dict(orient="records"))

@app.get("/country/{code}")
async def get_country(code: str):
    country_df = df[df["Country Code"].str.upper() == code.upper()]
    if country_df.empty:
        raise HTTPException(status_code=404, detail=f"Country Code '{code}' not found")
    return JSONResponse(content=country_df.to_dict(orient="records"))
