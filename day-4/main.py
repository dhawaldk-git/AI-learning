
from models.asset import Asset
from services.asset_manager import AssetManager
import logging
manager = AssetManager()

# manager.add_asset(Asset("PUMP100", "Water Pump", "ACTIVE"))
# manager.add_asset(Asset("PUMP100", "Water Pump", "ACTIVE"))
# manager.add_asset(Asset("MOTOR200", "Motor", "ACTIVE"))
logging.basicConfig(
    filename='log/app.log',
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info('Application Started')
while True:
    try:
        
        print('\n Asset Menu')
        print('1. View asset')
        print('2. Search asset')
        print('3. Add asset')
        print('4. Update asset')
        print('5. Save asset')
        print('6. Load assets')
        print('7. delete asset')
        print('8. Exit')
        asset_management = int(input('\n Enter value \n')) 
    except ValueError:
            print('Enter value between 1 to 5')
            continue

    if asset_management == 1:
        manager.view_assets()
    elif asset_management == 2:
        try: assetnum = input('Enter assetnum \n') 
        except Exception as e: print(e) 
        asset = manager.search_asset(assetnum)
        if asset:
            asset.display()
        else:
            print("Asset not found")

    elif asset_management == 3:
        asset_dict = {}
        assetnum = input('Enter assetnum- ')
        asset_dict['assetnum'] = assetnum
        desc =  input(' Enter description- ')
        asset_dict['description'] = desc
        status =  input(' Enter status- ')
        asset_dict['status'] = status
        if assetnum and desc and status:
            new_asset = Asset(assetnum, desc, status)
            result = manager.add_asset(new_asset)
            # print('result',result)
            if result == 'asset already exist':
                 logging.warning(f"Asset {assetnum} already exist")
            else:
                logging.info(f"Asset {result.assetnum} added")

    elif asset_management == 4:
        assetnum = input('Enter assetnum- ')
        desc =  input(' Enter description- ')
        status =  input(' Enter status- ')
        update_asset = manager.update_asset(assetnum,desc,status)
        if update_asset:
            update_asset.display()

    elif asset_management == 5:
        manager.save_asset()

    elif asset_management == 6:
         manager.load_asset()

    elif asset_management == 7:
        assetnum = input('Enter assetnum- ')
        result = manager.delete_asset(assetnum)
        if result == True:
            logging.info(f"Asset {assetnum} deleted successfully")
        else:
             logging.warning(f"Asset {assetnum} Not found")

    elif asset_management == 8:
        print ('Exiting.....')
        logging.info(f"Exit Application")
        break

    else:
        print('Invalid choice')
    

    