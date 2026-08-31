assets = [
            {
                "assetnum": "PUMP100",
                "description": "Water Pump",
                "status": "ACTIVE"
            },
            {
                "assetnum": "MOTOR200",
                "description": "Electric Motor",
                "status": "ACTIVE"
            },
            {
                "assetnum": "VALVE300",
                "description": "Control Valve",
                "status": "INACTIVE"
            }
        ]


def get_all_asset():
    return assets

def get_asset(assetnum):
    for asset in assets:
        if asset['assetnum'] == assetnum:
            return asset

    return None

def get_active_assets():
    active_assets = []
    for asset in assets:
        if asset['status'] == 'ACTIVE':
            active_assets.append(asset)

    return active_assets

def add_assets(asset_dict):
    assetnum = asset_dict.get('assetnum')
    for asset in assets:
        if asset['assetnum'] == assetnum:
            return 'Asset already present'

    assets.append(asset_dict)
    print('lst',assets)
    return 'Done'

def update_assets(assetnum,status):
    for asset in assets:
        if asset['assetnum'] == assetnum:
            asset['status'] = status
            return 'Asset status updated'
    return 'Asset not found'
    
while True:
    try:
        print('\n Asset Menu')
        print('1. View asset')
        print('2. Search asset')
        print('3. Add asset')
        print('4. Update asset')
        print('5. Exit')
        view_asset = int(input('\n Enter value \n')) 
    except ValueError:
            print('Enter value between 1 to 5')
            continue
    if view_asset == 1:
        print(get_all_asset())
    elif view_asset == 2:
        assetnum = input('Enter assetnum \n')
        print(get_asset(assetnum))
    elif view_asset == 3:
        asset_dict = {}
        assetnum = input('Enter assetnum- ')
        asset_dict['assetnum'] = assetnum
        desc =  input(' Enter description- ')
        asset_dict['description'] = desc
        status =  input(' Enter status- ')
        asset_dict['status'] = status
        if assetnum and desc and status: 
            print(add_assets(asset_dict))
    elif view_asset == 4:
        assetnum = input('Enter assetnum- ')
        status =  input(' Enter status- ')
        print(update_assets(assetnum,status))
        pass
    elif view_asset == 5:
        print ('Exiting.....')
        break
    else:
        print('Invalid choice')
    

    

    
        




    