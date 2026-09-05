from fastapi import APIRouter,status,HTTPException
from models.asset_model import Asset
from services.asset_service import add_asset, delete_asset,  get_assets, get_asset_by_num, update_asset
import sqlite3

def asset_not_found():
    """Raise an HTTPException for asset not found."""
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found")

router = APIRouter(
    prefix="/api/v1",
    tags=["Assets"],
)

@router.get("/assets",status_code=status.HTTP_200_OK)
def read_assets():
    return get_assets()

@router.post("/asset",status_code=status.HTTP_201_CREATED)
def create_assets(asset: Asset):
    try:
        add_asset(asset)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Asset with this assetnum already exists.")
    return {"message": "Asset added successfully"}

@router.get("/assets/{assetnum}",status_code=status.HTTP_200_OK)
def search_asset(assetnum: str):
    asset = get_asset_by_num(assetnum)
    if asset:
        return asset
    asset_not_found()

@router.put("/assets/{assetnum}",status_code=status.HTTP_200_OK)
def update(assetnum:str, asset:Asset):
    up_asset = update_asset(assetnum, asset)
    if up_asset:
        return {"Message": "Asset updated successfully"}
    asset_not_found()


@router.delete("/assets/{assetnum}",status_code=status.HTTP_200_OK)
def remove_asset(assetnum:str):
    del_asset = delete_asset(assetnum)
    if del_asset:
        return {"Message": "Asset deleted successfully"}
    asset_not_found()