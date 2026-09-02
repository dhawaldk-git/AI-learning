from pydantic import BaseModel

class Asset(BaseModel):
    assetnum:str
    description:str
    status:str
    