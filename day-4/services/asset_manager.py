import json
from asset import Asset
class AssetManager():

    def __init__(self):
        self.assets = []
        pass

    def add_asset(self, asset):
        for ex_asset in self.assets:
            if ex_asset.assetnum == asset.assetnum:
                return "asset already exist"
        self.assets.append(asset)

    def view_assets(self):
        for asset in self.assets:
            asset.display()

    def search_asset(self, assetnum):
        for asset in self.assets:
            if asset.assetnum == assetnum:
                return asset
        return None

    def update_asset(self, assetnum, description, status):
        for asset in self.assets:
            if asset.assetnum == assetnum:
                asset.description = description
                asset.status = status
                return asset

        return False

    def save_asset(self):
        data = []

        for asset in self.assets:
            data.append(asset.to_dict())

        with open("asset.json", "w") as json_file:
            json.dump(data, json_file, indent=4)


    def load_asset(self):

        try:
            with open ("asset.json", "r") as file:
                json_data = json.load(file)

                for asset in json_data:
                    print('asset',asset)
                    self.assets.append(
                        Asset(asset["assetnum"], asset["description"], asset["status"])
                    )

        except FileNotFoundError:
            print('file not found')
