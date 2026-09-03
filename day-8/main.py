from fastapi import FastAPI
from models import Asset
from fastapi import HTTPException
app = FastAPI()

assets = [
    {
        "assetnum": "PUMP100",
        "description": "Water Pump",
        "status": "ACTIVE"
    }
]

@app.get("/assets")
def get_assets():
    return assets

@app.post("/asset")
def add_asset(asset:Asset):
    assets.append(asset.model_dump())
    print(assets)
    return {"Message":"Asset added",
            "Asset":asset}

@app.get("/asset/{assetnum}")
def get_asset(assetnum:str):
    for asset in assets:
        if asset['assetnum'] == assetnum:
            return asset
    raise HTTPException(status_code=404,detail="Asset not found")

@app.put("/asset/{assetnum}")
def update_asset(assetnum:str,updated_asset:Asset):
    for index,asset in enumerate(assets):
        if asset['assetnum'] == assetnum:
            assets[index] = updated_asset.model_dump()
            return {"Message":"Asset updated"}
    return{"Message":"Asset not found"}

@app.delete("/asset/{assetnum}")
def delete_asset(assetnum):
    for asset in assets:
        if asset['assetnum'] == assetnum:
            assets.remove(asset)
            return {"Message":"asset deleted"}
    raise HTTPException(status_code=404,detail="Asset not found")

@app.get("/search")
def search_asset(status:str):
    for asset in assets:
        if asset['status'] == status:
            return asset
    return HTTPException(status_code=404,detail="asset Not matching with status")
