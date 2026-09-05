from database import create_table, drop_table
# drop_table()
create_table()
from fastapi import FastAPI
from models import Asset
from service import (add_asset, get_assets, search_asset ,update_asset, delete_asset)
app = FastAPI()

@app.post("/asset")
def create_assets(asset:Asset):
    add_asset(asset)
    return {"message": "Asset added successfully"}

@app.get("/assets")
def read_assets():
    return get_assets()

@app.get("/assets/{assetnum}")
def search(assetnum:str):
    asset = search_asset(assetnum)
    if asset:
        return (asset)
    return {"message": "Asset not found"}

@app.put("/assets/{assetnum}")
def update(assetnum:str, asset:Asset):
    up_asset = update_asset(assetnum, asset)
    if up_asset:
        return {"Message": "Asset updated successfully"}
    return {"Message": "Asset not found"}

@app.delete("/assets/{assetnum}")
def remove_asset(assetnum:str):
    del_asset = delete_asset(assetnum)
    if del_asset:
        return {"Message": "Asset deleted successfully"}
    return {"Message": "Asset not found"}