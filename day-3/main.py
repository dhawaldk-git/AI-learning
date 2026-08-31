
from asset import Asset
from asset_manager import AssetManager

manager = AssetManager()

manager.add_asset(Asset("PUMP100", "Water Pump", "ACTIVE"))
manager.add_asset(Asset("PUMP100", "Water Pump", "ACTIVE"))
manager.add_asset(Asset("MOTOR200", "Motor", "ACTIVE"))

manager.view_assets()

asset = manager.search_asset("PUMP200")

if asset:
    asset.display()
else:
    print("Asset not found")

update_asset = manager.update_asset("PUMP100","Water Pump","INACTIVE")

if update_asset:
    update_asset.display()

manager.save_asset()

manager.load_asset()