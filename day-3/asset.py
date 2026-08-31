class Asset:

    def __init__(self,assetnum,description,status):
        self.assetnum = assetnum
        self.description = description
        self.status = status

    def display(self):
        print(f"Asset: {self.assetnum}, "f"Description: {self.description}, "f"Status: {self.status}")

    def to_dict(self):
        return {
            "assetnum": self.assetnum,
            "description": self.description,
            "status": self.status
        }

# asset1 = Asset(
#     "PUMP100",
#     "Water Pump",
#     "ACTIVE"
# )

# # asset1.display()
# print(asset1.to_dict())