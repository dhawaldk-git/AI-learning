from fastapi import FastAPI

app = FastAPI()

assets = [
    {
        "assetnum": "PUMP100",
        "description": "Water Pump",
        "status": "ACTIVE"
    },
    {
        "assetnum": "MOTOR200",
        "description": "Motor",
        "status": "ACTIVE"
    }
]

@app.get("/")
def home():
    return {"measseg":"Welcome to Fast API"}

@app.get("/health")
def health():
    return{"status":"UP"}

@app.get("/assets")
def get_assets():
    return assets

@app.get("/get_asset/{assetnum}")
def get_asset(assetnum:str):
    for asset in assets:
        if asset['assetnum'] == assetnum:
            return asset
    return {"Message":"Asset not found"}

@app.get("/search")
def search(status:str):
    return {"status": status}